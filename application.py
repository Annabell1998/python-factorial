"""help the user to know a factorial of one number"""
import os, sys
def welcome():
    """the welcome fuction"""
    clear()
    print "welcome to factorial number\n"
    print "this program help you to calculate a factorial of one number"
def factorial(xname, number):
    """calculate the factorial number"""
    if number > 0:
        xname = factorial(xname, number-1)
        xname = xname * number
    else:
        xname = 1
    return xname
def option():
    """ask the user if want enter another number"""
    answer = raw_input("do you want to calculate  the factorial for other number? Y/N: ")
    answer.lower()
    if answer == "y":
        clear()
        print "let's go"
        numbers()
    elif answer == "n":
        clear()
        print "***Good bye , see you soon n.n/"
        out()
    else:
        print "Sorry but you need enter Y/N"
        option()
def clear():
    """clean the screen"""
    os.system("reset")
def out():
    """go out"""
    sys.exit()
def numbers():
    """ ask the number"""
    try:
        number = int(raw_input("Enter a number between 1-995: "))
    except ValueError:
        print "Sorry, only numbers please"
        numbers()
    if number > 995:
        clear()
        print "the number is to high, try again"
        numbers()
    else:
        total = factorial(1, number)
        print "the factorial of %s is %s " %(number, total)
        option()
welcome()
numbers()
