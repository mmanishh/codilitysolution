
def triangle(A):

    A = sorted(A,reverse=True)

    dict_a = {k: v for k,v in enumerate(A)}
    result = 0

    if len(A) < 3:
        return 0

    for each in dict_a:
        
        P = int(each) 
        Q = int(each)+1
        R = int(each)+2
        #print(P,Q,R)
        if dict_a[P]+dict_a[Q] > dict_a[R] and dict_a[Q]+dict_a[R] > dict_a[P] and dict_a[R]+dict_a[P] > dict_a[Q]:
            result = 1
        
        if each>=len(A)-3:
            return result
        
    return result


if __name__ =="__main__":
    #A= [10,50,5,1]
    #A = [10,2,5,1,8,20]
    A = [5]
    print(triangle(A))
