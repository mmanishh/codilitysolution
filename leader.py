import random

def fast_leader(A):

    n = len(A)

    leader = -1
    A = sorted(A)

    candidate = A[n//2]
    count =0

    for i in range(n):
        if A[i] == candidate:
            count+=1
    
    if count > n//2:
        leader = candidate
    
    return leader

def fastest_leader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if size==0:
            size += 1
            value = A[k]
            print('value',value)
        else:
            if value != A[k]:
                size -=1
            else:
                size += 1
        
    candidate = -1
    if size >0:
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n//2:
        leader = candidate
    
    return leader

def fastest_leader_stack(A):
    
    n = len(A)
    size = 0
    stack = []
    
    for each in A:
        if len(stack) <=0:
            stack.append(each)
        else:
            if stack[-1] != each:
                stack.pop(-1)
            else:
                stack.append(each)
    
    candidate = -1
    if len(stack) > 0:
        candidate = stack[-1]

    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n//2:
        leader = candidate
    
    return leader

def dominator(A):    
    n = len(A)
    size = 0
    stack = []
    
    for each in A:
        if len(stack) <=0:
            stack.append(each)
        else:
            if stack[-1] != each:
                stack.pop(-1)
            else:
                stack.append(each)
    
    candidate = -1
    if len(stack) > 0:
        candidate = stack[-1]

    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
            index = k
    if count > n//2:
        leader = candidate
        return index
    else:
        return -1


def generate_arr(m):
    array = []
    count = 0
    while True:
        n = random.randint(100000,1000000)

        a = random.randint(100,1000)

        arr = [a] * n
         
        array.extend(arr)

        count +=1

        if count >= m:
            return array



if __name__ == '__main__':
    #A = [8,4,6,6,6,6,8,8,6]
    #A = [3,4,3,2,3,-1,3,3,5,6,7,8,9]
    #A = generate_arr(3)
    A = [2, 1, 1, 3]
    print(dominator(A))