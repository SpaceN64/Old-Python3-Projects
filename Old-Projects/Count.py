while True:
    print("10 or 100?")
    10 = ["10", "ten"]
    100 = ["100", "a hundred", "hundred"]

    count = input(">>> ")

    if count in 100:
        print("")
        n = 0
        while n < 100:
            print(n)
    elif count in 10:
        n = 0
         while n < 10:
            print(n)
    else:
        print("That is not a valid command!")
