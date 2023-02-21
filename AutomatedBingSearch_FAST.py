import webbrowser
import random
import string
n=int(input("Enter how many times to search: "))

chrome_path = 'C:/Program Files (x86)/\Microsoft/Edge/Application/msedge.exe %s'

for i in range(0,n):
    x=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    url = "https://www.bing.com.tr/search?q={}".format(x)
    webbrowser.get(chrome_path).open_new_tab(url)