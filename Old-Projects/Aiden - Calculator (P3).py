# Import
import time

# 4 things
multi = ["Multiplication", "multiplication", "Multi", "multi"]
div = ["Division", "division", "Div", "div"]
add = ["Addition", "addition", "Add", "add"]
sub = ["Subtraction", "subtraction", "Sub", "sub"]

# Intro
print("""Welcome to a Calculator made in Python!
(Dev
eloped by Aiden Sorabji)
""")
time.sleep(1.5)

# Choose M, D, A, S

print("""Would you like Multiplication, Division, Addition, or Subtraction?
""")
mdas = input(""">>> """)


# Multiplication Part
if mdas in multi:
    print("""
Please pick you first number
""")
    num = int(input(""">>> """))

    print("""
Please pick your second number
""")
    num2 = int(input(""">>> """))

    print("")

    a = 1
    while a <= num:
        print(a,"x",num2,"=", a * num2)
        a = a + 1
        

# Division Part
elif mdas in div:
    print("""
Please pick you first number
""")
    num3 = int(input(""">>> """))

    print("""
Please pick your second number
""")
    num4 = int(input(""">>> """))

    print("")

    b = 1
    while b<= num3:
        print(b,"÷",num4,"=", b / num4)
        b = b + 1
        


# Addition Part
elif mdas in add:
    print("""
Please pick you first number
""")
    num5 = int(input(""">>> """))

    print("""
Please pick your second number
""")
    num6 = int(input(""">>> """))

    print("")

    c = 1
    while c<= num5:
        print(c,"+",num6,"=", c + num6)
        c = c + 1
        

# Subtraction Part
elif mdas in sub:
    print("""
Please pick you first number
""")
    num7 = int(input(""">>> """))

    print("""
Please pick your second number
""")
    num8 = int(input(""">>> """))

    print("")
    
    d = 1
    while d<= num7:
        print(d,"-",num8,"=", d - num8)
        d = d + 1
        

# Someone says something else
else:
    print("""
That isn't something we can do!
""")
    time.sleep(2)
    exit()
