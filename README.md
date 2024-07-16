#project  overview
pip install -r requirements.txt

to run application:
streamlit run main.py

Steps:
1. Extract Transcript
    - A. Directly from yt API
    - B. ASR(Automatic speech recognition)
        - i. Whisper OpenAI model (heavy)
2. Transcript summarization
    - A. Abstractive
        - i. Pegasus
    - B. Extractive
        - i. nltk
        - ii. Spacy
3. Metrics(To validate accuracy)
     - A. BertScore
     - B. Rogue
     - C. Meteor
  
Screenshot:
![image](https://github.com/shrutiiigupta/youtube-summarizer/assets/98140693/406c7b46-149a-4157-8b58-f493d5d3571e)



The Authors of this project are:
1. [Sanjeevani Lakade](https://github.com/sanjeevani-25)
2. [Shruti Gupta](https://github.com/shrutiiigupta)
3. [Spruha Thorat](https://github.com/Spruha017)
4. [Tridib Nandi](https://github.com/tridib-25)

    
