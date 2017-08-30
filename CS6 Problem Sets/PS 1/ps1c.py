


print('Enter Balance:')
beginBalance = float(raw_input())
print('Enter APR:')
anualInterest = float(raw_input())

monthlyInterest = anualInterest / 12

balance = beginBalance

minMonthPay = 10.00

lowerbound = balance / 12
upperbound = (balance * (1 + monthlyInterest)**12.0) / 12.0
guess = round(((upperbound - lowerbound) / 2) + lowerbound,2)

#returns true if balance = 0 before 12 months, false if balance remains after 12
def testMMP(minMonthPay):
    balance = beginBalance
    for month in range(1,13):
        newBalance = balance * (1 + monthlyInterest) - minMonthPay
        
        if newBalance <= 0:
            print round(minMonthPay,2) , month, " $",round(newBalance,2)
            return True
    
        balance = newBalance
        #print "Month ", month, " $",round(newBalance,2)
    return False

while upperbound - lowerbound > .02:

    if testMMP(guess):
        #make new guess, half of guess - lowerbound.
        upperbound = guess
        #print upperbound
        #print lowerbound
        guess = round(((upperbound - lowerbound) / 2) + lowerbound,2)
        

    elif not testMMP(guess):
        lowerbound = guess
        #print lowerbound
        #print upperbound
        guess = round(((upperbound - lowerbound) / 2) + lowerbound,2)
    #print guess
