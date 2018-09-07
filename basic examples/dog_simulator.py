#!/usr/bin/env python3
import time
import random


class Dog:

    def __init__(self, name, breed=None):
        self.name = name

        if breed:
            self.breed = breed
        else:
            self.breed = 'unknown breed'

        self.hunger_level = 0

        self.is_dead = False
        self._status = None

        # this is 'protected' variable. Protected in the sense of it should be private, but not in the sense that you
        # can't actually reference it from outside the object.
        self._creation_time = time.time()
        self._cause_of_death = None

    def feed(self):
        self.update_age()
        if not self.is_dead:
            self.hunger_level -= 1
            if self.hunger_level < -5:
                self.is_dead = True
                self._cause_of_death = 'overeating'
            elif self.hunger_level < -3:
                print('Watch out, {} is getting fat. You should go for a walk'.format(self.name))
                self._status = 'fat'
            else:
                self._status = 'well'
        if not self.is_dead:
            print('{} is at hunger level: {}'.format(self.name, self.hunger_level))
        print()
        self.dead_msg()

    def walk(self):
        self.update_age()
        if not self.is_dead:
            dist_walked = int(random.random() * 9) + 1
            print('{} went on a walk for {} km.'.format(self.name, dist_walked))
            self.hunger_level += int(dist_walked / 3)

            if self.hunger_level > 8:
                self.is_dead = True
                self._cause_of_death = 'exhaustion'
            elif self.hunger_level > 4:
                print(self.name, 'is pretty tired. You should feed it.')
                self._status = 'fatigued'
            else:
                self._status = 'wells'

        print()
        self.dead_msg()

    def update_age(self):
        current_time = time.time()
        if current_time - self._creation_time > 150:  # kill dog after 2.5 minutes
            self.is_dead = True
            self._cause_of_death = 'old age'

    def dead_msg(self):
        if self.is_dead:
            print('Unfortunately %s has died of %s.' % (self.name, self._cause_of_death))

    def get_status(self):
        if not self._status:
            self._status = 'well'
        return self._status


class DogManager:
    def __init__(self):
        self._num_default_dog = 1
        self.dog_list = []
        self.dog_dict = {}

    # technically camelCase isn't PEP-8 but it makes too much sense to not use.
    def adoptDog(self):
        print()
        print('So you want to adopt a dog')

        name = None
        counter = 0
        while not name and counter < 10:
            name = input('What\'s its name?: ').strip()
            if not name:
                # blank name. '', None, and [] evaluate to False logically
                print('Sorry a name is required.')
            elif name.lower() in self.dog_dict:  # lower() returns the string but all lowercased
                print('Sorry dog must have unique names.')
                print('Names already in use:')
                for name in self.dog_dict:
                    print('    ' + name)
                print()
            counter += 1

        if counter >= 10:
            print('Too many failed attempts, a default dog will be adopted!')
            name = 'Poochie ' + str(self._num_default_dog)
            self._num_default_dog += 1
            breed = None
        else:
            breed = input('What\'s %s\'s breed?: ' % name)  # if nothing entered this will be handled in init of Dog()
        print()

        dog = Dog(name, breed)
        self.dog_list.append(dog)
        self.dog_dict[name.lower()] = dog

        if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            indefinite_article = 'an'
        else:
            indefinite_article = 'a'

        print('Done. You\'ve adopted ' + indefinite_article + ' {} named {}!'.format(dog.breed, dog.name))
        print()
        time.sleep(1)

    def feedDog(self):

        if self.dog_list:  # if no dogs in list
            self.print_dog_house()
            print('Pick a Dog you want to Feed or \'q\' to go back.')

            while True:
                dog = None
                dog_to_feed = input('Which dog do you want to feed?: ').lower().strip()
                print()
                if dog_to_feed == 'q':
                    return  # exit method
                try:
                    # user picked a number
                    dog = self.dog_list[int(dog_to_feed)]
                except ValueError:
                    try:
                        dog = self.dog_dict[dog_to_feed.lower()]
                    except KeyError:
                        print('Could not find: ' + dog_to_feed)
                        time.sleep(1)
                except KeyError:
                    print('Dog {} is an invalid choice'.format(dog_to_feed))
                    time.sleep(1)
                if dog:
                    dog.feed()
                    if not dog.is_dead:
                        print('Dog Successfully Fed!')
                    print()
                    time.sleep(1)
                    break

        else:
            print('You own no dogs at the moment. Please adopt one first!')
            print()
            time.sleep(1)

    def walkDog(self):
        if self.dog_list:
            self.print_dog_house()
            print('Pick a Dog you want to Walk or \'q\' to go back.')
            while True:
                dog = None
                dog_to_walk = input('Which dog do you want to walk?: ').lower().strip()
                print()
                if dog_to_walk == 'q':
                    return  # exit method

                try:
                    # user picked a number
                    dog = self.dog_list[int(dog_to_walk)]
                except ValueError:
                    try:
                        dog = self.dog_dict[dog_to_walk.lower()]
                    except KeyError:
                        print('Could not find: ' + dog_to_walk)
                except IndexError:
                    print('Dog {} is an invalid choice'.format(dog_to_walk))
                if dog:
                    dog.walk()
                    if not dog.is_dead:
                        print('Dog Successfully Walked!')
                    print()
                    time.sleep(1)
                    break
        else:
            print('You don\'t own any dogs at the moment. Please adopt one first!')
            print()
            time.sleep(1)

    def print_dog_house(self):
        if self.dog_list:
            print('You have', len(self.dog_list), 'dog(s) right now:')
            for ind, dog in enumerate(self.dog_list):
                if dog.is_dead:
                    status = 'Dead'
                else:
                    # Alive
                    dog_status = dog.get_status()
                    if dog_status.lower().strip() != 'well':
                        status = 'Alive but ' + dog_status
                    else:
                        status = 'Alive and ' + dog_status

                    status += ' - hunger_level = {}'.format(dog.hunger_level)
                print('    ' + str(ind) + ': ' + dog.name + ' - ' + status)
            print()
        else:
            print('You don\'t own any dogs at the moment. Please adopt one first!')
            print()


if __name__ == '__main__':
    print()
    print('Welcome to Super Easy Dog Simulator')
    print()
    options = 'Options:\n\n' \
              '1: Adopt Dog\n' \
              '2: Feed Dog\n' \
              '3: Walk Dog\n' \
              '4: Check On Dogs \n' \
              '\n' \
              'q: Quit'

    dog_manager = DogManager()
    while True:
        print(options)
        decision = input('Your Choice: ').strip()  # strip() takes out leading and trailing whitespace
        print()
        if decision == '1':
            dog_manager.adoptDog()
        elif decision == '2':
            dog_manager.feedDog()
        elif decision == '3':
            dog_manager.walkDog()
        elif decision == '4':
            dog_manager.print_dog_house()
            time.sleep(1)
        elif decision == 'q':
            break
        else:
            print('Sorry.', decision, 'is an invalid decision. Try Again')
            print()
            time.sleep(.5)
    print()
    print('Thank You For Using Super Easy Dog Simulator. See you Later!')
    print()
