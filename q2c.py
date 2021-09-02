def divide(x, y):
    try:
              result = x / y
    except ZeroDivisionError:
        print("Zero division error ")
    else:
        print("Your answer is :", result)
    finally:
        print('This is always executed')


divide(3, 2)
divide(3, 0)