def binary(number):
    if number>=1:
        binary(number//2)
    print(number%2, end=" ")

def octal(number):
    print("\n" ,oct(number))

def hexadecimal(number):
    # hexadecimal(number / 16)
    # x = (number % 16)
    # if (x < 10):
    #     print(x)
    # if (x == 10):
    #     print("A")
    # if (x == 11):
    #     print("B")
    # if (x == 12):
    #     print("C")
    # if (x == 13):
    #     print("D")
    # if (x == 14):
    #     print("E")
    # if (x == 15):
    #     print("F")
    a = "{0:x}".format(number)
    print(a)

binary(256)
octal(42)
hexadecimal(10)
