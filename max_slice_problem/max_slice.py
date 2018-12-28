

def max_slice(A):
    max_end = 0
    max_slice = 0
    for i,a in enumerate(A):
        max_end = max(0,max_end+a)
        max_slice = max(max_slice,max_end)
        print(i,'max_end:',max_end,'max_slice:',max_slice)
    
    return max_slice

def quadratic_max_slice(A):

    n = len(A)
    result =0

    for p in range(n):
        sum =0
        for q in range(p,n):
            sum += A[q]
            result = max(result,sum)
    
    return result

def max_double_slice(A):

    n = len(A)
    k1 = [0] * n
    k2 = [0] * n

    for i in range(1,n-1):
        k1[i] =  max(k1[i-1]+A[i],0)
    
    for i in reversed(range(1,n-1)):
        k2[i] = max(k2[i+1]+A[i],0)
    
    result = 0

    print('k1',k1)
    print('k2',k2)

    for i in range(1,n-1):

        result = max(result, k1[i-1] + k2[i+1])
    
    return result


            



if __name__ == "__main__":
    #A = [5,-7,3,5,-2,4,-1]
    A = [3,2,6,-1,4,5,-1,2]
    print(max_double_slice(A))