#task 8 - creating a hangman game
secret_phrase = open('secret_phrase','r')
for line in secret_phrase:
    secret_phrase = line

#showing secret phrase without the letters
show_phrase = '------'

x = list(secret_phrase)
y = list(show_phrase)

name = raw_input ('What is your name?')
print 'Hi' + name ,'Welcome to Hangman? Here is the phrase you need to guess' + show_phrase

count = 0

#starting to play the game
#26 correspond to the number of letter in the alphabet
while count <= 26:
    if '-'in y:
        r = raw_input('What is your guess ?')
    print "the player is given", y , 'They guess' + r + "."
    if r in x:
        y[x.index(r)] = r
        print 'Your guess is', y
        count += 1
        print y

    else:
        print 'Wrong answer'
    print 'well done you found the good answer in', count


while count <= 26:
    if '-'in y:
        m = raw_input('What is your guess ?')
    print "the player is given", y , 'They guess' + m + "."
    if m in x:
        y[x.index(m)] = m
        print 'Your guess is', y
        count += 1
        print y

    else:
        print 'Wrong answer'
    print 'well done you found the good answer in', count


while count <= 26:
    if '-'in y:
        i = raw_input('What is your guess ?')
    print "the player is given", y , 'They guess' + i + "."
    if i in x:
        y[x.index(i)] = i
        print 'Your guess is', y
        count += 1
        print y

    else:
        print 'Wrong answer'
    print 'well done you found the good answer in', count


while count <= 26:
    if '-'in y:
        o = raw_input('What is your guess ?')
    print "the player is given", y , 'They guess' + o + "."
    if o in x:
        y[x.index(o)] = o
        print 'Your guess is', y
        count += 1
        print y

    else:
        print 'Wrong answer'
    print 'well done you found the good answer in', count

#The player found the secret phrase. It took him 4 tries to find the whole word.
