import speech_recognition as spam

print("Enter Filename to Analyze:")
filename = input()



def getText(input):
	rec = spam.Recognizer()
	file = spam.AudioFile(input)
	with file as source:
		audio = rec.record(source)
	return	rec.recognize_google(audio)


print(getText(filename)) 
