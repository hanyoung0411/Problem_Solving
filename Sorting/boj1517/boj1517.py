def bubble_sort(array,length,end) :
    while length > 0 :
        for i in range(length) :
            if array[i] > array[i+1] :
                array[i], array[i+1] = array[i+1], array[i]
        length -= 1
        end -= 1
        if end == 0 :
            return array

N,K = map(int,input().split())
numbers = list(map(int,input().split()))
sorted_array = bubble_sort(numbers, len(numbers)-1, K)
for i in range(N) :
    print(numbers[i],end=' ')
