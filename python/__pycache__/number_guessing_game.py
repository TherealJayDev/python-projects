import random
# adding difficulty feature
def get_difficulty():
     print('Choose difficulty level:')
     print('Level 1: 1 -50')
     print('Level 2: 1 - 100')
     print('Level 3: 1 - 200')
    
     while True:
          user_input = input('Choose from level 1 - 3: ')
          if user_input == '1':
               return 50
          elif user_input == '2':
               return 100
          elif user_input == '3':
               return 200
          else:
               print('Please choose one of the available level')
          
def guess_a_number():
    # start the game
    max_range = get_difficulty()
    print("Welcome! Let's play a game of guessing")
    print(f'I want you to guess a number from 1 - {max_range}')
    # generate a random number from range 1 - 100
    random_number = random.randint(1, max_range)
    # take the number of attempts
    attempts = 0
    guessed_correctly = False
    while not guessed_correctly:
        #get user input
        try:
            number = int(input('Enter a number you think would match my number: '))
            # check for error
        except ValueError:
            print(f'Please enter a valid number from 1 - {max_range}')
            continue

            # account for attempts
        attempts += 1
        print(f'You have attempted {attempts} times')
        # logic for the guessing
        if number < random_number:
                print(f'You guessed too low')
        elif number > random_number:
                print(f'Oops you guessed too high')
        else:
             guessed_correctly = True
             print(f'Hurray! Your guess was the same as the number in my mind, how telepathic but you tried {attempts} times')
        
        # option to restart the game
    guess_again = input('Would you like to try your telepathic skills again?:yes or no?')
    if guess_again == 'yes':
         guess_again()
    else:
         print('You agree you got lucky the first time right? So bye!')

# start the game
guess_a_number()