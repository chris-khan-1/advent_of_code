import os

year = 2015
for i in range(4, 26):
    directory = f"./{year}/{i}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/input.txt", "w") as output_file:
        output_file.write("")
    with open(f"{directory}/instructions.txt", "w") as output_file:
        output_file.write("")
