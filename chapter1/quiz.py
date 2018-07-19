truthy = ['true', 'True', 't', 'T', 'yes', 'Yes']
falsey = ['false', 'False', 'f', 'F', 'no', 'No']

print("Welcome to the odd survey!")
print("Answer all questions please\n")

correct_answers = 0
incorrect_answers = 0

name = input("\nWhat is your name?\n")
print("CORRECT! I couldn't possibly know but I trust!\n")
correct_answers += 1

math = input("\nWhat is 40 + 2?\n")
if math == '42':
    print("Correct!")
    correct_answers += 1
else:
    print("Ooo sorry, that's not the meaning of life")
    incorrect_answers += 1

human = input("\nAre you human?\n")
if human in truthy:
    correct_answers += 1
    print("Hmm, ok I believe you")
elif human in falsey:
    incorrect_answers += 1
    print("I highly doubt it you troll")

new_name = input("\nWhat is your name again?\n")
if new_name == name:
    print("Just checkin!")
    correct_answers += 1
else:
    print("Ah Ha! Gotcha!")
    incorrect_answers += 1

correct_answers += 1



print("\nCorrect: " + str(correct_answers))
print("Incorrect: " + str(incorrect_answers))
