def chocolates_naive(N,M):
    count =0
    A = list(range(N))
    i = 0
    while True:

        

        if A[i] == -1:
            return count
        else:
            A[i] = -1
            count +=1
            i = (i+M) % len(A)
            #print(i)

def gcd(p, q):
  if q == 0:
    return p
  return gcd(q, p % q)
 
def lcm(p,q):
    return p * (q / gcd(p,q))
 
def chocolates(N, M):
    return lcm(N,M)/M


if __name__ == "__main__":
    print(chocolates(100000000,30000))
