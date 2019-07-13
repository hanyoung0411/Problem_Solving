scores = []
for i in range(5) :
    scores.append(int(input()))
    if scores[i] < 40 :
        scores[i] = 40
print(int(sum(scores)/5))
