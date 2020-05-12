from tkinter import *

main = Tk()
main.title("GUIpalc")

numbers = ""

def number(num):
    num = str(num)
    global numbers
    numbers = numbers + num

def op(calc):
    #TAX
    elif calc == "tax":
        taxCalc()
    #MULTIPLICATION
    elif calc == "x":
        multi()
    #SQUARE
    elif "sq" == calc:
        n = int(input(_("Number? ")))
        cprint.info(n * n)
        logging.info(("User squared number ", n, " got result ", (n * n)))
    #DIVISION
    elif "/" == calc:
        div()
    #SUBTRACTION
    elif "-" == calc:
        sub()
   elif "sub" == calc:
        sub()
   elif "min" == calc:
        sub()
    #ADDITION
   elif "+" == calc:
        add()
   elif "add" == calc:
        add()
    #MODULO
   elif "%" == calc:
        mod()
   elif "mod" == calc:
        mod()
#AREA
   elif "ar" == calc:
        area()
   elif "#" == calc:
        area()
   elif "area" == calc:
        area()
#VOLUME
   elif "vol" == calc:
        uc()
#CUBE
   elif "{}" == calc:
        cubedNumber = int(input("\nType the number to be cubed: "))
        print()
        cprint.info(cubedNumber ** 3) #Manually cube number
        logging.info(("User cubed number ", cubedNumber, " got result ", (cubedNumber ** 3)))
        print()
#EXIT
   elif "quit" == calc:
        logging.info("User exited using `quit' command")
        e()
#EXPONENTS
   elif "power" == calc:
        origin = int(input("Original number?"))
        ex = int(input("Exponent? "))
        cprint.info(origin ** ex)
        logging.info(("User exponented number ", origin, " with ", ex, "getting ", (origin ** ex)))
    #ROOTS
   elif "root" == calc:
        root = input("Square root or cube root?(square/cube)")
        root = root.lower()
        if "square" == root:
            num = input("Number to be rooted?")
            cprint.info(_("That equals.....\n", num ** 0.5))
            logging.info(("user sqrooted number ", (num**0.5)))
        elif "cube" == root:
            cu()
        else:
            print(_("Currently I don't support the root you chose. Hopefully this will change :)"))
#EASTER EGG!
   elif calc == "=":
        print()
        number = int(input("Type in a number: "))
        if number == 42:
            cprint.info(_("=42 -- the answer to life, the universe, and everything"))
            logging.info("User got the easter egg")
        else:
            cprint.info("=" +number)
            logging.info("User used the `=' feature for number ", number)
#NUMBER SYSTEMS
   elif calc == "base":
        base()
#ORD
   elif calc == "ord":
       logging.info(("User ord'ed to get result ", result))
       result = str(ord(int(input(_("Type in the number to ord: ")))))
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
            cprint.err(_("You did not type an answer.\nAbort."))
            logging.error("User didn't type an answer in MEM function")
#FIBONACCI
   elif calc == "fib":
        cprint.ok(_("Starting fibonacci sequence. Please wait."))
        fib()
#PERCENTAGE
   elif calc == "percent": #SOURCE: https://stackoverflow.com/a/5998010/9654083
        whichOne = int(input(_('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage.
Type: ''')))
        if whichOne == 1:
            whatIsPercent()
        elif whichOne == 2:
            getPercentageRN()
        else:
            cprint.err(_("You didn't type a valid answer. Abort."))
#INTEREST
   elif calc == "interest":
        calculateInterest()