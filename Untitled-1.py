for i in range(1,100):
    if i % 3 == True:
        print(i,'BUZZ')
    if i % 5 == True:
        print(i,'FIZZ')
    if i % 5 and i % 3 == True:
        print(i,'FIZZBUZZ')
    else:
        print(i,'number doesnt exist')