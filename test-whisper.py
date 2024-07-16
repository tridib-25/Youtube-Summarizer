import whisper

model = whisper.load_model("tiny")
# audio = whisper.load_audio("audiofile.mp3")
# audio = whisper.pad_or_trim(audio)
# mel = whisper.log_mel_spectrogram(audio).to(model.device)
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

result = model.transcribe("audiofile.mp3")
# time.sleep(2)
# result = model.transcribe("audiofile.mp3",fp16=False)
final_data=""
with open("transcript.txt","w") as f:
    final_data+=result["text"]

    f.write(result["text"])
# os.remove('./audiofile.mp3')
print("done")
print(final_data)
