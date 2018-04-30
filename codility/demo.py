# given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# single item
# all negative
# all positive

def solution(A):
    # single item
    if len(A) == 1:
        cur = A[0]
        return 2 if cur == 1 else 1

    # sort the array
    array = sorted(list(set(A))) # remove duplicates
    min_num = 1

    # check for negative use case
    if array[len(array) - 1] < 1:
        return 1

    for i in range(len(array)):
        cur = array[i]
        if cur == min_num:
            min_num += 1
        elif cur > min_num:
            return min_num

    return min_num
