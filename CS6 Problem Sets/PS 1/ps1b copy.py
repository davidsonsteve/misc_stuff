


print('Enter Balance:')
beginBalance = float(raw_input())
print('Enter APR:')
anualInterest = float(raw_input())

monthlyInterest = anualInterest / 12

monthNum = 0
minPayment = 10
balance = beginBalance

while balance > 0:

    if monthNum > 11:
        minPayment += 10
        monthNum = 0
        balance = beginBalance
        
    else:
        monthNum += 1
        newBalance = balance * (1 + monthlyInterest)
        balance = newBalance - minPayment
        

print 'Monthly Payment to pay off debt in 1 year: $', round(minPayment,2)
print 'Number of Months needed: ' , monthNum
print 'Balance: ' , round(balance,2)
