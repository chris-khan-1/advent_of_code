# import os

# year = 2015
# for day in range(5, 26):
#     directory = f"./{year}/{day}"
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     with open(f"{directory}/input.txt", "w") as output_file:
#         output_file.write("")
#     with open(f"{directory}/instructions.txt", "w") as output_file:
#         output_file.write("")
#     with open(f"{directory}/day_{day}_solution.py", "w") as output_file:
#         output_file.write(
#             f"""\n\nif __name__ == "__main__":
#     with open("{directory}/input.txt", "r") as input_file:
#         pass

#     with open("{directory}/solution.txt", "w") as output_file:
#         output_file.write(
#             f"Part 1: ")
#         output_file.write(
#             f"Part 2: ")"""
#         )
#     with open(f"{directory}/test_day_{day}_solution.py", "w") as output_file:
#         output_file.write("")
