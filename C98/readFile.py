from fileinput import filename


entry = input("Enter file name here: ")
f = open(entry)

wordCount = 0

filelines = f.readlines()

for line in filelines:
    words = line.split()
    print(words)
    wordCount = wordCount + len(words)
    print(line)
    print(wordCount)

