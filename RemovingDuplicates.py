
def remove_duplicates(argument):
  duplicates = 0
  characters = []
  for char in argument:
    if char.lower() in characters:
      duplicates = duplicates + 1
    else:
      characters.append(char.lower())
  characters.sort()
  return "".join(characters), duplicates
  print(characters)




remove_duplicates("how are you you today ")


#MINEEEE

def function2(word):
  duplicates = 0
  noduplicates = []

  for char in word:
    if char not in noduplicates:
      noduplicates.append(char)
    else:
      duplicates =+ 1
  return noduplicates
  print (noduplicates)



function2("i am here today ")

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
for x in myList:
  if x not in cleanlist:
    cleanlist.append(x)
print (cleanlist)