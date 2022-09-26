print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        if float(first_number) == 0:
            print('неопределенность')
        else:
            print('бесконечность')
    else:
        print(answer)