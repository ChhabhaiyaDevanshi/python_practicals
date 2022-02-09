# 20CE011-Chhabhaiya Devanshi
# https://github.com/ChhabhaiyaDevanshi/python_pra2/blob/main/20CE011_prac3.py

# Find Captain Room Number
# Sample Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# Sample Output
# 8
# Explanation: The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
# Hence, 8 is the Captain's room number.

a = int(input())  # take input from the user
room = list(map(int, input().split()))  # take input elements as in list
for i in room:  # loop for counting the repeataion of elements
    b = room.count(i)
    if b == 1:  # if count is 1, it means that elemennt is not repeated
        print(i)  # print that element
