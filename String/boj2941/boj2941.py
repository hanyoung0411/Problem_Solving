word = input()
croat_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in range(8) :
    word = word.replace(croat_alpha[i],chr(i+65))
print(len(word))
