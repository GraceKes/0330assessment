#Q1
def nthSandwich(n):
    count = 0
    num = 10
    while True:
        num += 1
        if num % 10 == 0:
            continue
        first_digit = num
        while first_digit >= 10:
            first_digit //= 10
        last_digit = num % 10
        if first_digit != last_digit:
            continue
        has_middle_digit = False
        a = num // 10
        while a >= 10:
            if a % 10 == first_digit:
                has_middle_digit = True
                break
            a //= 10
        if not has_middle_digit:
            if count == n:
                return num
            count += 1
print(nthSandwich(1000))

#Q2
# ValueError - print(int("str"))
# ZeroDivisionError - print(12/0)
# NameError - print(I)

#Q3
"""
int
float
Bool
type
str
list
tup
dict
dict
6
"abc""abc""abc"
5
"abcdef"
generate typeError
"""

#Q4
"""
/ simply divides the number, but // divides and rounds the number
until the first digit
"""

#Q5
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# def testIsPrime():
#     assert(isPrime(1)==False)
#     assert (isPrime(0) == False)
#     assert (isPrime(2) == True)
#     assert (isPrime(5) == True)
#     assert (isPrime(3) == True)
# testIsPrime()
"""
Since the isPrime function is excluding the incidents where an even 
number 2 is an prime number and 1 cannot be a prime number, 
we should if conditions to make a exclusion for those numbers.
"""


#Q6
def isPalindrome(n):
    num= [str(i) for i in str(n)]
    for i in range(len(num)):
        if num[i]==num[len(num)-i-1]:
            continue
        else:
            return False
    return True
print(isPalindrome(12321))

#Q7
"""
Something mutable is when we can replace the value and is changeable, 
but something immutable is when we cna change but not replace a
value inside. 
"""

