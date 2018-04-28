def solution(N):
    # convert N to binary string
    b_string = bin(N)[2:]

    # iterate through string searching for maximum gap
    # initiate search
    # count zeros until reaching next 1
    # check if last iteration
    searching = False
    max_gap = 0
    cur_total = 0

    for i in range(len(b_string)):
        cur = b_string[i]
        if cur == '1':
            if not searching:
                searching = True
            # only update max_gap if capped 1 is reached
            elif searching:
                if cur_total > max_gap:
                    max_gap = cur_total
                cur_total = 0

        if searching and cur == '0':
            cur_total += 1

    return max_gap
