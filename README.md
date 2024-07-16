# Youtube-Summarizer : Project Overview

This project provides a streamlined way to generate concise summaries from YouTube videos. Follow the steps below to set up and run the application.

### Installation

To install the required dependencies, run : **pip install -r requirements.txt**

### Running the Application

To start the application, use : **streamlit run main.py**

### Steps

1. Extract Transcript
    * Directly from YouTube API
    * Automatic Speech Recognition (ASR)
        * Using the Whisper OpenAI model (resource-intensive)
2. Transcript Summarization
    * Abstractive Summarization
        * Using Pegasus
    * Extractive Summarization
        * Using NLTK
        * Using SpaCy
3. Metrics (To Validate Accuracy)
    * BertScore
    * ROUGE
    * METEOR

### Screenshot

<img width="1433" alt="Screenshot 2024-07-16 at 2 05 39 PM" src="https://github.com/user-attachments/assets/ee372245-e2a8-4dfc-a388-c4e381f58597">

<img width="1432" alt="Screenshot 2024-07-16 at 2 06 37 PM" src="https://github.com/user-attachments/assets/45e007fd-8551-406b-9f7c-ae9972494b09">

The Authors of this project are :

1. @Sanjeevani Lakade
2. @Shruti Gupta
3. @Spruha Thorat
4. @Tridib Nandi
