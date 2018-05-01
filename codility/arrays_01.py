from collections import deque
# rotate array A right K amount of times

def solution(A, K):
    """
    Creates a new empty array of the same size of the input
    array, and reasigns values in the correct rotated order
    """
    output_array = deque(A, maxlen=len(A))
    n = len(A)

    # prevent repeated rotations
    if K > n and n > 1:
        K = K % n

    # reassign list items to correct index
    for i in range(len(A)):
        output_array[(i + K) % n] = A[i]
    return list(output_array)
