# Youtube-Summarizer : Project Overview

This project provides a streamlined way to generate concise summaries from YouTube videos. Follow the steps below to set up and run the application.

### Installation

To install the required dependencies, run : ** pip install -r requirements.txt **

### Running the Application

To start the application, use : ** streamlit run main.py **

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
