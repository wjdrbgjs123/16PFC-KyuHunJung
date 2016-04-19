#-*-coding: cp949
from sys import argv

script, user_name = argv
prompt ='>'

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = raw_input(prompt)

print ("Where do you live %s" % user_name)
lives = raw_input(prompt)

print(" What kind of computer do you have?")
computer = raw_input(prompt)

print ("""
Alright, so you said %s about liking me.
you live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer))
# %r 을 %s 로 바꾸면 출력할때 한글이 나온다. %r로 하면 이상한 문자 나옴 13과는 다르게 raw_input이 추가됨
