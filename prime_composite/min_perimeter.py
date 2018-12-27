import sys

def min_perm_rect(N):

    i = 1
    prime = True
    result = sys.maxsize
    while i*i <= N:
        
        if N % i == 0:
            A = i
            B = N // i
            p = perimeter(A,B)
            result = min(result,p)
            prime= False
        
        if prime:
            return perimeter(N,1)
        
        i +=1
    
    return result




def perimeter(A,B):
    return 2 * (A+B)


if __name__ == "__main__":
    print(min_perm_rect(100000000))