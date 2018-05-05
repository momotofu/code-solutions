# V between U and W if U < V < W or U > V > W
# A[P] < A[Q] and A[P] != A[Q], and no value lies
# strictly between

# values cant equal each other. Max distance, which is absolute difference
# between indicies.

def solution(A):
    """
    Computes the pair indices in the array, and then returns the
    maximum distances between an index pair.
    """
    # find all pair indices
    max_value = 0 # keep track of max value

    # make a dictionary of every occuring integer, with an array with indice values.
    occurances = {}
    for i in range(len(A)):
        cur = A[i]
        if not cur in occurances.keys():
            occurances[cur] = []
        occurances[cur].append(i)

    # keep track of largest distance
    max_distance = 0
    # adjacent_values = []
    prev = []
    prev_set = False

    # populate adjecent_values
    for key, value in sorted(occurances.items()):
        if not prev_set:
            prev = value
            prev_set = True
        else:
            for i in range(len(prev)):
                for j in range(len(value)):
                    # adjacent_values.append((prev[i], value[j]))
                    distance = get_distance(prev[i], value[j])
                    if distance > max_distance:
                        max_distance = distance
            prev_set = False

    # otherwise return -1
    return -1 if max_distance == 0 else max_distance

def get_distance(x, y):
    return abs(x - y)
