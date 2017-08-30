


print('Enter Balance:')
beginBalance = float(raw_input())
print('Enter APR:')
anualInterest = float(raw_input())

monthlyInterest = anualInterest / 12

balance = beginBalance

minMonthPay = 10.00

def testMMP(minMonthPay):
    balance = beginBalance
    for month in range(1,13):
        newBalance = balance * (1 + monthlyInterest) - minMonthPay
        
        if newBalance <= 0:
            print minMonthPay , month, " $",round(newBalance,2)
            return True
    
        balance = newBalance
        #print "Month ", month, " $",round(newBalance,2)

while not testMMP(minMonthPay):
    minMonthPay += 10.00
