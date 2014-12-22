# PROJECT EULER Problems
#
# List of already-implemented methods for use in later problems:
# l:109 prime(n) returns a boolean, True if n is prime
# l:137 prod_13(n, arr) returns the product of 13 consecutive 
#                 numbers starting at arr[n]
# l:202 check_div(n, arr) checks if any e in arr divides n
# triangle(n) returns the nth triangle number
# prime_fac(n) returns an array of the prime factors of n
# num_factors(n) returns the number of factors of n
# len_Collatz(n) returns the Collatz number of n

import time

###############
## PROBLEM 1 ##
###############

start = time.time()
a = 0
b = 0
while (a < 1000):
  if (a % 3 == 0 or a % 5 == 0): b = a + b
  a += 1
end = time.time()
print 'Problem 1:', b
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#233168



###############
## PROBLEM 2 ##
###############

start = time.time()
a = 1
b = 1
d = 0
while (b < 4000000):
  if (b % 2 == 0): d = d + b
  c = b + a
  a = b
  b = c
end = time.time()
print 'Problem 2:', d
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#4613732



###############
## PROBLEM 3 ##
###############

start = time.time()
a = 600851475143
b = 2
while (b < a ** 0.5):
  if (a % b == 0):
    a = a / b
  else: b += 1
end = time.time()
print 'Problem 3:', a
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#6857



###############
## PROBLEM 4 ##
###############

start = time.time()
# we assume that a,b > 900
b = 900
largest = 10000
while (b < 1000):
  a = b
  while (a < 1000):
    c = a * b
    s = str(c)
    d = len(s) / 2
    s1 = s[:d]
    if (len(s) % 2 != 0): d = d + 1
    s2 = s[d:]
    s2 = s2[::-1]
    if (s1 == s2): largest = max(largest, c)
    a += 1
  b += 1
end = time.time()
print 'Problem 4:', largest
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#906609



###############
## PROBLEM 5 ##
###############

start = time.time()
a = 2520 * 11 * 13 * 17 * 19 * 2
end = time.time()
print 'Problem 5:', a
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#232792560



###############
## PROBLEM 6 ##
###############

start = time.time()
a = 100 * 101 * 201 / 6
b = 100 * 100 * 101 * 101 / 4
end = time.time()
print 'Problem 6:', b - a
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#25164150



###############
## PROBLEM 7 ##
###############

start = time.time()
# assumes that n is not even and you are not stupid
# assume n != 1
def prime(n):
  a = n ** 0.5 + 1
  b = 3
  while (b < a):
    if (n % b == 0): return False
    b += 2
  return True

num_prime = 2

# implementation of a 6-wheel
# it is not as efficient as a simple increment
# slightly slower, but slightly cooler
a1 = 1
inc = 2

while (num_prime < 10001):
  a1 = a1 + 2 + inc
  if (prime(a1)):
    num_prime += 1
  inc = (inc + 2) % 4

end = time.time()
print 'Problem 7:', a1
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#104743



###############
## PROBLEM 8 ##
###############

start = time.time()
f = open('ProjectEuler/p8.txt', 'r')
nums = f.read()
l = len(nums)

# assumes the length of the array is >= i + 13
def prod_13(i, nums2):
  j = 0
  p = 1
  while (j < 13):
    p = p * int(nums2[i + j])
    j += 1
  return p

p = prod_13(0, nums)
largest = p
i = 13
while (i < l):
  first = int(nums[i - 13])
  next = int(nums[i])
  if (first == 0):
    p = prod_13(i - 12, nums)
  else:
    p = p / first
    p = p * next
  largest = max(largest, p)
  i += 1
f.close()
end = time.time()
print 'Problem 8:', largest
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#23514624000



###############
## PROBLEM 9 ##
###############

# this code verifies that (0,0,0), (0,5,5), and (5,0,5) are
# the only possible ones-digit triples that might work
# a = 0
# while (a < 10):
#   b = 0
#   while (b < 10):
#     c = int((a ** 2 + b ** 2) ** 0.5)
#     if ((a + b + c) % 10 == 0 and a ** 2 + b ** 2 == c ** 2): print a, b, c
#     b += 1
#   a += 1

start = time.time()
a = 5
b = 10
found = False
while (a < 333):
  b = a + 5
  while (b < (1000 - a) / 2):
    c = 1000 - a - b
    if (a ** 2 + b ** 2 == c ** 2):
      found = True
    if (found): break
    b += 5
  if (found): break
  a += 5
end = time.time()
print 'Problem 9:', a * b * c
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#31875000



################
## PROBLEM 10 ##
################

# you want the arr to contain all primes less than n
def check_div(n, arr):
  a = n ** 0.5
  for e in arr:
    if (e > a): return True
    if (n % e == 0):
      return False
  return True

start = time.time()
s = 2 + 3 + 5 - 1
a1 = 1; a2 = 7; a3 = 11; a4 = 13
a5 = 17; a6 = 19; a7 = 23; a8 = 29

