import tkinter as tk

bro = input('do u need C to f or f to c,Type c or f ONLY: ')

lol = int(input('Input Value: '))

def cel():
    print('c to f selected')
    print(lol * 9/5 + 32,'fahrenheit')

def far():
    print('f to c selected')
    #print(lol - 32 * 5 / 9, 'celsius')
    lop = lol - 32
    kop = lop * 5
    jop = kop / 9
    print(jop,'celsuis')

if bro =='c':
    cel()
if bro =='f':
    far()

