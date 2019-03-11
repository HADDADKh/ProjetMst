from gtts import gTTS
import os
import speech_recognition as sr
import sys
from time import sleep
from label import *
r=sr.Recognizer();

def TTS(question, i):
   language='fr'
   myob=gTTS(question,lang=language,slow=False)
   myob.save('Question'+str(i)+'.mp3')
   return myob
   
def STT(voix):
	with sr.AudioFile(voix) as source:
	 audio=r.listen(source)
	print(r.recognize_google(audio))

#def play(voix):
#   from pygame import mixer
#   mixer.init()
#   mixer.music.load(voix)
#   mixer.music.play()
   
fichier = open("emotion.txt", "w") 
			
theFile= open('Question.txt', 'r') 
#print ("error")   
for lignenumber,ligne in enumerate(theFile) :
	   #Afficher la question
	   
	   print(ligne)
	   
	   #Tranformation de Texte en Voix
	   
	   voix=TTS(ligne, lignenumber)
	   
	   #Activer le voix
	   
	   #play(voix)
	   
	   #---------------------------
	   #Robot en situation d'ecout exemple 5 mls
	   sleep(5)
	   
	   #detection d"emotion (audio_video)

	   x=llsb()
	   #Transformation de voix en texte
	   fichier.write('Emotion du personne paraport question du robot  ') 
	   fichier.write(x) 
	   fichier.write('\n')
	   #Speach to text
	   STT("Rep%s.wav" % str(lignenumber+1))

	   
	 
fichier.close()
	 
theFile.close()
