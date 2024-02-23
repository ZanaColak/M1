import os

os.makedirs("os_exercises", exist_ok=True)

filename1 = os.path.join("os_exercises", "exercise1.txt")
with open(filename1, "w") as file:
    user_input = input("Enter text for exercise1.txt: ")
    file.write(user_input)

filename2 = os.path.join("os_exercises", "exercise2.txt")
with open(filename2, "w") as file:
    user_input = input("Enter text for exercise2.txt: ")
    file.write(user_input)

for filename in [filename1, filename2]:
    with open(filename, "r") as file:
        file_content = file.read()
        print(f"Content of {filename}:")
        print(file_content)
