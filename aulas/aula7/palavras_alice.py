
file = open('alice.txt')
dictionary = {}

text = file.read()

words = text.split()
for word in words:
   if word not in dictionary.keys():
       dictionary[word] = 1
   else:
       dictionary[word] += 1



print(dictionary)
pass