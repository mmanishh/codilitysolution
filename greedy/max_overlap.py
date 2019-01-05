
def solution(A, B):
    # No overlapping is possible.
    if len(A) < 2:      
        return len(A)
    count = 1       # The first segment starts a new cluster.
    end = B[0]
    index = 1       # The second segment.
    while index < len(A):
        # Skip all the segments in this cluster.
        while index < len(A) and A[index] <= end:
            index += 1
        print('end:',end)
        print('start:',A[index])
        # All segments are processed.
        if index == len(A):
            break
        # Start a new cluster.
        count += 1
        
        end = B[index]
    return count


if __name__ == "__main__":
    A = [1,3,7,9,9]
    B = [5,6,8,9,10]

    print(solution(A,B))