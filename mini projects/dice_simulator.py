#!/usr/bin/env python3

# EZPZ Project. You only really have to fill in anything with the TODO
# Should read the main to see how the program will be executed. But logic and flow
# should be intuitive. Good luck. Learn how to google better.

import random


# return a random die roll result of a n sided die
def roll_1_die(num_sides):

    # TODO: Change result to represent a random roll of a die with dice_side_num sides
    result = -1

    return result


# return a list of results of unique rolls for m number of dice with n sides
def roll_n_dice(num_dice, num_sides):

    result_list = []
    for i in range(num_dice):
        result_of_roll = roll_1_die(num_sides)  # do something with this
        # TODO: put result of roll into result_list
    return result_list


# return a tuple of number of rolls it took to reach a certain total and the list of results to that point
def how_many_rolls_to_get_total(threshold, num_sides):
    # TODO: Figure out how to keep track of rolls and the total of the previous rolls. Return them as a tuple
    return -1, []


# Yahtzee is where you roll 6 dice at the same time. If they are all 6, that's Yahtzee. Roll 6 dice at the same time.
# Then if it doesn't have all 6s, uptick a counter. When it does hit Yahtzee, return that number.
def how_many_rolls_to_get_yahtzee():
    # TODO: Figure out how to roll 6 dice at once. Then keep rolling until all result in 6's.
    # Note: Don't do unless you're sure roll_1_die() will not break. Might infinite loop in that case.
    return -1


# return True if die input is valid and False if not.
def is_dice_number_valid(input_num):
    try:
        num_dice = int(input_num)
        if num_dice < 1:
            print('Number of Dice Should Be More Than 0')
            return False
        return True  # is valid
    except ValueError:
        print('Number of Dice Should Be an Integer')
        return False


# return True if number of die sides is valid and False if not.
def is_die_side_number_valid(input_num):
    try:
        num_dice = int(input_num)
        if num_dice < 1:
            print('Number of Sides Should Be More Than 0')
            return False
        return True  # is valid
    except ValueError:
        print('Number of Sides Should Be an Integer')
        return False


def is_threshold_valid(input_num):
    try:
        int(input_num)
        return True
    except ValueError:
        print('Number of Sides Should Be an Integer')
        return False


def do_menu_choice(choice):

    if choice == '1':  # Roll 1 Die
        valid_inputs = True
        num_sides = 6  # default number of sides per die

        user_dice_side_num = input('Number of Sides on Die: ').strip('d')
        if user_dice_side_num:
            if is_die_side_number_valid(user_dice_side_num):
                num_sides = int(user_dice_side_num)
            else:
                valid_inputs = False
        else:
            valid_inputs = False

        if valid_inputs:
            result = roll_1_die(num_sides)
            print('Roll of ' + str(user_dice_side_num) + '-sided die is: ' + str(result))

            if result < 0:
                print('That doesn\'t look right....')
        else:
            print('Could not Roll Dice')

    elif choice == '2':  # Roll n dice
        valid_inputs = True

        user_dice_num = input('Number of Dice: ')
        if user_dice_num:
            if is_dice_number_valid(user_dice_num):
                num_dice = int(user_dice_num)
            else:
                valid_inputs = False
        else:
            num_dice = 1  # default number of dice

        user_dice_side_num = input('Number of Sides on Die: ').strip('d')
        if user_dice_side_num:
            if is_die_side_number_valid(user_dice_side_num):
                num_sides = int(user_dice_side_num)
            else:
                valid_inputs = False
        else:
            num_sides = 6

        if valid_inputs:
            results = roll_n_dice(num_dice, num_sides)
            for index, result in enumerate(results):
                print('Roll ' + str(index) + ': ' + str(result))

            if not results:
                print('You don\'t have any rolls. That\'s not right....')
        else:
            print('Could not Roll Dice')

    elif choice == '3':  # How Many Die Needed to Roll Total
        valid_inputs = True

        user_threshold = input('Threshold to Break: ')
        if user_threshold:
            if is_threshold_valid(user_threshold):
                threshold = int(user_threshold)
            else:
                valid_inputs = False
        else:
            threshold = 100  # default threshold

        user_dice_side_num = input('Number of Sides on Die: ').strip('d')
        if user_dice_side_num:
            if is_die_side_number_valid(user_dice_side_num):
                num_sides = int(user_dice_side_num)
            else:
                valid_inputs = False
        else:
            num_sides = 6

        if valid_inputs:
            result, list_of_results = how_many_rolls_to_get_total(threshold, num_sides)
            if list_of_results:
                print('Rolls: ')
                for num in list_of_results:
                    print('   ' + str(num))

            print('Number of Rolls: ' + str(result))
            if result < 0:
                print('That doesn\'t look right....')
        else:
            print('Could not Roll Dice')

    elif choice == '4':  # How Many Rolls Needed To Get Yahtzee
        result = how_many_rolls_to_get_yahtzee()
        print('It took you' + str(result) + ' rolls to get Yahtzee!')

        if result < 0:
            print('That doesn\'t look right....')
        elif result > 1000:
            print('That\'s hella rolls!')
        elif result > 100:
            print('Wow!')
        else:
            print('You must be lucky!')

    elif choice == 'q':
        return True
    else:
        print('That Option doesn\'t exist. Try again!\n')

    return False


if __name__ == '__main__':
    shouldBreak = False
    menu = 'What do you want to do?\n\n' \
           '1 - Roll 1 Die\n' \
           '2 - Roll n Dice\n' \
           '3 - How Many Die Needed to Roll Total\n'\
           '4 - How Many Rolls Needed To Get Yahtzee\n' \
           'q - Quit\n' \
           'Menu Choice: '

    while not shouldBreak:
        print()  # blank line for visual spacing
        print()
        menu_choice = input(menu).strip()  # get your user answer without extra whitespace
        shouldBreak = do_menu_choice(menu_choice)
    print()
    print('Thank you. Come again!')
