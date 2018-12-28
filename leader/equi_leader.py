
def leader(A):
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


def equi_leader(A):
    N = len(A)
    l = leader(A)

    if l == -1:
        return 0
    else:
        leader_count  = len([i for i in A if i==l])
    
    equi_leaders = 0
    leader_count_so_far =0

    for i in range(N):
        if A[i] == l:
            leader_count_so_far +=1
        
        if leader_count_so_far > (i+1)//2 and leader_count-leader_count_so_far > (N-i-1)//2:

            equi_leaders += 1
        
    
    return equi_leaders

if __name__ == "__main__":
    A = [4,3,4,4,4,2]

    print(equi_leader(A))