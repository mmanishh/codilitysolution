import random

def passing_cars(A):
    zeros = []
    ones = []
    for i,a in enumerate(A):
        if a == 0:
            zeros.append(i)
        if a == 1:
            ones.append(i)
    
    count = 0
    for z in zeros:
        count += sum([z<i for i in ones])

    return count

def generate_array(limit):
    count = 0
    array = []
    while True:

        array.append(random.randint(0,1))
        count +=1

        if count>=limit:
            return array
        



if __name__ == '__main__':
    A = [0,1,0,1,1]
    print(passing_cars(generate_array(10000)))