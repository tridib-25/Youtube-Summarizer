from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from method4_nltk_and_pegasus import m2_pegasus
# import m2_pegasus

def nltk():
    # Read text from the file
    file_path = "./transcript.txt"
    with open(file_path, "r",encoding="utf8") as file:
        text = file.read()
        # print(text)

    # Tokenizing the text 
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 

    # Creating a frequency table to keep the 
    # score of each word 
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence 
    sentences = sent_tokenize(text) 
    sentenceValue = dict() 

    for sentence in sentences: 
        for word, freq in freqTable.items(): 
            if word in sentence.lower(): 
                if sentence in sentenceValue: 
                    sentenceValue[sentence] += freq 
                else: 
                    sentenceValue[sentence] = freq 

    sumValues = 0
    for sentence in sentenceValue: 
        sumValues += sentenceValue[sentence] 

    # Average value of a sentence from the original text 
    average = int(sumValues / len(sentenceValue)) 

    # Determine the maximum number of words based on the size of the text
    num_words_limit = 500 if len(words) > 2000 else float('inf')

    # Storing sentences into our summary. 
    summary = '' 
    word_count = 0
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            words_in_sentence = len(word_tokenize(sentence))
            if word_count + words_in_sentence <= num_words_limit:
                summary += " " + sentence 
                word_count += words_in_sentence
            else:
                break

    # Write the summary to the output file
    with open("summary_temp.txt", "w",encoding="utf8") as output_file:
        output_file.write(summary)

    print("Summary has been saved to summary_temp.txt")
    return(m2_pegasus.pegasus())

# nltk()