import os;
from random import randint;

print("Welcome to the Great Chase\n")
print("Our Dearest Leader, Chump Dumpster-Fire, is chasing you down\n")
print("His people did some digging on you and it turns out your \ngreat-great-great-great grandparents were from Europe, gross!")
print("Chump Dumpster is gaining on you fast with the help of a secret service bridgade\n")
print("Try and escape to Canada!\n")
print("------------------------")

done = False
day = 0
miles_traveled = 0
distance = 100
wakefullness = 100

def game_over(done, miles_traveled, distance, wakefullness):
    if done == True:
        return True
    elif miles_traveled >= 100:
        return True
    elif distance <= 0:
        return True
    elif wakefullness <= 0:
        return True
    else:
        return False

def speeding(done):
    random_val = randint(0,9)
    if random_val == 1 or random_val == 7 or random_val == 4:
        return True
    else:
        return False

def check_status(done, miles_traveled, distance, wakefullness):
    if wakefullness <= 0:
        print("=========================")
        print("Game Over! You fell asleep and Chump caught up to you!")
        print("=========================")
        done = True
    if miles_traveled >= 100:
        print("=========================")
        print("Winner! You Escaped to Canada!")
        print("=========================")
        done = True
    if distance <= 0:
        done = True
        print("=========================")
        print("Oh No! Chump and his goons caught up to you!")
        print("=========================")

def status():
    print("Chump and his goons are " + str(distance) + " miles away")
    print("You're wakefullness level is at " + str(wakefullness) + "percent")

while done is False:

    if game_over(done, miles_traveled, distance, wakefullness) == True:
        break

    print("A. Stop somewhere and buy a redbull.")
    print("B. Drive the speed limit.")
    print("C. Drive well over the speed limit.")
    print("D. Stop at a motel for the night.")
    print("E. Status check.")
    print("Q. Drive full speed off the talest nearby mountain.")

    print("=========================")
    response = input("\n It's day " + str(day) + "...What will you do?\n")
    print("=========================")

    if response.lower() == 'a':
        distance -= 20
        day += 1
        wakefullness += 20
        check_status(done, miles_traveled, distance, wakefullness)
        os.system('clear')
    elif response.lower() == 'b':
        distance -= 20
        miles_traveled += 10
        wakefullness -= 30
        day += 1
        check_status(done, miles_traveled, distance, wakefullness)
        os.system('clear')
    elif response.lower() == 'c':
        os.system('clear')
        if speeding(done) == True:
            print("\nYou knew the risk and were pulled over for speeding! That'll set you back...\n")
            distance -= 30
            wakefullness -= 10
            check_status(done, miles_traveled, distance, wakefullness);
        else:
            distance += 20
            miles_traveled += 20
            day += 1
        check_status(done, miles_traveled, distance, wakefullness)
    elif response.lower() == 'd':
        distance -= 50
        wakefullness = 100
        day += 1
        os.system('clear')
    elif response.lower() == 'e':
        os.system('clear')
        print("=========================")
        print("=========================")
        print("It's day " + str(day))
        print("\nChump and his goonies are " + str(distance) + " miles away!!\n")
        print("You're feeling " + str(wakefullness) + " percent awake right now.\n")
        print("So far you've traveled " + str(miles_traveled) + " miles")
        print("====================")
        print("=========================")
    elif response.lower() == 'q':
        print("Damn you're hardcore\n")
        print("I mean I guess you win, Chump never really did catch up with you\n")
        print("Too bad after you died he pinned the entire election fraud scandal on you and now people from all over the world go to your grave to take steamy dumps on your grave... Worth it.")
        done = True


print("Game Over\n""Days: " + str(day) + "\nMiles Traveled out of 100: " + str(miles_traveled) + "\nDistance from Chump: " + str(distance) + "\n" + str(wakefullness) + " % Awake")
