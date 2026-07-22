import torch

from datasets import load_dataset

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    BitsAndBytesConfig
)

from peft import LoraConfig, get_peft_model

# --------------------------------------------------
# Configuration
# --------------------------------------------------

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("Abirate/english_quotes")


def tokenize(example):
    return tokenizer(
        example["quote"],
        truncation=True,
        padding="max_length",
        max_length=128
    )


tokenized_dataset = dataset["train"].map(tokenize)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto"
)

# --------------------------------------------------
# QLoRA
# --------------------------------------------------

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

print("\nTrainable Parameters")
model.print_trainable_parameters()

training_args = TrainingArguments(
    output_dir="./qlora_output",
    per_device_train_batch_size=2,
    learning_rate=2e-4,
    num_train_epochs=2,
    logging_steps=10,
    save_strategy="no",
    fp16=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
)

trainer.train()

print("\nFinal Training Loss:", trainer.state.log_history[-1]["loss"])

if torch.cuda.is_available():
    print(
        "Peak GPU Memory:",
        round(torch.cuda.max_memory_allocated() / 1024**3, 2),
        "GB"
    )

# --------------------------------------------------
# Test Prompts
# --------------------------------------------------

prompts = [
    "Explain Artificial Intelligence.",
    "What is Machine Learning?",
    "Write a short poem about nature."
]

print("\n==============================")

for prompt in prompts:

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    print("\nPrompt:", prompt)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))