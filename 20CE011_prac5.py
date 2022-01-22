# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

str = input()

for i in str:
    if i.islower() == True:
        str += i.upper()

    elif i.isupper() == True:
        str += i.lower()

    else:
        str += i

print(str)
