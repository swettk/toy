#!/usr/bin/env python

def split_sentence(y):
  collect = [] 
  for z in y.split(" "):
     collect.append(pig_word(z))
  return (" ").join(collect)

def pig_word(x):
    if x[0].isupper():
      return x[1].upper() + x[2:] + x[:1].lower() + "ay"
    else: 
      return x[1:] + x[:1] + "ay"

#def 
#def is_vowel

def assert_same(a,b):
    if a != b:
        print "|%s != %s|" % (a,b)
        raise Exception("boom!")
    print "|%s %s|" % (a,b)

if __name__ == "__main__":
    #print split_sentence("hello")
    assert_same(split_sentence("hello"),"ellohay")
    #"hello world"
    assert_same(split_sentence("hello world"),"ellohay orldway")
    ##"Hello World"
    assert_same(split_sentence("Hello World"),"Ellohay Orldway")

#"Hello, world!"
#"eat apples"
#"quick brown fox"
