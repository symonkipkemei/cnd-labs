# operational operators
# assignment operation
# comparision operation
# arthimaetic operation


def assignment_operator():
    # assigment operator
    # chained assigenment ( same value to multiple variables)
    symon = brian = kiptoo = 900
    print(symon, brian, kiptoo)

    # shorthand assigment (combination of arthimetic operators and assignment operators)
    y = 5
    y += 1
    print(y)

    y -=1
    print(y)

    y *= 3
    print(y)

    y /= 2
    print(y)




def arthimetic_operators():
    # 1. Addition
    # 2. subtraction
    # 3. multiplication
    # 4. division
    # 5. exponent
    # 6. Modulus (gives the remainder)
    # 7 .Floor division (abadons the decimal and gives an integer)

    y = 6
    x = 4
    # addition
    print(x + y)
    # subtraction
    print(x - y)
    # multiplication
    print(x * y)
    # division
    print(x / y)
    #modulus
    print(3 % 2)
    # flooor division
    print(3 // 2)
    print(5 // 3)




def membership_operators():

    # confirming sub_strings
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sem massa, imperdiet quis feugiat nec, maximus vitae justo. Ut a sem nulla. Ut pulvinar, libero sollicitudin lacinia faucibus, sapien mauris viverra nibh, eget blandit leo nibh ut neque. Pellentesque bibendum est quam, quis dictum eros placerat viverra. Nunc ac ultricies lacus. Suspendisse mollis sed diam feugiat bibendum. Vivamus imperdiet lacus velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed quam augue, volutpat ac nisi at, vestibulum sodales augue.

Ut varius magna at viverra rutrum. Sed rhoncus accumsan placerat. Maecenas sed pretium mauris. Sed tempus molestie sagittis. Proin bibendum dignissim tortor sed vestibulum. Etiam dignissim eros sed sem porttitor, non volutpat dui cursus. Nullam sit amet arcu porta, aliquet ante eget, venenatis felis. Duis sit amet aliquet tortor. Ut euismod molestie tellus ac lacinia. Ut tincidunt, tellus a rutrum semper, ex orci convallis libero, in accumsan ante lectus nec odio. Ut cursus fringilla nibh et bibendum.

Vestibulum ipsum velit, porttitor gravida tristique at, facilisis eu leo. Suspendisse ac nibh eros. Mauris sem ligula, sagittis eu purus nec, pellentesque faucibus nisi. Sed pulvinar augue nec mauris dictum, sit amet efficitur mi aliquam. Donec eu porttitor risus, suscipit laoreet erat. Duis purus magna, venenatis a placerat hendrerit, suscipit sit amet est. Donec luctus efficitur arcu nec rutrum. Vestibulum suscipit enim molestie libero mollis, in egestas est consequat. Integer urna dui, mollis vitae viverra a, gravida eu nisi."""
    # (in) checks whether an element is part of a colection
    x = 'symon' in text
    print(x)


    name = "symonkiplelgo"
    print(len(name))
    name = name.capitalize()
    print(name)
    print("symon" in name)



def boolean_values():

    # bool datattype with two possible outcomes (True or False)

    # assigning the feedback from membership in collection
    water = ["liquid", "soda", "fanta", "sprite", "cocacola", "mango"]
    ans = "mango" in water
    print(ans)


    # assigning a bool type to a variable

    ukweli = True
    uwongo = False

    print(ukweli, uwongo)



def comparison_operators():
    # Less than
    # less than or equal to
    # greater than
    # greater than or equal to
    # equal to
    # Not equal to

    # the results of these relational operators ia boolean value

    print(1 < 2)
    print(1 <= 2)
    print(1 > 2)
    print(1 >= 2)
    print(1 == 2)
    print(1 != 2)

    # comparision operators allow you to compare string to string and integer to integer

    # python compares if the sequence of characters  ids the same.

    print("string comparision", "symo" != "svkimondo")
    print("string comparision", "symo" == "symo")

    print("i" > "a")
    print("Harry" < "Sally")
    print("harry", "Harry" > "Harrx")

    print("i" > "a")


    print(ord("a"))
    print(ord("A"))


    import string
    print('For :', string.ascii_lowercase)
    print('')
    print('a =', ord('a'), 'b =', ord('b'), 'c =', ord('c'), 'd =', ord('d'), 'e =', ord('e'), 'f =', ord('f'), 'g =', ord('g')) 
    print('h =', ord('h'), 'i =', ord('i'), 'j =', ord('j'), 'k =', ord('k'))
    print('l =', ord('l'), 'm =', ord('m'), 'n =', ord('n'), 'o =', ord('o'), 'p =', ord('p'))
    print('q =', ord('q'), 'r =', ord('r'), 's =', ord('s'))
    print('t =', ord('t'), 'u =', ord('u'), 'v =', ord('v'))
    print('w =', ord('w'), 'x =', ord('x'))
    print('y =', ord('y'), 'and', 'z =', ord('z')) 
    print('')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('')
    print('For :', string.ascii_uppercase)
    print('')
    print('A =', ord('A'), 'B =', ord('B'), 'C =', ord('C'), 'D =', ord('D'), 'E =', ord('E'), 'F =', ord('F'), 'G =', ord('G')) 
    print('H =', ord('H'), 'I =', ord('I'), 'J =', ord('J'), 'K =', ord('K'))
    print('L =', ord('L'), 'M =', ord('M'), 'N =', ord('N'), 'O =', ord('O'), 'P =', ord('P'))
    print('Q =', ord('Q'), 'R =', ord('R'), 'S =', ord('S'))
    print('T =', ord('T'), 'U =', ord('U'), 'V =', ord('v'))
    print('W =', ord('W'), 'X =', ord('X'))
    print('Y =', ord('Y'), 'and', 'Z =', ord('Z'))

    integer = ord(3)
    print(integer)

    comparison_operators()
