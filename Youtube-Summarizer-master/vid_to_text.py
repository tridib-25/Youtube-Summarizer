from youtube_transcript_api import YouTubeTranscriptApi as yta
import audio_to_text
import freq
# import pegasus_summarizer
import nlp_summarizer
import streamlit as st
from method4_nltk_and_pegasus import m1_nltk
import BART_summarizer
import pegasus_summarizer
import nltk_summarizer

# flag_here=""


def vid_to_text(link, vid_id, flag):

    # hindi - harman singh - manual script - https://youtu.be/Wn9iALMyS7c?si=q0LYZBrR9mSbj2b7
    # --- https://www.youtube.com/watch?v=Wn9iALMyS7c

    # hindi - netflix death note dhruv rathee - no script allowed - https://www.youtube.com/watch?v=H3nzTmNlS4I&t=32s
    # eng - power couple - auto-generated only - https://www.youtube.com/watch?v=6dpF_G3yMMQ
    # eng - manual(default) - veryyyy long vid - 892 words transcript haha - https://www.youtube.com/watch?v=1qbna6t1bzw
    # what is  python - english - https://www.youtube.com/watch?v=Y8Tko2YC5hA
    # fraz google - https://www.youtube.com/watch?v=ZSoTKpKGkCU
    # tedx - https://www.youtube.com/watch?v=P6FORpg0KVo
    # martin luther - https://youtu.be/_IB0i6bJIjw?si=2ZKZqi9uCfHC486K
    # Ranveer Allahbadia - https://www.youtube.com/watch?v=3wBEUuV7BYg
    # eng -manual script - 5 Fascinating Missions in Space | Planet Explorers: Full Series | BBC Earth Lab - https://www.youtube.com/watch?v=kvfa-6Pr36w
    # en - mba speech - no transcript - https://www.youtube.com/watch?v=e0HlQh-hwyE

    # verrryy long vids
    # https://www.youtube.com/watch?v=7CqJlxBYj-M
    # https://www.youtube.com/watch?v=PkZNo7MFNFg&t=8560s

    english_language_codes = [
        'en',
        'en-AU',
        'en-BZ',
        'en-CA',
        'en-IE',
        'en-JM',
        'en-NZ',
        'en-ZA',
        'en-TT',
        'en-GB',
        'en-US',
        'en-IN']

    # transcript_list = yta.list_transcripts(vid_id)
    # transcript = transcript_list.find_transcript(english_language_codes)
    # print(transcript.language,transcript.language_code)
    # transcript.translation_languages,

    # data = transcript.fetch()
    # print(data)

    global flag_here
    flag_here = flag

    try:
        print("transcript try1 --> manual scripts only")
        transcript_list = yta.list_transcripts(vid_id)
        transcript = transcript_list.find_manually_created_transcript(
            english_language_codes)
        data = transcript.fetch()
        # print(
        # # a list of languages the transcript can be translated to
        # transcript.translation_languages,
        # )
        # print(data)
        # data = yta.get_transcript(vid_id)
        # print(data)
        print("done")
        return (clean_text(data))
    except:
        try:
            print("transcript try2 --> auto-generated scripts english")
            # data = transcript.find_generated_transcript(vid_id, languages=['en'])
            data = yta.get_transcript(vid_id, languages=english_language_codes)
            print("done")
            return (clean_text(data))
        except:
            print("transcript try3 --> ASR")
            data = audio_to_text.audio_to_text(link)
            print("done")
            if (data == '1'):
                data = only_summary()
            else:
                data = "audio_to_text return != 1"
            return (data)

    # return("kkklkl")


def clean_text(data):
    print(flag_here)
    print("clean_text entered")
    final_data = ''
    for val in data:
        for key, value in val.items():
            if key == 'text':
                final_data += ' ' + value
    # script=''
    # for x in data:
        #     t = x["text"]
        # 	if t != '[Music]':
        # 		script += t + " "

    # print(final_data)
    # process_data = final_data.splitlines()
    # clean_data = ''.join(process_data)
    # print(clean_data)
    text = open("transcript.txt", 'w', encoding='utf-8')
    text.write(final_data)
    text.close()
    print("done")

    # method 1
    # summary_data=freq.main_freq()

    # method 2 --> spacy nlp summmarizer
    # summary_data=nlp_summarizer.nlp_spacy_summarizer()

    # summary_text = open("summary.txt",'w',encoding="utf-8")
    # summary_text.write(summary_data)
    # summary_text.close()

    # return(final_data)
    return (only_summary())


def only_summary():
    print(flag_here)
    print("only_summary entered")

    if (flag_here == '00'):
        # method 5 --> nltk only
        summary_data = nltk_summarizer.nltk_summarizer()

    elif (flag_here == '01'):
        # method 2 --> spacy nlp summmarizer
        summary_data = nlp_summarizer.nlp_spacy_summarizer()

    elif (flag_here == '10'):
        # method 5 --> pegasus only
        summary_data = pegasus_summarizer.pegasus_summarizer()

    elif (flag_here == '11'):
        # method 3 --> bart
        summary_data = BART_summarizer.bart_summarizer()

    summary_text = open("summary.txt", 'w', encoding="utf-8")
    summary_text.write(summary_data)
    summary_text.close()
    print("Summary Done")

    # print(summary_data)
    # return(final_data)
    return (summary_data)

    # method 4 --> nltk + pegasus
    # summary_data = m1_nltk.nltk()

    # method 1
    # summary_data=freq.main_freq()
