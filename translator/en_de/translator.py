from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def eng_ger_translate(question):

    tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_en_de", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_en_de")
    sentence = question
    input_ids = tokenizer(sentence, return_tensors="pt", add_special_tokens=False).input_ids
    output_ids = model.generate(input_ids)[0]
    return tokenizer.decode(output_ids, skip_special_tokens=True)

def ger_eng_translate(question):
    tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_de_en", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_de_en")
    sentence = question
    input_ids = tokenizer(sentence, return_tensors="pt", add_special_tokens=False).input_ids
    output_ids = model.generate(input_ids)[0]
    return tokenizer.decode(output_ids, skip_special_tokens=True)