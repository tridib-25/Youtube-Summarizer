from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline

def pegasus_summarizer():
# Pick model
    model_name = "google/pegasus-xsum"

    # Load pretrained tokenizer
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    with open('transcript.txt',encoding="utf8") as f:
        example_text = f.read()

    # Define PEGASUS model
    # pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    # Create tokens
    # tokens = pegasus_tokenizer(example_text, truncation=True, max_length=512, padding="max_length")

    # Define summarization pipeline
    summarizer = pipeline(
        "summarization",
        model=model_name,
        tokenizer=pegasus_tokenizer
    )

    # summary = summarizer(example_text,truncation=True)
    lengthhh = 512 if len(example_text)>512 else len(example_text)
    print(lengthhh)
    print("transcript length= "+str(len(example_text)))

    # def chunkstring(str, length):
    #     return(str[0+i:length+i] for i in range(0,len(str),length))
    
    # example_txt_fixedlen=list(chunkstring(example_text,512))
    # # print(example_txt_fixedlen)

    # result=""
    # for txt in example_txt_fixedlen:
    #     summary=summarizer(txt)
    #     result+=summary[0]["summary_text"]

    summary = summarizer(example_text, min_length=100, max_length=512,truncation=True)
    result=summary[0]["summary_text"]
    # # summary = summarizer(example_text)
    # summary = summarizer(example_text, min_length=100, max_length=300, truncation=True)
    # print(result)
    # result="hi"
    return(result)
    # summary_text = open("testing.txt", 'w', encoding="utf-8")
    # summary_text.write(result)
    # summary_text.close()

# pegasus_summarizer()
