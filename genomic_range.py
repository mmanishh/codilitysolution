
def genomic_range(S,P,Q):

    S = list(S)
    new_s = []
    result = []

    impact = {'A':1,'C':2,'G':3,'T':4}

    for s in S:
        new_s.append(impact[s])

    for i in range(len(P)):
        l ,r = P[i] , Q[i]

        sliced = new_s[l:r+1]

        result.append(min(sliced))
    
    return result



if __name__ == '__main__':

    S = 'CAGCCTA'
    P = [2,5,0]
    Q = [4,5,6]

    print(genomic_range(S,P,Q))





