largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':  break

    #validate input
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

     #compare integers
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    elif smallest is None:
         smallest = num
    elif num < smallest:
         smallest = num



    #print (num)

print('Maximum is',largest)
print('Minimum is',smallest)
