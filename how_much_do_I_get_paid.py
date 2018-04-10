<<<<<<< HEAD
#plz... I have a wife... kids... don't make them go hungry...#
=======
#Listen to my will, filthy computer!#
>>>>>>> 27144e1d0f34afa8473a3416056767bac58eaab4

#### PARAMETERS ####

defaultSpendingMoney = 10. # this is the default amount of spending money per week
payRate = 12.6819 # an estimate of how much $ I make per hour, after taxes


def fn():
    miniloop = True
    while miniloop == True:
        try:
            hours = input ("How many hours did you work? ")
            minutes = input ("How many minutes? ")
            global time
            time = float(hours) + float(minutes) / 60.
            print ("\n\nYou made... $" + str(round(payRate * time, 2)))
            spendingMoney = defaultSpendingMoney
            if (time > 30.):
                spendingMoney += round(payRate / 2. * (time - 30.),2) # for every hour over 30 that you work, your spending money goes up by half your pay rate
            print ("You have $" + str(spendingMoney) + " of spending money this week.\n\n")

            miniloop = False
        except:
            print ("\n--Error, please type a number.--\n\n---------------------------------------")

if (__name__ == '__main__'):

    startOver = True

    while startOver == True:
        fn()
        a = raw_input("Press ENTER to exit or type a key to restart. ")
        if (a == ''):
            startOver = False
        print ("\n\n---------------------------------------")
    else:
        ()
