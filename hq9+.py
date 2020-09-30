"""""
h - hello world
q - text from the prog
9 - lyric for 99 bottels of beer 
+ - increasing useless count 
"""""




user_input = input('Input for h9q+:')
s = user_input 

template = ''
count = 0 

for i in s.upper():
    if i == 'H':
        print("Hello world!")
    elif i == 'Q':
        print(s)
    elif i == '9':
        for i in range(99, 1, -1):
            print(template.format(i, i-1))
        print('1 bottle of beer on the wall.\nTake one down and pass it around, no more bottles of beer on the wall.')
        print('No more bottles of beer on the wall.\nGo to the store and buy some more, 99 bottles of beer on the wall.')
    elif i == '+':
        count += 1
        print(count) 