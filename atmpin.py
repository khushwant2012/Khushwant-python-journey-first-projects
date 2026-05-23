pin=int(input('Enter your Atm pin:'))
balance=5000
if pin == 1234:
    print('welcome to your account')
    option=input('what do you want to do? withdraw or check balance? ')
    if option == 'cheeck balance':
        print('your balance is',balance)
    elif option == 'withdraw':
        amont=int(input('how much do you want to withdraw? '))
        if amont > balance:
            print('insufficient balance')
        else:
            balance=balance-amont
            print('you have withdrawn',amont,'your new balance is',balance)
else:
    print('incorrect pin')

    