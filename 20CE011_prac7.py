# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.The two halves contain the same characters but their frequencies do not match.Your task is simple. Given a string, you need to tell if it is a lapindrome.
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc

# Output:
# YES
# NO
# YES
# YES
# NO
# NO

N = int(input())
string = []

for i in range(N):
    string.append(input())

for i in range(N):
    s = str(string[i])
    s1, s2 = '', ''
    l = len(s)

    if(l % 2 == 0):
        s1 = s[:l//2]
        s2 = s[l//2:]

    else:
        s1 = s[:l//2]
        s2 = s[l//2+1:]

    if sorted(s1) == sorted(s2):
        print("YES")

    else:
        print("NO")
