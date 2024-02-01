import gtts
import playsound
text = input("Enter the name: ")
sound = gtts.gTTS(text, lang="hi")
sound.save("my python program.mp3")
playsound.playsound("my python program.mp3")