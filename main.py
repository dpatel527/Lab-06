def encode(phrase):
    new_phrase = ""
    for element in phrase:
        element = int(element)
        element += 3
        element = str(element)
        new_phrase += element
    return new_phrase


def decode(new_phrase):
    old_phrase = ""
    for element in new_phrase:
        element = int(element)
        element -= 3
        element = str(element)
        old_phrase += element
    return old_phrase



def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            new_phrase = encode(phrase)
            print('Encoded phrase is', new_phrase)
        elif option == '3':
            print('Decoded phrase is', decode(new_phrase))


if __name__ == '__main__':
    main()