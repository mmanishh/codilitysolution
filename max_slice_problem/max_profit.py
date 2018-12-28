

def max_profit(A):

    if len(A) <=1:
        return 0
    else:
        min_price = A[0]
        max_sofar = 0
        max_ending = 0

        for i in range(1,len(A)):

            max_ending = max(0, A[i] - min_price)
            min_price = min(min_price,A[i])
            max_sofar = max(max_sofar,max_ending)
    
    return max_sofar

if __name__ == '__main__':
    A = [23171,21011,21123,21366,21013,21367]
    print(max_profit(A))