
with open("numbers.dat", "w") as file:
    for number in range(0, 101):
        file.write(str(number) + "\n")


with open("numbers.dat", "r") as file:
    print(file.read())