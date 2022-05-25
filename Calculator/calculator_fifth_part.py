# write your code here
def add(a, b):
    return str(int(a) + int(b))


def subtract(a, b):
    return str(int(a) - int(b))


def logic(sequence):

    print(sequence)

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
    print(sequence_1)

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
        if sequence_1[j] == "-" or sequence_1[j] == "+":
            marks.append(sequence_1[j])
            if sequence_1[j + 1].isdigit():
                temp_seq.append("".join(marks))
                marks.clear()
        j += 1
    sequence_1 = temp_seq
    print(sequence_1)

    # If first number is minus and last character in not a number
    if not sequence_1[0].isdigit() and sequence_1[1].isdigit():
        sequence_1[1] = sequence_1[0] + sequence_1[1]
        sequence_1.pop(sequence_1.index(sequence_1[0]))
    if not sequence_1[len(sequence_1) - 1].isdigit():
        sequence_1.pop()

    print(sequence_1)
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

    print(sequence_1)
    # Main calculations
    j = 0
    while True:
        if j >= len(sequence_1) - 1:
            break
        if sequence_1[j] == "+":
            sequence_1[j] = add(sequence_1[j - 1], sequence_1[j + 1])
            sequence_1.remove(sequence_1[j - 1])
            sequence_1.remove(sequence_1[j])
            continue
        elif sequence_1[j] == "-":
            sequence_1[j] = subtract(sequence_1[j - 1], sequence_1[j + 1])
            sequence_1.remove(sequence_1[j - 1])
            sequence_1.remove(sequence_1[j])
            continue
        else:
            j += 1

    print(sequence_1)
    # Sum all numbers
    result = sum([int(i) for i in sequence_1])
    print(result)


def main():
    while True:
        something = input().strip()
        a = something.split()

        # If empty input
        if something == "":
            continue

        if something == "/exit":
            print("Bye!")
            break
        elif something == "/help":
            print("The program calculates the sum or subtraction of numbers")
            continue

        # If /Unknown command
        for i in something:
            if i == "/":
                print("Unknown command")
                continue

        # If there is alphabet
        f = False
        for i in something:
            if i.isalpha():
                print("Invalid expression")
                print("1")
                f = True
                break
        if f:
            continue

        # If there 'number-' or 'number+'
        f = False
        for i in a:
            r = False
            for n in i:
                if n.isdigit():
                    r = True
                    break
            if r and len(i) > 1 and not i[len(i) - 1].isdigit():
                print("Invalid expression")
                f = True
                break
        if f:
            continue

        # Rotating '+number' to 'number'
        if len(a) == 1 and something[0] == "+":
            something = something.strip("+")

        # If string is just a number
        if len(a) == 1:
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
                print("3")
                f = True
                break
            j += 1
        if f:
            continue
        print(something)
        sequence = something.split()
        print(sequence)
        logic(sequence)


if __name__ == "__main__":
    main()
