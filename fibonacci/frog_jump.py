
def solution(A):
    N = len(A)
    F = fibonacci(N)
    print(F)
    intial = -1
    jumps = 0
    for i in range(N):
        if intial + F[i] == 1:
            intial = intial + F[i]
            jumps +=1

        if intial > N:
            return jumps
        else:
            return -1


def fibonacci(N):
    A = [0] *N
    A[1] = 1

    for i in range(2,N):
        A[i] = A[i-1]  + A[i-2]
    
    return A

if __name__ == "__main__":
    A = [0,0,0,1,1,0,1,0,0,0,0]
    print(solution(A))