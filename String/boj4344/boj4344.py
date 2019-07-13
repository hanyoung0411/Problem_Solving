C = int(input())
for _ in range(C) :
    scores = list(map(int,input().split()))
    N = scores.pop(0)
    average = sum(scores)/len(scores)
    student_num = 0
    for i in range(len(scores)) :
        if scores[i] > average :
            student_num += 1
    print('{:.3f}%'.format(student_num / len(scores) * 100))
