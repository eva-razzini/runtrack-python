i=0
while i <= 100:
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    if i%3 == 0:
        print("Fizz")
    else:
        print(i)
    if i%5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i + 1
