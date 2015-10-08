# Aqui escribe tu codigo
import os, sys
def welcome():
	clear()
	print "welcome to factorial number\n"
	print "this program help you to calculate a factorial of one number"
def factorial(x,number):
	if(number>0):
		x=factorial(x,number-1)
		x=x*number
	else:
		x=1
	return x
def option():
	option = raw_input("do you want to calculate  the factorial for other number? Y/N: ")
	option.lower()
	if option == "y":
		clear()
		print "let's go"
		numbers()
	elif option == "n":
		clear()
		print "***Good bye , see you soon n.n/"
		out()
	else:
		print "Sorry but you need enter Y/N"
		option()
def clear():
	os.system("reset")
def out():
	sys.exit()
def numbers():
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
		print "the factorial of %s is %s " %(number,total)
		option()
welcome()
numbers()
