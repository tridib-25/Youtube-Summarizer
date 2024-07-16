from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline

def pegasus():
    # Pick model
    model_name = "google/pegasus-xsum"

    # Load pretrained tokenizer
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    example_text = open('./summary_temp.txt','r',encoding="utf8").read()
    # print(example_text)

    # Define summarization pipeline
    summarizer = pipeline(
        "summarization",
        model=model_name,
        tokenizer=pegasus_tokenizer,
        framework="pt"
    )

    # summary = summarizer(example_text, min_length=100, max_length=150)
    # summary = summarizer(example_text)
    summary = summarizer(example_text, min_length=100, max_length=512,truncation=True)

    result = summary[0]["summary_text"]

    # Write the result to the output file
    # with open("./summary.txt", "w") as result_file:
    #     result_file.write(result)

    print("Result has been saved to summary.txt")
    # print(result)
    return(result)

# pegasus()