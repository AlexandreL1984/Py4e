#Reads number until the user enters done
while True:
    line = input('Enter a Number: ')
    if line == 'done':
        break
    if input(isnot.int):
        print('Invalid input')
        break
print('Done!')
