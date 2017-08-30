


print('Enter Balance:')
bal = float(raw_input())
print('Enter APR:')
apr = float(raw_input())
print('Enter Minimum Monthly Payment Rate:')
mmpr = float(raw_input())

print(bal)
print(apr)
print(mmpr)
prinp = 0
tap = 0

for i in range(1,13):
    mmp = mmpr * bal
    intp = (apr / 12) * bal
    prinp = mmp - intp
    rembal = bal - prinp
    print('Month ' + str(i))
    print('Minimum Monthly Payment:' + str(round(mmp,2)))
    print('Principle Paid:' + str(round(prinp,2)))
    print('Remaining Balance:' + str(round(rembal,2)))
    bal = rembal
    tap = tap + mmp

print('RESULT:')
print('Total Amount Paid: ' + str(round(tap,2)))
print('Remaining Balance:' + str(round(rembal,2)))
      





