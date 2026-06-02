# 1. Alternate Number Series

n = 10
for i in range(1, n + 1):
    if i % 2 == 0:
        print(-i)
    else:
        print(i)


# 2. Number and Reverse Both Prime

num = int(input())

rev = int(str(num)[::-1])

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if prime(num) and prime(rev):
    print("Both are prime")
else:
    print("Not prime")


# 3. Adam Number

num = int(input())

if int(str(num**2)[::-1]) == (int(str(num)[::-1]))**2:
    print("Adam Number")
else:
    print("Not Adam Number")


# 4. Duck Number

num = input()

if '0' in num:
    print("Duck Number")
else:
    print("Not Duck Number")


# 5. Circular Prime

num = input()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

flag = True

for i in range(len(num)):
    rot = num[i:] + num[:i]
    if not is_prime(int(rot)):
        flag = False
        break

if flag:
    print("Circular Prime")
else:
    print("Not Circular Prime")


# 6. Automorphic Number

num = int(input())

if str(num*num).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")


# 7. Peterson Number

import math

num = int(input())

s = 0
for i in str(num):
    s += math.factorial(int(i))

if s == num:
    print("Peterson Number")
else:
    print("Not Peterson Number")


# 8. Spiral Matrix Printing

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

top = 0
bottom = len(mat)-1
left = 0
right = len(mat[0])-1

while top <= bottom and left <= right:

    for i in range(left, right+1):
        print(mat[top][i], end=" ")
    top += 1

    for i in range(top, bottom+1):
        print(mat[i][right], end=" ")
    right -= 1

    if top <= bottom:
        for i in range(right, left-1, -1):
            print(mat[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            print(mat[i][left], end=" ")
        left += 1

print()


# 9. AI Message Recovery System

s = input()

def palindrome(x):
    return x == x[::-1]

ans = "NO"

for i in range(len(s)):
    if palindrome(s[:i] + s[i+1:]):
        ans = "YES"
        break

print(ans)


# 10. Missing Sensor Detection System

n = int(input())
arr = list(map(int, input().split()))

total = n * (n + 1) // 2

print(total - sum(arr))


# 11. Duplicate Product Detection Engine

arr = input().split()

flag = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            flag = True

if flag:
    print("Duplicate Found")
else:
    print("No Duplicate")


# 12. Trending Keyword Analyzer

words = input().split()

d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

mx = max(d.values())

ans = []

for k, v in d.items():
    if v == mx:
        ans.append(k)

print(sorted(ans)[0])


# 13. Banking Fraud Prevention System

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("Transaction Denied")
        else:
            print("Transaction Approved")

balance = int(input())
amount = int(input())

obj = BankAccount(balance)
obj.withdraw(amount)


# 14. Cybersecurity Access Violation Detector

authorized = set(input().split())
attempted = set(input().split())

unauthorized = attempted - authorized

print("Unauthorized Users =", unauthorized)


# 15. Rocket Launch Eligibility Checker

fuel = int(input())
payload = int(input())

if fuel >= 5000 and payload <= 1000:
    print("Launch Approved")
else:
    print("Launch Rejected")


# 16. Aircraft Collision Warning System

import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distance < 10:
    print("Collision Risk")
else:
    print("Safe")


# 17. Secure Password Strength Analyzer

pwd = input()

upper = False
lower = False
digit = False

for ch in pwd:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True

if len(pwd) >= 8 and upper and lower and digit:
    print("Strong Password")
else:
    print("Weak Password")


# 18. University Scholarship Evaluation System

n = int(input())

students = []
topper = ""
top_avg = 0

for i in range(n):
    data = input().split()

    name = data[0]
    marks = list(map(int, data[1:]))

    avg = sum(marks) / 5

    students.append((name, avg))

    if avg > top_avg:
        top_avg = avg
        topper = name

print("Topper :", topper)

print("Scholarship Eligible:")

for name, avg in students:
    if avg >= 90:
        print(name)