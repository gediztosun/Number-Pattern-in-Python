try:
    num = int(input('Number? (Positive integers only) '))
except ValueError:
    print('NOT a positive integer')
else:    
    if (num > 0):
        SPACE = ' '
        LENGTH = len(str(num))

        print('')

        for i in range(0, num):
    
            for j in range(0, i):
                print(SPACE * (LENGTH - len(str(num - j))), num - j, sep = '', end = ' ')

            for j in range(0, (num - i) * 2 - 1):
                print(SPACE * (LENGTH - len(str(num - i))), num - i, sep = '', end = ' ')

            for j in range(i - 1, -1, -1):
                print(SPACE * (LENGTH - len(str(num - j))), num - j, sep = '', end = ' ')

            print('')

        for i in range(num - 2, -1, -1):

            for j in range(0, i):
                print(SPACE * (LENGTH - len(str(num - j))), num - j, sep = '', end = ' ')

            for j in range(0, (num - i) * 2 - 1):
                print(SPACE * (LENGTH - len(str(num - i))), num - i, sep = '', end = ' ')

            for j in range(i - 1, -1, -1):
                print(SPACE * (LENGTH - len(str(num - j))), num - j, sep = '', end = ' ')

            print('')
    else:
        print('NOT a positive integer')

