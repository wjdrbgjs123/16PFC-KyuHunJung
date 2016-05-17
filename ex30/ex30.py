# -*-coding:cp949
# coding: utf-8
people = 30
cars = 40
trucks = 15

if cars >people:
    print "We should take the cars."
elif cars < people:
    print "We should not takd the cars."
else:
    print "We can't decide."
# else는 전체 집합에서 if 의 집합과 elif의 집합을 제외한 나머지를 의미 한다

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."