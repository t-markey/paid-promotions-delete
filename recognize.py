import speech_recognition as spam
from keywords88 import KEYWORDS
import pprint
#==============================

print("Enter Filename to Analyze:")
filename = input()


# takes in .wav, outputs list of words 
def getText(input):
	rec = spam.Recognizer()
	file = spam.AudioFile(input)
	with file as source:
		rec.adjust_for_ambient_noise(source)
		audio = rec.record(source,offset = 12, duration= 30)
	sample =rec.recognize_google(audio)
	list = sample.split(' ')
	#show all possible translations	
	#possibilities  =rec.recognize_google(audio, show_all=True)
	#pprint.pprint(possibilities)
	return list



# Takes in list of key words and spam , Reutrns set of matches
'''
def matching (spam_sample, spam_keywords):
	matches = set( spam_keywords) & set (getText(spam_sample))
	return matches
'''





#takes in a list
def repititions(list_input):
	count = dict()
	for word in list_input:
		if word in count:
			count[word] +=1
		else:
			count[word]= 1

	return count

	



#================================
sample_spam =getText(filename)
print(getText(filename)) 
matches = set(KEYWORDS) & set(sample_spam)
print (matches)
#print(KEYWORDS)

print(repititions(sample_spam))

