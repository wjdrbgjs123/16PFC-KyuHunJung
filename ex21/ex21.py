# -*-coding:cp949
#-*-coding:utf-8

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# 함수의 일반적인 형태, 함수의 이름은 (add)
# return은 반환을 의미한다

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# 여기부터가 함수를 실제로 실행하고 호출하는 부분이다.
# 앞에서는 계속 함수를 설정해주느 역할을 하고있었다
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 제일 안에있는 divide 가 먼저 실행된다.그리고 바깥으로 실행된다.

print "That becomes: ", what, "Can you do it by hand?"
