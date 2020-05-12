from tkinter import *

main = Tk()
main.title("GUIpalc")

numbers = ""

def number(num):
    num = str(num)
    global numbers
    numbers = numbers + num

def op(calc):
    pass