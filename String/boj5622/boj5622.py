word = input()
result = 0
for alphabet in word :
    if ord(alphabet)-65 < 15 :
        result += (ord(alphabet)-65) // 3 + 3
    elif ord(alphabet)-65 >= 15 and ord(alphabet)-65 <= 18 :
        result += 8
    elif ord(alphabet)-65 >= 19 and ord(alphabet)-65 <= 21 :
        result += 9
    else  :
        result += 10
print(result)
