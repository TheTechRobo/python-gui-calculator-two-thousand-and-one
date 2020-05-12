
import logging
from tkinter import *
num = ""
numm = ""
numbers = ""
def number(num):
    num = str(num)
    global numbers
    numbers = numbers + num
def getNum():
    num1 = numbers
    new = Toplevel()
    new.title("Enter the second number: ")
    e = Entry(main)
    e.pack()
    num2 = e.get()
    return num1, num2
def h():
    print('''
     Current list of commands: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (power), root (root), equals (=), logarithm (log), memory (mem), interest calculator (interest), fibonacci sequence (fib), percentage (percent), and convert number systems (base). Type e to e.
     Bugs? Head on over to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     ''')
def multi(): #multiplication
    n1, n2 = getNum()
    cprint.info("\nThat equals...\n%s" % (n1 * n2))
    logging.info(("User multiplied ", n1, " by ", n2, " and got result ", (n1 * n2))
    return n1 * n2
def div(): #division
    n1, n2 = getNum()
    try:
        cprint.info("\nThat equals...\n%s" % (n1 / n2))
        return (n1 / n2)
    except ZeroDivisionError:
        cprint.err("Do not divide by zero!")
        logging.error("User attempted to divide by zero.")
        raise ValueError
    except:
        cprint.err("There was an unknown issue dividing your Numbers...")
    logging.info(("User divvied ", n1, " by ", n2, ", getting a result of ", (n1 / n2))
def sub(): #subtraction
    n1, n2 = getNum()
    cprint.info("\nThat equals...\n%s" % (n1 - n2))
    logging.info(("User subtracted ", n1, " by ", n2, " and got result ", (n1 - n2))
def add(): #addition
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 + n2)
    logging.info(("User added ", n1, " to ", n2, " and got result ", (n1 + n2))
def mod(): #modulo
    try:
        bigger = int(input("\nType the first number (greater): "))
        smaller = int(input("Type the second number (smaller): "))
    except (TypeError, ValueError):
        print("\nError!")
        print("Invalid input (code 1)\n")
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 1.")
    if(abs(bigger)<abs(smaller):
        print("\nError!")
        print("The second number entered is greater than the first number (code 2)\n")
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 2.")
    else:
        print("\nThat equals...")
        print(bigger-smaller*int(bigger/smaller)
        logging.info(("User attempted to modulo numbers ", bigger, " and ", smaller, ", and got result ", (bigger-smaller*int(bigger/smaller))
        print()
def base():
    base = int(input('''What base would you like to use?
    Available: 2 (binary) 8 (octo) 10 (decimal (normal) 16 (hex)
    Type 2, 8, 10, or 16: ''')
    if base == 2:
        result = bin(int(input("Type the original number: ")) #bin() the number
        printThis = "=" +str(result)
        logging.info(("User binaried number ", result, ", getting a result of ", printThis)
        print(printThis)
    elif base == 8:
            result = oct(int(input("Type the original number: ")) #oct() the number
            printThis = "=" +str(result)
            logging.info(("User oct'ed number ", result, ", getting a result of ", printThis)
            print(printThis)
    elif base == 10:
        goodanswer = False
        while goodanswer is False:
            whichType = input("Which type is the Number (ord, binary, octo, or hex): ")
            if whichType == "ord":
                goodanswer = True
                result = int(ord(input("Type the original number: ")) #int() the number
            elif whichType == "binary":
                goodanswer = True
                result = int(bin(input("Type the original number: ")) #int() the number
            elif whichType == "octo":
                goodanswer = True
                result = int(oct(input("Type the original number: ")) #int() the number
            elif whichType == "hex":
                goodanswer = True
                result = int(hex(input("Type the original number: ")) #int() the number
            else:
                print("That was an invalid answer. Try again.")
            printThis = "=" +str(result)
            logging.info(("User int'ed number ", result, ", getting a result of ", printThis)
            print(printThis)
    elif base == 16:
        result = hex(int(input("Type the original number: ")) #ask for original number
        printThis = "=" +str(result)
        logging.info(("User hexed number ", result, ", getting a result of ", printThis)
        print(printThis)
def uc():
    import runpy
    logging.warning(("User ran `volume.py'. Log is currently unavailable for area and volume.")
    runpy.run_path(path_name='volInteractive.py')
def area():
    import runpy
    logging.warning(("User ran `area.py'. Log is currently unavailable for area and volume.")
    runpy.run_path(path_name='areaInteractive.py')
def log(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    import math
    while True:
        base = input("What base would you like to use? \nCurrentlysupported: 10 (base 10), e (natural)")
        if base == "10":
            print("Using base 10")
            number = int(input("What is the number? "))
            print(math.log10(number)
            logging.info(("User used base 10 logarithm with number", number, ", getting a result of ", math.log10(number))
            break
        elif base.lower() == "e":
            print("Using natural logarithm")
            number = int(input("What is the number? "))
            print(math.log(number)
            logging.info(("User used natural logarithm with number ", number, ", getting a result of ", math.log(number))
            break
        else:
            print("The logarithm you typed is not available.")
            print("Try again.")
            logging.info(("User attempted to use a logarithm that is unavailable.")
def remember():
    print("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor.")
    toRemember = float(input("\nPlease enter the number to be saved: "))
    slot = str(int(input("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info(("Saved number ", toRemember, " to memory slot ", slot)
def readMyMemory():
    print("This is the remember function.\nIt will read a number that was previously stored in a file.")
    try:
        slot = str(int(input("What slot number did you use? "))
        memory = open(slot, "r")
        print("Number: ", memory.read())
        logging.info(("Retrieved number ", memory.read(), " from memory.")
    except:
        logging.info("There was an error retrieving the file from memory.")
        print("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?")
def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0 <= x:
        return x**(1./3.)
    return -(-x)**(1./3.)
def cu():
    print(cubeInternal(int(input("Number to be rooted? ")))
def fib():
    import runpy
    runpy.run_path(path_name="fibonacci.py")
    logging.info("user ran fibonacci function")
def percentage(percent, whole):
    if whole == 0:
        logging.error("User typed 0 as whole.")
        return ("Please do not type in a zero as the whole.")
    return (percent * whole) / 100.0
def whatIsPercent():
    origin = int(input("what is the ORIGINAL NUMBER? "))
    percent = int(input("What is the PERCENTAGE? "))
    logging.info(("Got percentage RN origin ", origin, " and ", percent)
    print(percentage(percent, origin)
def getPercentage(part, whole):
    if whole == 0:
        logging.error("user typed whole zero")
        return ("Please do not type in a zero as the whole.")
    return 100 * float(part)/float(whole)
def getPercentageRN():
    origin = int(input("What is the number that would be 100%? "))
    part = int(input("What is the number that you want to convert to percentage (e.g. this number out of the number that would be 100%)? "))
    logging.info(("Got percentage RN origin ", origin, " and ", part)
    print(getPercentage(part, origin)
def calculateInterest():
    while True: 
        origin = int(input("What is the original number? "))
        rate = float(input("What is the rate of interest in percentage (without the percent sign)? "))
        print()
        howMany = int(input('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: '''))
        inRealNumbers = percentage(whole=origin, percent=rate)
        number = origin + (inRealNumbers * howMany)
        logging.info(("INTERESTCALC: origin: ", origin, " rate: ", rate, " how many: ", howMany, " answer: ", number)
        print(("The answer is ", number))
        doItAgain = input("Would you like to do it again (Y/n)? ")
        doItAgain = doItAgain.lower()
        if doItAgain == "y":
            pass
        else:
            print("OK. Going back...")
            break
def taxCalc():
    whatPlace = int(input("""1 - Ontario Sales Tax
2 - Quebec Sales Tax
3 - Yukon, Northwest Territories, Nunavut, and Alberta Sales Tax
4 - BC / Manitoba Sales Tax
5 - Custom Tax
Choose one: """))
    if whatPlace == 1:
        originPrice = int(input("What is the original price (before tax)? "))
        percent = 13.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Ontarian Sales Tax 13 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        print("After tax, the price is: \n%s" % newPrice)
        return newPrice
    elif whatPlace == 2:
        originPrice = int(input("What is the original price (before tax)? "))
        percent = 14.975
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Quebec Sales Tax 14.975 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        print("After tax, the price is: \n%s" % newPrice)
        return newPrice
    elif whatPlace == 3:
        originPrice = int(input("What is the original price (before tax)? "))
        percent = 5.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Alberta Sales Tax 5 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        print("After tax, the price is: \n%s" % newPrice)
        return newPrice
    elif whatPlace == 4:
        originPrice = int(input("What is the original price (before tax)? "))
        percent = 12.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Manitoba Sales Tax 12 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        print("After tax, the price is: \n%s" % newPrice)
        return newPrice
    elif whatPlace == 5:
        originPrice = float(input("OK, enter the original price: "))
        percent = float(input("Now enter the tax percentage without the percent sign: "))
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        print("After tax, the price is: \n%s" % newPrice)
        return newPrice
    else:
        print("You did not type answer. Abort.")
from tkinter import *
from tkinter import messagebox
from func import *

main = Tk()
main.title("GUIpalc")

numbers = ""

def op(calc):
   Label(main, text="Please Enter The Second Number: ")
   w = Entry(main)
   w.pack()
   num1 = numbers
   num2 = w.get()
#TAX
   if calc == "tax":
        taxCalc()
#MULTIPLICATION
   elif calc == "x":
        multi()
#SQUARE
   elif "sq" == calc:
        n = int(input("Number? "))
        cprint.info(n * n)
        logging.info(("User squared number ", n, " got result ", (n * n))
#DIVISION
   elif "/" == calc:
        div()
#SUBTRACTION
   elif "-" == calc:
        sub()
#ADDITION
   elif "+" == calc:
        add()
#MODULO
   elif "%" == calc:
        mod()
#AREA
   elif "area" == calc:
        area()
#VOLUME
   elif "vol" == calc:
        uc()
#CUBE
   elif "{}" == calc:
        cubedNumber = int(input("\nType the number to be cubed: ")
        print()
        cprint.info(cubedNumber ** 3) #Manually cube number
        logging.info(("User cubed number ", cubedNumber, " got result ", (cubedNumber ** 3))
        print()
#EXIT
   elif "quit" == calc:
        logging.info("User exited using `quit' command")
        e()
#EXPONENTS
   elif "power" == calc:
        origin = int(input("Original number?")
        ex = int(input("Exponent? ")
        cprint.info(origin ** ex)
        logging.info(("User exponented number ", origin, " with ", ex, "getting ", (origin ** ex))
    #ROOTS
   elif "root" == calc:
        root = input("Square root or cube root?(square/cube)")
        root = root.lower()
        if "square" == root:
            num = input("Number to be rooted?")
            cprint.info("That equals.....\n", num ** 0.5)
            logging.info(("user sqrooted number ", (num**0.5))
        elif "cube" == root:
            cu()
        else:
            print("Currently I don't support the root you chose. Hopefully this will change :)")
#EASTER EGG!
   elif calc == "=":
        print()
        number = int(input("Type in a number: ")
        if number == 42:
            cprint.info("=42 -- the answer to life, the universe, and everything")
            logging.info("User got the easter egg")
        else:
            cprint.info("=" +number)
            logging.info("User used the `=' feature for number ", number)
#NUMBER SYSTEMS
   elif calc == "base":
        base()
#ORD
   elif calc == "ord":
       logging.info(("User ord'ed to get result ", result)
       result = str(ord(int(input("Type in the number to ord: ")))
       cprint.info("=", result)
#LOGARITHM
   elif calc == "log":
       log()
#MEMORY
   elif calc == "mem":
        memOrRecall = input("Would you like to set the memory or recall? (set / recall)\nType: ")
        if memOrRecall.lower() in "set":
            remember()
        elif memOrRecall.lower() in "recall":
            readMyMemory()
        else:
            cprint.err("You did not type an answer.\nAbort.")
            logging.error("User didn't type an answer in MEM function")
#FIBONACCI
   elif calc == "fib":
        cprint.ok("Starting fibonacci sequence. Please wait.")
        fib()
#PERCENTAGE
   elif calc == "percent": #SOURCE: https://stackoverflow.com/a/5998010/9654083
        whichOne = int(input('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage.
Type: '''))
        if whichOne == 1:
            whatIsPercent()
        elif whichOne == 2:
            getPercentageRN()
        else:
            cprint.err("You didn't type a valid answer. Abort.")
#INTEREST
   elif calc == "interest":
        calculateInterest()


#SOURCE: https://www.python-course.eu/tkinter_layout_management.php
w = Button(main, text=1, command=number(1)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=2, command=number(2)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=3, command=number(3)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=4, command=number(4).pack()
w = Button(main, text=5, command=number(5)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=6, command=number(6)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=7, command=number(7).pack()
w = Button(main, text=8, command=number(8)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=9, command=number(9)
w.pack(padx=5, pady=10, side=LEFT)
w = Button(main, text=0, command=number(0)
w.pack(padx=5, pady=10, side=LEFT)

Label(main, text="OPERATORS").pack()
w = Button(main, text="+", command=op("+")


main.mainloop()