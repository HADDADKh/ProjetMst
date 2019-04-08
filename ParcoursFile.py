from gtts import gTTS
import os
import speech_recognition as sr
import sys
from time import sleep
#import speech
from label import *
from gtts import gTTS	   
from time import sleep
import os
import pyglet
import playsound
import sounddevice as sd
from rec import *
from videor import *

r=sr.Recognizer();

def TTS(question, i):
   language='fr'
   myob=gTTS(question,lang=language,slow=False)
   myob.save('Question'+str(i)+'.mp3')
   return myob
   
def STT(voix):
	with sr.AudioFile(voix) as source:
	 audio=r.listen(source)
	print(r.recognize_google(audio, language = 'fr'))

   
fichier = open("emotion.txt", "w") 
			
theFile= open('Question.txt', 'r') 
duration = 20 
for lignenumber,ligne in enumerate(theFile) :
	   #Afficher la question
	   
	   print(ligne)
	   
	   #Tranformation de Texte en Voix
	   

	   tts = gTTS(text=ligne, lang='fr')
	   #Sauvgarder la question

	   filename ='C:/Users/Arbing/Desktop/Code/questions/question'+str(lignenumber)+'.mp3'
	   tts.save(filename)
	   
	   #Pronnociation de la question
	   playsound.playsound(filename, True)
	   print ('Vous avez 10 seconds pour parler')
	   rec_fun(lignenumber,duration)
	   
	   
	   
	   #detection d'emotion  et sauvgarder le video
	   x=llsb(lignenumber,duration)
	   #Sauvgarder les emotion de personne aprés chaque question
	   fichier.write('Emotion du personne par rapport au question du robot numéro  '+'  '+ str(lignenumber)) 
	   fichier.write('-'+x) 
	   fichier.write('\n')
	   #Transformation de la voix au Texte
	   STT("C:/Users/Arbing/Desktop/Code/reponses/reponse"+str(lignenumber)+".wav")

	   
	 
fichier.close()
	 
theFile.close()
