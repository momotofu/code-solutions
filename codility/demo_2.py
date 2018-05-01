
def solution(A):
    # single element
    if len(A) == 1:
        cur = A[0]
        return 2 if cur == 1 else 1

    # sort array and remove duplicates
    a = sorted(list(set(A)))

    # all negative
    if a[-1] < 1:
        return 1

    # all other cases
    min_num = 1 # keep track of minum possible number

    # iterate through each item and compare / update min_num
    for i in range(len(a)):
        cur = a[i]
        if cur == min_num:
            min_num += 1
        elif cur > min_num:
            return min_num

    return min_num
