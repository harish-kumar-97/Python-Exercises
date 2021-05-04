for i in range(5):
    try:
        print(i)
    except ZeroDivisionError:
        print(e, "--> Division by 0  is not allowed")
    finally:
        print("I don't care, I'm getting printed either way")
    print("The rest of the code...")