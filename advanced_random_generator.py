from random import randint

print("##########################")
print("#                        #")
print("#     By Trollagent      #")
print("#                        #")
print("##########################")
print("")

while True:
    custom_file = input("Do you want to import an .txt file: ")
    if custom_file == "yes" or custom_file == "no":
        break
    else:
        print('Please type in "yes" or "no"')

if custom_file == "yes":

    while True:
        file_name = input('Whats the file name (without ".txt"): ')
        try:
            file_read = open(f"{file_name}.txt", "r").read()
            file = open(f"{file_name}.txt", "w")
            break
        except Exception:
            print(f"{file_name} is not a valid file!")

    while True:
        min_number = input("Min. Number: ")
        max_number = input("Max. Number: ")
        try:
            min_number = int(min_number)
            max_number = int(max_number)
            break
        except Exception:
            print("Please enter two valid numbers!")

    randoms = []
    result = []

    names_file = file_read.split("\n")
    lenght = names_file.__len__()
    
    for i in names_file:
        randoms.append(randint(min_number, max_number))

    for i in range(1, lenght + 1):
        result.append(f"{names_file[i - 1]}:{randoms[i - 1]}")

    for i in result:
        if i == result[lenght - 1]:
            file.write(str(i))
        else:
            file.write(str(i) + "\n")

    file.close()

elif custom_file == "no":

    while True:
        how_many_number = input("How many Number do you want: ")
        try:
            how_many_number = int(how_many_number)
            break
        except Exception:
            print(f"{how_many_number} is not a number!")

    while True:
        min_number = input("Min. Number: ")
        max_number = input("Max. Number: ")
        try:
            min_number = int(min_number)
            max_number = int(max_number)
            break
        except Exception:
            print("Please enter two valid numbers!")

    while True:
        names = input("Do you want custom names for each random Number: ")
        if names == "yes" or names == "no":
            break
        else:
            print('Please type in "yes" or "no"')

    randoms = []
    result = []

    for i in range(1, how_many_number + 1):
        randoms.append(randint(min_number, max_number))

    if names == "no":
        result = randoms
    elif names == "yes":
        names = []
        for i in range(1, how_many_number + 1):
            names.append(input(f"Enter Name number {i}: "))
        for i in range(1, how_many_number + 1):
            result.append(f"{names[i - 1]}:{randoms[i - 1]}")

    print(result)

    while True:
        save = input("Do you want to save it: ")
        if save == "yes" or save == "no":
            break
        else:
            print('Please type in "yes" or "no"')

    if save == "yes":
        file_name = input('File Name (without ".txt"): ')
        file = open(f"{file_name}.txt", "w")
        lenght = result.__len__()
        for i in result:
            if i == result[lenght - 1]:
                file.write(str(i))
            else:
                file.write(str(i) + "\n")
        file.close()
    elif save == "no":
        pass

input("Press enter to close")
