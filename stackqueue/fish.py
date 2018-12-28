def solution(A, B):
    survivals = 0
    stack = []
     
    for idx in xrange(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
                         
            else:
                survivals += 1
        else:
            stack.append(A[idx])
             
    survivals += len(stack)
     
    return survivals

if __name__ == "__main__":
    A = [4,3,2,1,5]
    B = [0,1,0,0,0]

    print(solution(A,B))
    