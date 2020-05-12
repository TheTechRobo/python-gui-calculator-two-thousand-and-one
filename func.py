import logging
num = ""
numm = ""
def getNum():
    num1 = numbers
    new = Toplevel()
    new.title("Press the second number: ")
    def n(num):
        global numm
        num = str(num)
        numm = numm + num
    w = Button(main, text=1, command=n(1))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=2, command=n(2))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=3, command=n(3))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=4, command=n(4)).pack()
    w = Button(main, text=5, command=n(5))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=6, command=n(6))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=7, command=n(7)).pack()
    w = Button(main, text=8, command=n(8))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=9, command=n(9))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text=0, command=n(0))
    w.pack(padx=5, pady=10, side=LEFT)
    w = Button(main, text="=", command=(return numm)).pack()
def h():
    print(_('''
     Current list of commands: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (power), root (root), equals (=), logarithm (log), memory (mem), interest calculator (interest), fibonacci sequence (fib), percentage (percent), and convert number systems (base). Type e to e.
     Bugs? Head on over to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     '''))
def multi(): #multiplication
    n1, n2 = getNum()
    cprint.info(_("\nThat equals...\n%s" % (n1 * n2)))
    logging.info(("User multiplied ", n1, " by ", n2, " and got result ", (n1 * n2)))
    return (n1 * n2)
def div(): #division
    n1, n2 = getNum()
    try:
        cprint.info(_("\nThat equals...\n%s" % (n1 / n2)))
        return (n1 / n2)
    except ZeroDivisionError:
        cprint.err(_("Do not divide by zero!"))
        logging.error("User attempted to divide by zero.")
        raise ValueError
    except:
        cprint.err(_("There was an unknown issue dividing your Numbers..."))
    logging.info(("User divvied ", n1, " by ", n2, ", getting a result of ", (n1 / n2)))
def sub(): #subtraction
    n1, n2 = getNum()
    cprint.info(_("\nThat equals...\n%s" % (n1 - n2)))
    logging.info(("User subtracted ", n1, " by ", n2, " and got result ", (n1 - n2)))
def add(): #addition
    n1, n2 = getNum()
    print(_("\nThat equals..."))
    print(n1 + n2)
    logging.info(("User added ", n1, " to ", n2, " and got result ", (n1 + n2)))
