def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input('> ')
    print(f'What a great name you have {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    print("The first remainder:")
    rem3 = int(input('> '))
    print("The second remainder:")
    rem5 = int(input('> '))
    print("The first remainder:")
    rem7 = int(input('> '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f'Your age is {str(age)}; that\'s a good time to start programming!')


def count():
    print('Now I will prove to you that I can count to any number you want.')
    print('Enter any positive integer:')
    num = int(input('> '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    print("Please, enter your answer:")
    x = int(input('> '))
    while x != 2:
        print('Please, try again.')
        x = int(input("> "))
        if x == 2:
            print('Congratulations!')

def end():
    print('Have a nice day!')

def main():
    print('Please, enter your bot\'s name:')
    bot_name = input("> ")
    print('And the current year:')
    birth_year = input("> ")
    greet(bot_name, birth_year)  # change it as you need
    remind_name()
    guess_age()
    count()
    test()
    end()

if __name__ == '__main__':
    main()
