import os

#current directory
print(os.getcwd())

#list files in current directory
print(os.listdir('.'))

#remove a file
os.remove('file_to_remove.txt')  # Uncomment to remove a file