import sys

def max_product(A):

    A = sorted(A,reverse=True)
    print(A)
    # mx = -sys.maxsize-1
    
    # for i in range(len(A)):
    #     if i==len(A)-3:
    #         return mx

    #     result = A[i] * A[i+1] *A[i+2]
    #     i +=1
    #     if result>mx:
    #         mx = result

    sum_first = A[0] * A[1] * A[2]
    sum_last = A[-1] * A[-2] * A[0]

    if sum_first>sum_last:
        return sum_first
    else:
        return sum_last

    return mx


if __name__ =='__main__':

    #A = [-5, 5, -5, 10,7]
    A = [-3, 1, 2, -2, 5, 6]
    print(max_product(A))