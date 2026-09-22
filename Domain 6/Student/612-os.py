import os

print("Your current directory is:", os.getcwd())


os.rename(f'Domain 6/Student/601-Message.txt', f'Domain 6/Student/OLD_601-Message.txt')


for text_file in os.listdir('Domain 6/Student'):
    if text_file.endswith('.txt'):
        print(text_file)

