# write your code here

# From Infix to PostFix Algorithm
def infixToPostfix(expression):
    Operators = {'+', '-', '*', '/', '(', ')', '^'}  # collection of Operators

    Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators

    stack = []  # initialization of empty stack

    output = []

    for character in expression:
        if character not in Operators:  # if an operand append in postfix expression
            output.append(character)
        elif character == '(':  # else Operators push onto stack
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(character)
    while stack:
        output.append(stack.pop())
    return output


def calculate(inputs):
    stack = []
    for a in inputs:
        if a.isdigit():
            stack.append(a)
            continue

        op_1, op_2 = stack.pop(), stack.pop()

        if a == '+':
            stack.append(add(op_2, op_1))
        elif a == '-':
            stack.append(subtract(op_2, op_1))
        elif a == '*':
            stack.append(multiplication(op_2, op_1))
        elif a == '/':
            stack.append(division(op_2, op_1))
        elif a == '^':
            stack.append(power(op_2, op_1))

    return stack.pop()


# Driver program to test above function
def add(a, b):
    return str(float(a) + float(b))


def subtract(a, b):
    return str(float(a) - float(b))


def multiplication(a, b):
    return str(float(a) * float(b))


def division(a, b):
    return str(float(a) / float(b))


def power(a, b):
    return str(float(a) ** float(b))


def logic(sequence, operators):
    md = ["/", "*"]
    pm = ["-", "+"]
    pars = ["(", ")"]

    # Separate characters from numbers
    sequence_1 = []
    for i in sequence:
        marks = []
        digits = []
        for r in i:
            if r.isdigit():
                digits.append(r)
            else:
                marks.append(r)
        if len(marks) != 0:
            sequence_1.append("".join(marks))
        if len(digits) != 0:
            sequence_1.append("".join(digits))

    # Invalid expressions with multiplications and divisions
    j = 0
    f = False
    while True:
        if j == len(sequence_1) - 1:
            break
        if sequence_1[j] in md and sequence_1[j + 1] in md:
            print("Invalid expression")
            f = True
            break
        j += 1
    if f:
        return True

    # Putting signs together
    j = 0
    nums = []
    marks = []
    temp_seq = []
    sequence_1.append(" ")
    while True:
        if j == len(sequence_1) - 1:
            break
        if sequence_1[j].isdigit():
            nums.append(sequence_1[j])
            if not sequence_1[j + 1].isdigit():
                temp_seq.append("".join(nums))
                nums.clear()
        if sequence_1[j] in pm:
            marks.append(sequence_1[j])
            if sequence_1[j + 1].isdigit() or sequence_1[j + 1] in md or sequence_1[j + 1] in pars or sequence_1[j + 1] == "^":
                temp_seq.append("".join(marks))
                marks.clear()
        if sequence_1[j] in md:
            marks.append(sequence_1[j])
            if sequence_1[j + 1].isdigit() or sequence_1[j + 1] in pm or sequence_1[j + 1] in pars or sequence_1[j + 1] == "^":
                temp_seq.append("".join(marks))
                marks.clear()
        if sequence_1[j] in pars:
            temp_seq.append(sequence_1[j])
        if sequence_1[j] == "^":
            temp_seq.append(sequence_1[j])
        j += 1
    sequence_1 = temp_seq

    # If first number is minus and last character in not a number
    if sequence_1[0] in pm and sequence_1[1].isdigit():
        sequence_1[1] = sequence_1[0] + sequence_1[1]
        sequence_1.pop(sequence_1.index(sequence_1[0]))
    if sequence_1[len(sequence_1) - 1] in operators:
        sequence_1.pop()

    # Combining signs in to one (except first number)
    j = 1
    while j < len(sequence_1) - 1:
        w = 0
        p = 0
        for n in sequence_1[j]:
            if n == "-":
                w += 1
            if n == "+":
                p += 1
        if w != 0 and w % 2 == 0:
            sequence_1[j] = "+"
        elif w != 0:
            sequence_1[j] = "-"
        elif w == 0 and p != 0:
            sequence_1[j] = "+"
        elif sequence_1[j] == "-+" or sequence_1[j] == "+-":
            sequence_1[j] = "-"
        j += 1

    # Left and right parentheses must be equal
    if "(" in sequence_1 or ")" in sequence_1:
        k = 0
        for i in sequence_1:
            if i == pars[0]:
                k += 1
            if i == pars[1]:
                k -= 1
        if k != 0:
            print("Invalid expression")
            return True

    postfix_result = infixToPostfix(sequence_1)

    finish_result = int(float(calculate(postfix_result)))
    return finish_result


