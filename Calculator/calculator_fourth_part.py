# write your code here
def add(a, b):
    return str(int(a) + int(b))


def subtract(a, b):
    return str(int(a) - int(b))


def logic(sequence):

    # Separate characters from numbers
    j = 0
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

    # Putting signs together
    while True:
        j = 0
        f = True
        while j < len(sequence_1) - 1:
            if not sequence_1[j].isdigit() and not sequence_1[j + 1].isdigit():
                sequence_1[j] = sequence_1[j] + sequence_1[j + 1]
                sequence_1.pop(sequence_1.index(sequence_1[j + 1]))
                f = False
            j += 1
        if f:
            break

    # If first number is minus and last character in not a number
    if not sequence_1[0].isdigit() and sequence_1[1].isdigit():
        sequence_1[1] = sequence_1[0] + sequence_1[1]
        sequence_1.pop(sequence_1.index(sequence_1[0]))
    if not sequence_1[len(sequence_1) - 1].isdigit():
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

    # Sum all numbers
    result = sum([int(i) for i in sequence_1])
    print(result)


def main():
    while True:
        something = input()
        a = something.split()
        if something == "/exit":
            print("Bye!")
            break
        elif something == "/help":
            print("The program calculates the sum or subtraction of numbers")
            continue
        if something == "":
            continue
        if len(a) == 1:
            print(something)
            continue
        sequence = something.split()
        logic(sequence)


if __name__ == "__main__":
    main()