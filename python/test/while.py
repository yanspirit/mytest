number = 23
stop = False
while not stop:
    guess = int(raw_input('enter an integer:'))
    if guess == number:
        print 'you are ok'
        stop = True
        break
    elif guess <number:
        print 'no,it\'s smaller'
    else:
        print 'no it\'s greater'
else:
    print 'the loop is over'


print 'Done.'