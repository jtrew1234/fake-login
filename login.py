from time import sleep

def reset():
    print("Please input new password")
    password2 = input()
    print("Please input again")
    password2 = input()
    print ("Password has been set. Computer will reboot")
    
sleep(2)
print("Hello, welcome to OS")
print("What is your username")
name =input()
print("Please wait while we log your username")
sleep(10)
print ("Please input your password")
password =input()
if password==("EpicPassword123"):
    print ("Welcome back",name)
    quit()
else:
    print ("Password reset? Y or N")
answer =input()
if answer == ("Y"):
    reset()
else:
    print("Please try again")
