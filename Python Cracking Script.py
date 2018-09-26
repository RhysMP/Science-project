import itertools
import string
import time
import pyautogui
import random

then = time.time() 

def guess_password(real):
    chars = string.ascii_letters + string.digits + string.punctuation 
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} attempt(s).'.format(guess, attempts)
            print(guess, attempts)

print(guess_password('PASSWORD HERE'))
now = time.time() 

print("Taking: ", now-then, " seconds")

print ("Done")

pyautogui.PAUSE = 10

pyautogui.keyDown('2')

pyautogui.keyUp('2')



