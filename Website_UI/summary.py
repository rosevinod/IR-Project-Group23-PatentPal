from transformers import PegasusForConditionalGeneration, PegasusTokenizer, AutoTokenizer
import torch

model_name = 'google/pegasus-big_patent'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

def get_summary(input_text):
	batch = tokenizer.prepare_seq2seq_batch(input_text, truncation=True, padding='longest', return_tensors='pt').to(device)
	translated = model.generate(**batch)
	tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
	return tgt_text[0]
	


