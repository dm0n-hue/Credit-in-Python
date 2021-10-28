# Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm

card_length = None
card_number = []

while card_length is None:
    # accepts input until valid
    card_number = list(input('Please enter your credit card number: '))
    # puts the input into a list to be iterated over later, accepts the input as strings
    card_length = len(card_number)
    # finds the length of the card number
    try:
        card_number = list(map(int, card_number))
        # re-maps the data to be integers
        if (card_length >= 13 and card_length <= 16):
            break
        else:
            print("Please enter a card number of the correct length")
    except ValueError:
        # if there's a letter detected, the program will stop
        print('Letter(s) detected. Please enter a valid card number')
        quit()
    except KeyboardInterrupt:
        # if a key command like ^C is used, then the program will stop
        print('\nKeyboard interruption: program exited.')
        quit()

lhun = 0
# will be used to store Lhun's number
toggle = 0
# will be used to switch between conditions

for i in range(card_length - 1, -1, -1):
    # counts from the length of the card down to 0
    if not toggle:
        lhun += card_number[i]
    else:
        tmp = card_number[i] * 2
        lhun = int(lhun + (tmp % 10))
        tmp = int(tmp / 10)
        lhun += tmp
    toggle = not toggle
    # toggled is changed to use a different condition in the next iteration

if lhun % 10:
    print('INVALID')
elif (card_number[0] == 3 and (card_number[1] == 4 or card_number[1] == 7) and card_length == 15):
    print('AMEX')
elif (card_number[0] == 5 and (card_number[1] >= 1 and card_number[1] <= 5) and card_length == 16):
    print('MASTERCARD')
elif (card_number[0] == 4 and (card_length == 13 or card_length == 16)):
    print('VISA')
else:
    print('INVALID')