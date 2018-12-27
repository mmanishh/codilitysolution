
def coins(n):

    result = 0
    coin = [0] * (n+1)
    for i in range(1,n+1):
        k = i
        while(k<=n):
            coin[k] = (coin[k]+1)%2
            k +=i
        
        result += coin[i]
    print(coin)
    return result


if __name__ == "__main__":
    print(coins(10))