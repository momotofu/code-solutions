# search for non-duplice value
def solution(A):
    """
    Uses a dictionary to keep track of duplicate values.
    Efficiency is O(2*N).
    """

    occurances = {} # create an empty dictionary to track occurances of values

    # populate occurances
    for i in range(len(A)):
        cur = A[i]
        if not cur in occurances.keys():
            occurances[cur] = 1
        else:
            occurances[cur] += 1

    # search occurances for the odd valued key
    for key in occurances.keys():
        value = occurances[key]
        if not value % 2 == 0:
            return key
