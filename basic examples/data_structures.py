#!/usr/bin/env python3

import traceback


def hello_world():
    print('Hello World')  # In Python3, the paren's around print are required.


def string_concat():
    a = 'this string'
    print('a:', a)
    b = ' is now one string!'
    print('b:', b)
    c = a + b  # Python is pass by value, so you can
    print('combine the two:', c)


def list_example():
    my_list = [1, 132, 2, 1, 'asb', True, (None, None)]  # can throw anything in here as long as comma separated
    print('my_list:', my_list)

    # find sum of all number in the list
    total = 0
    for elm in my_list:
        try:
            total += elm
        except TypeError:
            pass  # this happens when you try to '+' non agreeing types
    print('total of nums in list:', total)
    print()

    # change first element to a new string
    print('Replace first element of list with \'new_string\'')
    new_string = 'new_string'
    my_list[0] = new_string
    print('new_string:', my_list)

    # find how many strings in list now
    num_str = 0
    for elm in my_list:
        if isinstance(elm, str):
            num_str += 1
    print('number of strings:', num_str)
    print()

    # add element to end
    print('Appending 100 to end of my_list')
    new_my_list = my_list.append(100)  # lists are mutable, so any of these actions actually return None
    print('my_list:', my_list)
    print('Object returned from my_list.append:', new_my_list)
    total = 0
    for elm in my_list:
        try:
            total += elm
        except TypeError:
            pass  # this happens when you try to '+' non agreeing types
    print('total of nums in list:', total)
    print()


def dictionary_example():
    # subfunction will only exist in the scope of this function
    def print_dict(d):
        print('dict = {')
        for key in d:
            print('    ' + str(key) + ': ' + str(d[key]) + ',')  # can get items from dict like d[key] -> values
        print('}')

    dictionary = {
        1: 'sup',
        'a': 'dawg',
        None: 'yes',
        'this': 'still',
        'works': True,
    }
    print_dict(dictionary)
    print()

    # add some elements to the dictionary
    print('Lets add some some numbers where key is the number and value is the square')
    for i in range(10):
        dictionary[i] = i * i
    print_dict(dictionary)
    print('')

    print('What if I try to search for a key that doesn\'t exist?')
    print('dictionary[\'not_in_here\'] returns:')
    try:  # I don't really wanna crash the program so I'll just wrap it
        print(dictionary['not_in_here'])
    except KeyError:
        print()
        traceback.print_exc()
        print()

    # dictionaries are pass by reference, you can create a copy by setting it equal to another even if empty
    a = {}
    b = a
    print('a:', a)
    print('b:', b)
    print('where b -> a on creation')
    print('so doing b[\'test\'] = 123')
    b['test'] = 123
    print('a:', a)
    print('b:', b)
    print()


def tuple_example():
    birthdays = {
        'Roger': (1, 20),
        'Mike': (4, 30),
        'Glenn': (2, 29),
        'Janet': (12, 123)
    }

    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    print('You can assign variables via tuples rather than getting it from the index value')
    print('Birthday:', birthdays)

    for name in birthdays:
        month, day = birthdays[name]  # but you could just do a month = birthdays[name][0] if you wanted
        print('%s birthday is on %s %i' % (name, months[month], day))


# The pythonic way of doing somthing, is essentially to just do it and catch any exceptions that may happen
def put_num_in_str(num):
    if num:
        try:
            string = 'The number you inputted is:'
            if float(num) == int(num):  # don't want to truncate floats, but don't want to have .0 after ints
                print(string, int(num))  # you could also do a print(string + ' ' + str(num)) but that's inelegant
                num = int(num)  # overwriting same variable but different type. Generally this is frowned upon.
            else:
                print(string, float(num))
                num = float(num)
            print('number squared:', num * num)

        except ValueError:
            # This would happen if you trying to convert a non number input
            print(num, 'is not a valid number!')
    else:
        print('You did not input a number!')


def run_no_arg_example(funct, example_num):
    print('Example {}'.format(example_num))
    print()  # this is blank line
    funct()
    print('------------')
    input()


def main():
    counter = 1  # most counter should start at 0, but real world counting starts at 1

    run_no_arg_example(hello_world, counter)
    counter += 1

    run_no_arg_example(string_concat, counter)
    counter += 1

    print('Example' + str(counter))
    print()  # this is blank line
    my_num = input('Please Input a Number: ')
    put_num_in_str(my_num),
    print('------------')
    input()
    counter += 1

    run_no_arg_example(list_example, counter)
    counter += 1

    run_no_arg_example(dictionary_example, counter)
    counter += 1

    run_no_arg_example(tuple_example, counter)
    counter += 1


if __name__ == '__main__':
    print('\n\n')
    print('Welcome to the Data Structures Tutorial')
    print('Please Press Enter After Every Example To Move On and Follow If Prompted!')
    print()
    main()
    print()
    print('Out of Examples. Exiting. Thank You!')
