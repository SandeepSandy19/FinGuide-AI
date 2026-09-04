import torch 
from transformers import AutoModelForCausalLM , AutoTokenizer , BitsAndBytesConfig
from peft import LoraConfig , get_peft_model

MODEL_ID = 'google/gemma-4-E4B-it'

MAX_SEQ_LENGTH = 2048

LORA_TARGET_MODULES = [
    'q_proj','k_proj','v_proj','o_proj',
    'gate_proj','up_proj','down_proj'
]

def main() :
    print("CUDA available:", torch.cuda.is_available())

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA GPU is required for this smoke test.")

    # --------------------------------------------------
    # 1. Quantization
    # --------------------------------------------------

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    # --------------------------------------------------
    # 2. Tokenizer
    # --------------------------------------------------

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    # --------------------------------------------------
    # 3. Load quantized model
    # --------------------------------------------------

    print("\nLoading model...")

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config = quantization_config,
        device_map = 'auto',
        torch_dtype = torch.bfloat16,
    )

    print("Model Loaded")

    # --------------------------------------------------
    # 4. Attach LoRA
    # --------------------------------------------------

    lora_config = LoraConfig(
        r = 16,
        lora_alpha= 32,
        lora_dropout=0.05 ,
        target_modules=LORA_TARGET_MODULES,
        bias='none',
        task_type='CASUAL_LM'
    )

    model = get_peft_model(model, lora_config)

    print('\n LoRA attached')
    model.print_trainable_parameters()

    # --------------------------------------------------
    # 5. GPU memory after model + LoRA
    # --------------------------------------------------

    torch.cuda.reset_peak_memory_stats()

    allocated = torch.cuda.memory_allocated() / 1024**3
    reserved  = torch.cuda.memory_reserved() / 1024**3

    print(f"\nGPU allocated: {allocated:.2f} GB")
    print(f"GPU reserved:  {reserved:.2f} GB")

    # --------------------------------------------------
    # 6. Create a real 2048-token test example
    # --------------------------------------------------

    messages = [
        {
            'role' : 'user',
            'content' : (
                "### Context\n"
                "A company reported revenue of $500 million and "
                "operating income of $75 million.\n\n"
                "### Question\n"
                "What is the operating margin?"
            ),
        } ,
        {
            'role' : 'assistent',
            "content" : (
                "The operating margin is 15%, calculated as "
                "operating income divided by revenue."
            ),
        },
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize = False,
        add_generation_prompt = False,
    )

    inputs = tokenizer(
        text,
        return_tensors = 'pt',
        truncation = True,
        max_length = MAX_SEQ_LENGTH
    )

    input = {
        key : value.to(model.device) for key, value in inputs.items()
    }

    # --------------------------------------------------
    # 7. Forward + backward
    # --------------------------------------------------

    labels = inputs['input_ids'].clone()

    # Smoke test only:
    # calculate loss over the sequence.
    outputs = model(
        **inputs,
        labels = labels,
    )

    loss = outputs.loss 

    print("\nForward pass successful.")
    print("Loss:", loss.item())

    loss.backward()

    print("Backward pass successful.")

    # --------------------------------------------------
    # 8. Peak memory
    # --------------------------------------------------

    peak_memory = (
        torch.cuda.max_memory_allocated() / 1023**3
    )

    print(f"\nPeak GPU memory: {peak_memory:.2f} GB")

    print("\nSMOKE TEST PASSED.")

if __name__ == "__main__":
    main()
