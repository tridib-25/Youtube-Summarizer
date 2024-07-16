import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def bart_summarizer():
    file = open('transcript.txt', "r")
    FileContent = file.read().strip()

    print(len(FileContent))


    checkpoint = "sshleifer/distilbart-cnn-12-6"

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

    print(tokenizer.model_max_length )
    print(tokenizer.max_len_single_sentence)
    print(tokenizer.num_special_tokens_to_add() )

    import nltk
    nltk.download('punkt')
    sentences = nltk.tokenize.sent_tokenize(FileContent)

    print(max([len(tokenizer.tokenize(sentence)) for sentence in sentences]))


    length = 0
    chunk = ""
    chunks = []
    count = -1
    for sentence in sentences:
        count += 1
    combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

    if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
        chunk += sentence + " " # add the sentence to the chunk
        length = combined_length # update the length counter

        # if it is the last sentence
        if count == len(sentences) - 1:
            chunks.append(chunk.strip()) # save the chunk
        
    else: 
        chunks.append(chunk.strip()) # save the chunk
        
        # reset 
        length = 0 
        chunk = ""

        # take care of the overflow sentence
        chunk += sentence + " "
        length = len(tokenizer.tokenize(sentence))
    print(len(chunks))
    print([len(tokenizer.tokenize(c)) for c in chunks])

    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]


    for input in inputs:
        output = model.generate(**input)
        print(tokenizer.decode(*output, skip_special_tokens=True))
        answerText = tokenizer.decode(*output, skip_special_tokens=True)

    # answer = open("summary.txt",'w')
    # answer.write(answerText)
    # answer.close()
    # print(answerText)
    return(answerText)

# bart_summarizer()