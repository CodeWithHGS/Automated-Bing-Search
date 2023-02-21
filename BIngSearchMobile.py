import keyboard
import random
import string
import time
from AppOpener import open
n=int(input("Enter how many times to search: "))
open('Microsoft Edge')
time.sleep(1)
keyboard.press_and_release('F12')
time.sleep(1)
for i in range(0,n):
    keyboard.press_and_release('Ctrl + e')
    random_number=''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=5))
    keyboard.write(str(random_number))
    keyboard.press_and_release('Enter')
    time.sleep(1)
    print((i+1),' Itration Done') 

