def chocolates(N,M):
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


if __name__ == "__main__":
    print(chocolates(100000000,30000))
