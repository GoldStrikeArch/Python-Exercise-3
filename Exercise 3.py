"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

def list_less_than_5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for element in a:
      if element < 5:
          print(element)


#list_less_than_5()

#extra
def new_list():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    my_list = []
    for element in a:
        if element <5:
            my_list.append(element)
    print(my_list)


#extra 2
def one_line():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([b for b in a if b < 5])


#extra 3

def give_number():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    num = int(input("Please give us a number "))
    my_list = []
    for element in a:
        if element < num:
            my_list.append(element)
    print(my_list)


give_number()