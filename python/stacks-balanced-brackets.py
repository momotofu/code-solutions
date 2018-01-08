def get_symbol_map():
    return {'{': '}', '[': ']', '(': ')'}

def get_opening_symbols():
    return ['{', '[', '(']

def get_closing_symbols():
    return ['}', ']', ')']

def is_matched(expression, symbol_map):
    # [({})]{}()

    # run splits through stack
    # check if first half of stack matches last half of splits
    # return boolean
    print(split_brackets(expression, symbol_map))

def split_brackets(expression, symbol_map):
    """
    Separates brackets into groups and returns a list
    containing those groups.
    """
    # split balanced brackets
    # search through brackets until opposite brackets.
    # remember count
    # then capture count brackets forwards

    closing_symbols = get_closing_symbols()
    symbols_list = []

    current_search = expression[0]

    index = 0
    count = 0
    while (index < len(expression)):
        for i in range(index, len(expression)):
            if expression[i] in closing_symbols:
                index += count
                symbols_list.append(expression[get_brackets_length(symbols_list):index])
                count = 0
                break
            count += 1
            index += 1

    return symbols_list

def get_brackets_length(list):
    output = ''
    for el in list:
        output += el
    return len(output)

t = int(input().strip())
for _ in range(t):
    expression = input().strip()
    if is_matched(expression, get_symbol_map()) == True:
        print("YES")
    else:
        print("NO")
