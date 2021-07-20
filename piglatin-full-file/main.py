def pigLatin(a):
  cons = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
  vowels = "aeiuoAEIOU"
  
  counter = 0
  purgatory = ""
  word = ""

  #first letter is a consonant condition
  if a[0] in cons:
    #for loop for consonant movement, breaks if a vowel   is found
   for i in range(len(a)):
      #if y is at the end of a cluster
      if a[i] == "y":
        break
      #moving consonants
      if a[i] in cons:
        purgatory = purgatory + a[i]
        counter = counter + 1
      if a[i] in vowels:
        break
      if a == " ":
        break
        
  #first letter is a vowel condition
  if a[0] in vowels:
    word = "y" + a + "yay"
    return word

  word = a[counter:] + purgatory + "ay"
  return word

#working the file
file = open('mrhippo.txt')
writeFile  = open('pigLatin.txt', 'w')

for line in file:
  words = line.lower()
  words = words.split(' ')
  for word in words:
    writeFile.write(pigLatin(word) + ' ')

writeFile.flush()
writeFile.close()