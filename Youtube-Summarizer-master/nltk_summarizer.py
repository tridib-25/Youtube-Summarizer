from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import re

def nltk_summarizer():
    print("nltk entered")
    # Read text from the file
    file_path = "./transcript.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Function to split text into sentences if no proper punctuation
    def split_into_sentences(text):
        # Split on common sentence-ending punctuation
        sentences = re.split(r'(?<=[.!?])\s+', text)
        # If there's only one sentence, try splitting on common conjunctions or long pauses
        if len(sentences) <= 1:
            sentences = re.split(r'\s+(?:and|but|or|because|however|therefore|so|thus|hence|consequently|moreover|furthermore|in addition|nevertheless|nonetheless|although|though|while|whereas|since|despite|in spite of|due to|as a result of|accordingly|subsequently|meanwhile|alternatively|similarly|likewise|conversely|in contrast|on the other hand|for example|for instance|specifically|namely|in particular|in other words|that is|to illustrate|to clarify|in fact|indeed|actually|in reality|as a matter of fact)\s+', text, flags=re.IGNORECASE)
        # If still one sentence, split on commas or long spaces
        if len(sentences) <= 1:
            sentences = re.split(r'(?<=,)\s+|\s{3,}', text)
        # If still one sentence, split into chunks of approximately 20 words
        if len(sentences) <= 1:
            words = text.split()
            sentences = [' '.join(words[i:i+20]) for i in range(0, len(words), 20)]
        return sentences

    # Tokenizing the text 
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 

    # Creating a frequency table to keep the score of each word 
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
    sentences = split_into_sentences(text)
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

    print("nltk exit")
    return summary.strip()

# nltk_summarizer()