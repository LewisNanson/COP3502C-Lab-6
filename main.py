saved_password = ''

def encode(password):
    """Encodes a password and stores a given password"""
    global saved_password  # this function will access the variable in the global namespace
    saved_password = [(int(token) + 3) for token in password]  # turn every character into a digit and increase by 3
    saved_password = str(saved_password)


def decode():
    """Decodes and returns the stored password"""
    raise NotImplementedError


def main():
    while True:
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')

        user_selection = input('Please enter an option: ')
        if user_selection == '1':
            user_password = input('Please enter your password to encode: ')
            encode(user_password)
            print('Your password has been encoded and stored!')
        elif user_selection == '2':
            print('The encoded password is ' + saved_password + ', and the original password is ' + decode() + '.')
        elif user_selection == '3':
            break
        else:
            print('Invalid selection.')

if __name__ == '__main__':
    main()
