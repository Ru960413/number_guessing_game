#pure command line application
import random


def get_number():
    while True:
        try:
            min_number = int(input("Enter low bound: "))
            max_number = int(input("Enter high bound: "))
            number_to_guess = random.randint(min_number, max_number)

            if min_number < 0 or max_number < 0 or max_number < min_number:
                raise ValueError
            return number_to_guess

        except ValueError:
            print("Invalid number")
            continue
        

def guess(number_to_guess):

    counter = 0
    while True:
        counter += 1
        guess = int(input("Enter your guess: "))
        if guess > number_to_guess:
            print("Too Large")
        elif guess < number_to_guess:
            print("Too small")
        else:
            print("Congrats! You got it right! ")
            print (f"It took you {counter} times to guess")
            break
        
def main():
    number_to_guess = get_number()
    guess(number_to_guess)



if __name__ == "__main__":
    main()


