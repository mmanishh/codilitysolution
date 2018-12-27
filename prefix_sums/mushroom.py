
def prefix_sums(A):

    n = len(A)
    p = [0] * (n+1)

    for k in range(1,n+1):

        p[k] = p[k-1] + A[k-1]
    
    return p

def count_total(P,x,y):
    return P[y+1] - P[x]

def mushrooms(A,k,m):

    n = len(A)
    result = 0
    pref = prefix_sums(A)

    for p in range(min(m,k)+1):
        left_pos = k - p
        right_pos = min (n-1,max(k,k+m-2*p)) 
        result = max(result, count_total(pref,left_pos,right_pos))
    
    for p in range(min(m+1,n-k)):
        right_pos = k +p 
        left_pos = max(0,min(k, k- (m-2*p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result


if __name__ =="__main__":
    A = [2,3,7,5,1,3,9]
    print("prefix sum:",mushrooms(A,4,6))