def tocount():
    inp="none"
    first = []
    filtered = []
    count = int(input("Enter the number of numbers \n"))
    for i in range(count):
        inp = int(input())
        first.append(inp)
    choice = int(input("1. Multiple of the number 2. Ending with a number. 3. Both conditions. \n"))
    if choice == 1:
        devisor = int(input("Enter the divisor \n"))
        for i in range(count):
            if first[i] % devisor == 0:
                filtered.append(first[i])
        output_format = int(input("1. Print the amount 2. Print the quanity.\n"))
        if output_format == 1:
            print(sum(filtered))
        elif output_format == 2:
            print(len(filtered))
    elif choice == 2:
        last = int(input("Enter the last number \n"))
        for i in range(count):
            if first[i] % 10 == last:
                filtered.append(first[i])
        output_format = int(input("1. Print the amount 2. Print the quanity.\n"))
        if output_format == 1:
            print(sum(filtered))
        elif output_format == 2:
            print(len(filtered))
    elif choice == 3:
        devisor = int(input("Enter the devisor \n"))
        last = int(input("Enter the last number \n"))
        for i in range(count):
            if first[i] % devisor == 0 and first[i] % 10 == last:
                filtered.append(first[i])
        output_format = int(input("1. Print the amount 2. Print the quanity. \n"))
        if output_format == 1:
            print(sum(filtered))
        elif output_format == 2:
            print(len(filtered))
type_choice = int(input("1. With the input of a number of numbers. 2. With a final 0. "))
if type_choice == 1:
    tocount()
# elif type_choice == 2:
#     tozero()


                

