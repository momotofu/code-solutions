def get_symbol_map():
    return {'{': '}', '[': ']', '(': ')'}

def get_opening_symbols():
    return ['{', '[', '(']

def get_closing_symbols():
    return ['}', ']', ')']

def is_matched(expression, symbol_map):
    opening_symbols = get_opening_symbols()
    index = 0
    cur = expression
    while(index != len(cur)):
        for i in range(0, len(cur)):
            index += 1
            # print("cur: ", cur)
            # check for match
            a = cur[i]
            if a in opening_symbols and i + 1 < len(cur):
                if symbol_map[a] == cur[i + 1]:
                    cur = cur[:i] + cur[i + 2:]
                    index = 0
                    break

    if len(cur) == 0:
        return True
    else:
        return False

def split_brackets(expression, symbol_map):
    """
    Separates brackets into groups and returns a list
    containing those groups. Only works with balanced brackets.
    """
    # split balanced brackets
    # search through brackets until opposite brackets.
    # remember count
    # then capture count brackets forwards

    closing_symbols = get_closing_symbols()
    brackets_list = []

    current_search = expression[0]

    index = 0
    count = 0
    while (index < len(expression)):
        for i in range(index, len(expression)):
            if expression[i] in closing_symbols:
                index += count
                brackets_list.append(expression[get_brackets_length(brackets_list):index])
                count = 0
                break
            count += 1
            index += 1

    print(brackets_list)

    return brackets_list

def get_brackets_length(list):
    output = ''
    for el in list:
        output += el
    return len(output)

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression, get_symbol_map()) == True:
        print("YES")
    else:
        print("NO")