def dict_operations(operation, ves, *args):
    lst_keys = ves.keys()
    if operation == "check":
        if args[0] in lst_keys:
            return True
        else:
            return False
    if operation == "add":
        ves.update({args[0]: args[1]})
    if operation == "delete":
        pass


def variables_logic(ves):
    """
    input is expression

    return is string with "+", "-" and numbers
    """

    begin_str = input().strip()

    # If empty input
    f = False
    if begin_str == "":
        f = True
    if f:
        return True

    # if we want to know variable
    j = 0
    for _ in begin_str:
        j += 1
    if j == 1:
        return begin_str

    # If name variable -> 'alpha+number' or vise versa
    begin_str = begin_str + " "
    f = False
    j = 0
    while True:
        if begin_str[j].isalpha() and begin_str[j + 1].isdigit():
            print("Invalid identifier")
            f = True
            break
        if begin_str[j].isalpha() and begin_str[j - 1].isdigit():
            print("Invalid identifier")
            f = True
            break
        if j == len(begin_str) - 1 or begin_str[j] == "=":
            break
        j += 1
    if f:
        return True

    lst_str_1 = begin_str.strip().split()
    txt_1 = "".join(lst_str_1)
    lst_str = txt_1.strip().split("=", 1)

    # Checking right side of "="
    f = False
    j = 0
    while True:
        if "=" in begin_str:
            if lst_str[len(lst_str) - 1].isdigit():
                dict_operations("add", ves, lst_str[0], lst_str[len(lst_str) - 1])
                break
            elif lst_str[len(lst_str) - 1].isalpha():
                if dict_operations("check", ves, lst_str[len(lst_str) - 1]):
                    value = ves.get(lst_str[len(lst_str) - 1])
                    dict_operations("add", ves, lst_str[0], value)
                    break
                else:
                    print("Unknown variable")
                    f = True
                    break
            else:
                print("Invalid assignment")
                f = True
                break
        if j == len(begin_str) - 1:
            break
        j += 1
    if f:
        return True

    # Put numbers from dictionary instead of variables
    pre_final_expression = "".join(lst_str)
    close_final = list(pre_final_expression)
    f = False
    j = 0
    while True:
        if dict_operations("check", ves, close_final[j]):
            value = close_final[j]
            close_final[j] = ves.get(value)
        if j == len(close_final) - 1:
            break
        j += 1
    if f:
        return True

    # Final result
    final_expression = "".join(close_final)
    if "=" in begin_str:
        return True
    return final_expression


def main():
    ves = {}
    operators = ["-", "+", "*", "/"]
    parentheses = ["(", ")"]
    commands = ["/exit", "/help"]
    while True:
        expression = variables_logic(ves)
        if isinstance(expression, bool):
            continue
        something = expression
        a = something.split()

        if something == "/exit":
            print("Bye!")
            break
        elif something == "/help":
            print("The program calculates expression of numbers")
            continue

        # If /Unknown command
        f = False
        for _ in something:
            if something[0] == "/" and something not in commands:
                print("Unknown command")
                f = True
                break
        if f:
            continue

        # If it is alphabet
        if len(something) == 1 or something.isalpha():
            if dict_operations("check", ves, something):
                print(ves[something])
            else:
                print("Unknown variable")
            continue

        # If there 'number-' or 'number+'
        f = False
        for i in a:
            r = False
            for n in i:
                if n.isdigit():
                    r = True
                    break
            if r and len(i) > 1 and i[len(i) - 1] in operators:
                print("Invalid expression")
                f = True
                break
        if f:
            continue

        # Rotating '+number' to 'number'
        if len(a) == 1 and something[0] == "+":
            something = something.strip("+")

        # If string is just a number
        if len(something) == 1 and something.isdigit():
            print(something)
            continue

        # If two numbers in a row
        j = 0
        f = False
        while True:
            if j == len(a) - 1:
                break
            if a[j].isdigit() and a[j + 1].isdigit():
                print("Invalid expression")
                f = True
                break
            j += 1
        if f:
            continue

        # Making list from expression string
        sequence = []
        r = []
        j = 0
        # lst_r = ""
        for i in something:
            if i.isdigit():
                r.append(i)
            if i in operators or i in parentheses or i == "^":
                if len(r) == 0:
                    pass
                else:
                    lst_r = "".join(r)
                    sequence.append(lst_r)
                sequence.append(i)
                r.clear()
                j += 1
                continue
            if j == len(something) - 1:
                lst_r = "".join(r)
                sequence.append(lst_r)
            j += 1

        finish = logic(sequence, operators)
        if finish is True:
            continue
        else:
            print(finish)


if __name__ == "__main__":
    main()
