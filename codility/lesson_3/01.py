# tests

# empty array
# single element
# missing first or last element
# double element

def solution(A):
    # sort the array
    a = sorted(A)

    # check if array is empty
    if len(a) == 0:
        return 1

    # if single element
    if len(a) == 1:
        return a[0] + 1 if a[0] == 1 else 1

    # iterate through each element and check with index
    delta = a[0]
    for i in range(delta, a[-1]):
        if not i == a[i - delta]:
            return i

    # check if first or last element is missing
    if a[0] is not 1:
        return 1
    else:
        return a[-1] + 1
