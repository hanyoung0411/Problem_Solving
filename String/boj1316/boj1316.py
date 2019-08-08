N = int(input())
result = 0
for _ in range(N) :
    word = input()
    alphabet = []
    alphabet.append(word[0])
    isgroup = True
    for i in range(1,len(word)) :
        if word[i] == alphabet[-1] :
            continue
        elif not (word[i] in alphabet):
                alphabet.append(word[i])
        else :
            isgroup = False
    if isgroup :
        result += 1
print(result)
            