while (a8 < 2000000):
  if (prime(a1)):
    s += a1
  a1 += 30
  if (prime(a2)):
    s += a2
  a2 += 30
  if (prime(a3)):
    s += a3
  a3 += 30
  if (prime(a4)):
    s += a4
  a4 += 30
  if (prime(a5)):
    s += a5
  a5 += 30
  if (prime(a6)):
    s += a6
  a6 += 30
  if (prime(a7)):
    s += a7
  a7 += 30
  if (prime(a8)):
    s += a8
  a8 += 30
if (a1 < 2000000):
  if (prime(a1)):
    s += a1
if (a2 < 2000000):
  if (prime(a2)):
    s += a2
if (a3 < 2000000):
  if (prime(a3)):
    s += a3
if (a4 < 2000000):
  if (prime(a4)):
    s += a4
if (a5 < 2000000):
  if (prime(a5)):
    s += a5
if (a6 < 2000000):
  if (prime(a6)):
    s += a6
if (a7 < 2000000):
  if (prime(a7)):
    s += a7

end = time.time()
print 'Problem 10:', s
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#142913828922



################
## PROBLEM 11 ##
################

start = time.time()
f = open('ProjectEuler/p11.txt', 'r')
i = 0
nums = []
# Read in the data and store in a matrix
while (i < 20):
  s = f.readline()
  j = 0
  row = []
  while (j < 20):
    e = int(s[j * 3: j * 3 + 2])
    row.append(e)
    j += 1
  nums.append(row)
  i += 1

# Handles the horizontal


# Handles the vertical


# Handles left to right diagonal


# Handles right to left diagonal
  


end = time.time()
print 'Problem 11:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time




################
## PROBLEM 12 ##
################

start = time.time()
def triangle(n):
  return n * (n + 1) / 2
def prime_fac(n):
  facs = []
  if (n % 2 == 0):
    facs.append(2)
    n = n / 2
    while (n % 2 == 0):
      n = n / 2
  a = n ** 0.5 + 1
  b = 3
  while (b < a):
    if (n % b == 0):
      facs.append(b)
      n = n / b
      while (n % b == 0):
        n = n / b
    b += 2
  return facs
def num_fac(n):
  arr = prime_fac(n)
  num = 1
  for e in arr:
    times = 0
    while (n % e == 0):
      times += 1
      n = n / e
    num = num * (times + 1)
  if (arr == []):
    return 2
  return num

i = 43 * 44 / 2
j = 44
while (num_fac(i) < 500):
  i += j
  j += 1
end = time.time()
print 'Problem 12:', i
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#76576500



################
## PROBLEM 13 ##
################

start = time.time()
end = time.time()
print 'Problem 13:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time











################
## PROBLEM 14 ##
################

start = time.time()
i = 0
left = []
while (i < 1000000):
  left.append(i)
  i += 1
j = 0
largest = 0
largest_length = 0

def len_collatz(n):
  steps = 0
  while (n != 1):
    if (n % 2 == 0):
      n = n / 2
    else:
      n = 3 * n + 1
    steps += 1
  return steps

def collatz(n, dict):
  if (dict.has_key(n)):
  

while (left != []):
  steps = 0
  next = left[0]
  t = next
  while (next != 1):
    if (next % 2 == 0):
      next = next / 2
    else:
      next = 3 * next + 1
    if (left.count(next) != 0):
      left.remove(next)
    steps += 1
  if (steps > largest_length):
    largest = t
    largest_length = steps
  print 'done', len(left)

end = time.time()
print 'Problem 14:', largest
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time



################
## PROBLEM 15 ##
################

start = time.time()
end = time.time()
print 'Problem 15:', 2 * 13 * 37 * 2 * 33 * 31 * 29 * 5 * 23 * 21
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#137846528820



################
## PROBLEM 16 ##
################

start = time.time()
arr = [2,0]
i = 0
while (i < 333):
  arr.append(0)
  a = len(arr)
  j = 0
  next = 0
  while (j < a):
    pre = arr[j]
    mul = pre * 8 + next
    next = mul / 10
    new = mul % 10
    arr[j] = new
    j += 1
  i += 1
s = 0
for e in arr:
  s += e
end = time.time()
print 'Problem 16:', s
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
#1366





################
## PROBLEM 17 ##
################

start = time.time()
end = time.time()
print 'Problem 17:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time





################
## PROBLEM 18 ##
################

start = time.time()
end = time.time()
print 'Problem 18:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
  
  
  
  
################
## PROBLEM 19 ##
################

start = time.time()
end = time.time()
print 'Problem 19:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
  
  
  
  
  
  
  
################
## PROBLEM 20 ##
################

start = time.time()
end = time.time()
print 'Problem 20:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
  
  
  
  
  
  
  
################
## PROBLEM 21 ##
################

start = time.time()
end = time.time()
print 'Problem 21:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time
  
  
  
  
  
  
  
################
## PROBLEM 22 ##
################

start = time.time()
end = time.time()
print 'Problem 22:'
run_time = int((end - start) * 100) / 100.0
if (run_time != 0):
  print 'Time:', run_time