def mod(): #modulo
    try:
        bigger = int(input(_("\nType the first number (greater): ")))
        smaller = int(input(_("Type the second number (smaller): ")))
    except (TypeError, ValueError):
        print(_("\nError!"))
        print(_("Invalid input (code 1)\n"))
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 1."))
    if(abs(bigger)<abs(smaller)):
        print(_("\nError!"))
        print(_("The second number entered is greater than the first number (code 2)\n"))
        logging.error(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 2."))
    else:
        print(_("\nThat equals..."))
        print(bigger-smaller*int(bigger/smaller))
        logging.info(("User attempted to modulo numbers ", bigger, " and ", smaller, ", and got result ", (bigger-smaller*int(bigger/smaller))))
        print()
def base():
    base = int(input('''What base would you like to use?
    Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
    Type 2, 8, 10, or 16: '''))
    if base == 2:
        result = bin(int(input(_("Type the original number: ")))) #bin() the number
        printThis = "=" +str(result)
        logging.info(("User binaried number ", result, ", getting a result of ", printThis))
        print(printThis)
    elif base == 8:
            result = oct(int(input(_("Type the original number: ")))) #oct() the number
            printThis = "=" +str(result)
            logging.info(("User oct'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 10:
        goodanswer = False
        while goodanswer is False:
            whichType = input(_("Which type is the Number (ord, binary, octo, or hex): "))
            if whichType == "ord":
                goodanswer = True
                result = int(ord(input(_("Type the original number: ")))) #int() the number
            elif whichType == "binary":
                goodanswer = True
                result = int(bin(input(_("Type the original number: ")))) #int() the number
            elif whichType == "octo":
                goodanswer = True
                result = int(oct(input(_("Type the original number: ")))) #int() the number
            elif whichType == "hex":
                goodanswer = True
                result = int(hex(input(_("Type the original number: ")))) #int() the number
            else:
                print(_("That was an invalid answer. Try again."))
            printThis = "=" +str(result)
            logging.info(("User int'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 16:
        result = hex(int(input(_("Type the original number: ")))) #ask for original number
        printThis = "=" +str(result)
        logging.info(("User hexed number ", result, ", getting a result of ", printThis))
        print(printThis)
def uc():
    import runpy
    logging.warning(("User ran `volume.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='volInteractive.py')
def area():
    import runpy
    logging.warning(("User ran `area.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='areaInteractive.py')
def log(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    import math
    while True:
        base = input(_("What base would you like to use? \nCurrentlysupported: 10 (base 10), e (natural)"))
        if base == "10":
            print(_("Using base 10"))
            number = int(input(_("What is the number? ")))
            print(math.log10(number))
            logging.info(("User used base 10 logarithm with number", number, ", getting a result of ", math.log10(number)))
            break
        elif base.lower() == "e":
            print(_("Using natural logarithm"))
            number = int(input(_("What is the number? ")))
            print(math.log(number))
            logging.info(("User used natural logarithm with number ", number, ", getting a result of ", math.log(number)))
            break
        else:
            print(_("The logarithm you typed is not available."))
            print(_("Try again."))
            logging.info(("User attempted to use a logarithm that is unavailable."))
def remember():
    print(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info(("Saved number ", toRemember, " to memory slot ", slot))
def readMyMemory():
    print(_("This is the remember function.\nIt will read a number that was previously stored in a file."))
    try:
        slot = str(int(input(_("What slot number did you use? "))))
        memory = open(slot, "r")
        print(_("Number: ", memory.read()))
        logging.info(("Retrieved number ", memory.read(), " from memory."))
    except:
        logging.info("There was an error retrieving the file from memory.")
        print(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?"))
def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0 <= x:
        return x**(1./3.)
    return -(-x)**(1./3.)
def cu():
    print(cubeInternal(int(input(_("Number to be rooted? ")))))
def fib():
    import runpy
    runpy.run_path(path_name="fibonacci.py")
    logging.info("user ran fibonacci function")
def percentage(percent, whole):
    if whole == 0:
        logging.error("User typed 0 as whole.")
        return (_("Please do not type in a zero as the whole."))
    return (percent * whole) / 100.0
def whatIsPercent():
    origin = int(input(_("what is the ORIGINAL NUMBER? ")))
    percent = int(input(_("What is the PERCENTAGE? ")))
    logging.info(("Got percentage RN origin ", origin, " and ", percent))
    print(percentage(percent, origin))
def getPercentage(part, whole):
    if whole == 0:
        logging.error("user typed whole zero")
        return (_("Please do not type in a zero as the whole."))
    return 100 * float(part)/float(whole)
def getPercentageRN():
    origin = int(input(_("What is the number that would be 100%? ")))
    part = int(input(_("What is the number that you want to convert to percentage (e.g. this number out of the number that would be 100%)? ")))
    logging.info(("Got percentage RN origin ", origin, " and ", part))
    print(getPercentage(part, origin))
def calculateInterest():
    while True: 
        origin = int(input(_("What is the original number? ")))
        rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
        print()
        howMany = int(input(_('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
        inRealNumbers = percentage(whole=origin, percent=rate)
        number = origin + (inRealNumbers * howMany)
        logging.info(("INTERESTCALC: origin: ", origin, " rate: ", rate, " how many: ", howMany, " answer: ", number))
        print(_(("The answer is ", number)))
        doItAgain = input("Would you like to do it again (Y/n)? ")
        doItAgain = doItAgain.lower()
        if doItAgain == "y":
            pass
        else:
            print(_("OK. Going back..."))
            break
def taxCalc():
    whatPlace = int(input(_("""1 - Ontario Sales Tax
2 - Quebec Sales Tax
3 - Yukon, Northwest Territories, Nunavut, and Alberta Sales Tax
4 - BC / Manitoba Sales Tax
5 - Custom Tax
Choose one: """)))
    if whatPlace == 1:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 13.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Ontarian Sales Tax 13 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice)))
        print(_("After tax, the price is: \n%s" % newPrice))
        return newPrice
    elif whatPlace == 2:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 14.975
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Quebec Sales Tax 14.975 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice)))
        print(_("After tax, the price is: \n%s" % newPrice))
        return newPrice
    elif whatPlace == 3:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 5.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Alberta Sales Tax 5 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice)))
        print(_("After tax, the price is: \n%s" % newPrice))
        return newPrice
    elif whatPlace == 4:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 12.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info(("User used Manitoba Sales Tax 12 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice)))
        print(_("After tax, the price is: \n%s" % newPrice))
        return newPrice
    elif whatPlace == 5:
        originPrice = float(input(_("OK, enter the original price: ")))
        percent = float(input(_("Now enter the tax percentage without the percent sign: ")))
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        print(_("After tax, the price is: \n%s" % newPrice))
        return newPrice
    else:
        print(_("You did not type answer. Abort."))