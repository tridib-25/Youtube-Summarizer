# YouText : Youtube Summarizer : Project Overview

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

<img width="1440" alt="Screenshot 2024-07-16 at 3 01 35 PM" src="https://github.com/user-attachments/assets/5bcb82a7-7b69-4254-bb49-ef8f0fcbc549">

<img width="1440" alt="Screenshot 2024-07-16 at 3 02 09 PM" src="https://github.com/user-attachments/assets/f05faeae-0936-44d1-8c20-65f4e2d5bbac">

The Authors of this project are:

1. [Sanjeevani Lakade](https://github.com/sanjeevani-25)
2. [Shruti Gupta](https://github.com/shrutiiigupta)
3. [Spruha Thorat](https://github.com/Spruha017)
4. [Tridib Nandi](https://github.com/tridib-25)

    
