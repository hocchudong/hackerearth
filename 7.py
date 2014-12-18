# Fizz Buzz Test

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print "FizzBuzz"
    elif not i % 3:
        print "Fizz"
    elif not i % 5:
        print "Buzz"
    else:
        print i
