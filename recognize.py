import speech_recognition as spam
from keywords88 import KEYWORDS
#==============================

print("Enter Filename to Analyze:")
filename = input()



def getText(input):
	rec = spam.Recognizer()
	file = spam.AudioFile(input)
	with file as source:
		audio = rec.record(source)
	sample =rec.recognize_google(audio)
	list = sample.split(' ')
	return list


#def matching (spam_sample, spam_keywords):
	






#================================
sample_spam =getText(filename)
print(getText(filename)) 
matches = set(KEYWORDS) & set(sample_spam)
print (matches)
#print(KEYWORDS)
