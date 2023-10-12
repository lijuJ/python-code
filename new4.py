# program to find number of lines in a given file
with open('tutebox.txt','r') as file:
   li = file.readlines()
total_line = len(li)
print(f"Number of lines in the notepad file: {total_line}")