from pytube import YouTube
import whisper
import os

def audio_to_text(link):

    try:
        # link='https://youtu.be/Wn9iALMyS7c?si=q0LYZBrR9mSbj2b7'
        video = YouTube(link)
        # video.set_filename('audio_file')
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"audiofile.mp3")
        print("audio file generated")

        model = whisper.load_model("tiny")

        audio = whisper.load_audio("audiofile.mp3")
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        if (max(probs, key=probs.get) !='en'):
            print("Can't perform ASR on other languages.")
            return("Can't perform ASR on other languages.")
        else:
            print("performing..")
            result = model.transcribe("audiofile.mp3")
            # time.sleep(2)
            # result = model.transcribe("audiofile.mp3",fp16=False)
            final_data=""
            with open("transcript.txt","w") as f:
                final_data+=result["text"]
                f.write(result["text"])
            
            # os.remove('./audiofile.mp3')
            print("done")
            return('1')
        
    except:
        print("Couldn't find audio")
        return("Couldn't find audio")


    # except:
    #     print("ASR error")
    #     return("ASR error")
    
    # return("hieie")

    # text = open("transcript.txt",'w')
    # text.write(clean_data)
    # text.close()

    # return("hiiiiiiiiii")

# audio_to_text()