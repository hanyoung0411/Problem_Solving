alphabet = [0]*26
word = input().upper()
for i in range(26) :
    alphabet[i] += word.count(chr(65+i))
if alphabet.count(max(alphabet)) > 1 :
    print('?')
else :
    print(chr(alphabet.index(max(alphabet))+65))
