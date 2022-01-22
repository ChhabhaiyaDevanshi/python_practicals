# Find runner-up from given list
# Sample Input
# 5
# 2 3 6 6 5
# Sample Output
# 5
# Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

n = input()  # take input
a = list(map(int, input().split()))  # take input of elements
mylist = sorted(a)  # store sorted elements in mylist var
myset = set(mylist)  # convert list into set to avoid repetation
mylist = list(myset)  # convert set into list
maximum = max(mylist)  # find maximum value
mylist.remove(maximum)  # remove max value from list
maximum = max(mylist)  # find maximum value from updated list
print(maximum)  # print maximum
