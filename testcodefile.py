## This comment indicates version 1, original version
## Editting, version 2 store on branch




def get_name():
    name = input("What is your name? ")
    # print("Your name is {}.".format(name))
    return name

def greet_user():
    name = get_name()
    print("hello {}!".format(name))
    # statement = "Nice to meet you {}!".format(name)
    # print(statement)


greet_user()
