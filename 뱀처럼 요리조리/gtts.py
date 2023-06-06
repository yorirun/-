from gtts import gTTS

tell = input("원하는 말을 입력해줘! \n")
print(tell + " 을/를 변환하는 중...")

tts = gTTS(text=tell, lang='ko')
tts.save(r"저장위치/대사.mp3") #저장위치 지정

print("성공!"
      "\n 지정된 저장위치에서 확인해주세요!")

#by yorirun
