# all negative
# single element
# missing first
# missing last

def solution(A):
    # check of array is single element
    if len(A) == 1:
        return 1 if not A[0] == 1 else A[0] + 1

    # sort array
    a = sorted(list(set(A)))

    # check for all negative
    if a[-1] < 1:
        return 1

    min_num = 1

    # check each element of the array
    for i in range(len(a)):
        cur = a[i - delta]
        if cur == min_num:
            min_num += 1
        elif cur > min_num:
            return min_num
