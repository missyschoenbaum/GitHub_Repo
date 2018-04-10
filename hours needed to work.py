from how_much_do_I_get_paid import *

def backCalculate(numberWeeks, moneyNeeded):
    hoursPerWeek = 30 + float(2*(moneyNeeded - 10 * numberWeeks))/float(payRate * numberWeeks)
    if (hoursPerWeek <30):
        hoursPerWeek = 30
    print ("Over %s weeks, to generate $%s of spending money,\nyou will need to work %s hours per week." \
           %(numberWeeks, moneyNeeded, round(hoursPerWeek,2)))
    print ("\n\n---------------------------------------")

def repeat():
    global startOver
    startOver = True

    while startOver == True:
        backCalculate(input ("How many weeks do you want to work for this money? "), \
                      input ("How much money is needed? "))
        a = raw_input("Press ENTER to exit or type a key to restart. ")
        if (a == ''):
            startOver = False
        print ("\n\n---------------------------------------")
    else:
        ()

if (__name__ == '__main__'):
    repeat()
                  
