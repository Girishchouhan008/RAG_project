from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "distilgpt2"
AutoTokenizer.from_pretrained(model_id).save_pretrained("models/distilgpt2")
AutoModelForCausalLM.from_pretrained(model_id).save_pretrained("models/distilgpt2")
