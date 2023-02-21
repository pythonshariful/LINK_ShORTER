import os
import sys
import time
import pyshorteners


username = "python"
password = "1234"

givenUsername = input("\033[0;34mEnter your username: ")
if givenUsername == username:
  print("\033[0;32mCorrect Username")
  givenPassword = input("\033[0;34mEnter your password:")
  if givenPassword == password:
    print("\033[0;32mCorrect password")
    
    time.sleep(1)
    os.system('clear')
  else:
    print("\033[0;31mWrong password")
    foo =input()
    sys.exit()
    
else:
  print("\033[0;31mWrong User")
  foo = input()
  sys.exit()
os.system('figlet LOG IN SUCCESS')
time.sleep(0.5)
os.system('clear')

def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)

logo  = '''

\033[1;33m$$\       $$$$$$\ $$\   $$\ $$\   $$\        $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
$$ |      \_$$  _|$$$\  $$ |$$ | $$  |      $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\\__$$  __|$$  _____|$$  __$$\ 
$$ |        $$ |  $$$$\ $$ |$$ |$$  /       $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |  $$ |   $$ |      $$ |  $$ |
$$ |        $$ |  $$ $$\$$ |$$$$$  /        \$$$$$$\  $$$$$$$$ |$$ |  $$ |$$$$$$$  |  $$ |   $$$$$\    $$$$$$$  |
$$ |        $$ |  $$ \$$$$ |$$  $$<          \____$$\ $$  __$$ |$$ |  $$ |$$  __$$<   $$ |   $$  __|   $$  __$$< 
$$ |        $$ |  $$ |\$$$ |$$ |\$$\        $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |   $$ |      $$ |  $$ |
$$$$$$$$\ $$$$$$\ $$ | \$$ |$$ | \$$\       \$$$$$$  |$$ |  $$ | $$$$$$  |$$ |  $$ |  $$ |   $$$$$$$$\ $$ |  $$ |
\________|\______|\__|  \__|\__|  \__|       \______/ \__|  \__| \______/ \__|  \__|  \__|   \________|\__|  \__|
                                                                                                                 
                                                                                                                 
                                                                                                                 

'''
animated(logo)



link = input("\033[0;34mEnter your link to short: ")
s = pyshorteners.Shortener()
x = s.tinyurl.short(link)
print(f"Your short link is : {x}")
