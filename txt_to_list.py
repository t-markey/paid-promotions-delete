from random import randint


#input = input()
# add input or make command line argument



# opens file in current directory
file = open("keywords.txt", "r")
list = []
for line in file:
	line = line[:-1]
	list.append(line)
	if " " in line:
		phrase = line.split(" ")
		for word in phrase:
			list.append(word)

#print(list)
file.close()

filesuffix = str(randint(0,100))
newfilename =  "keywords" + filesuffix + ".py"
newfile = open(newfilename, 'x')
newfile = open(newfilename, 'w')
content = "KEYWORDS = " + str(list)
print (content)
newfile.write(content)




newfile.close()

