# read the whole file at once, return a single string
f = open('../data/drinks.csv', 'rU')
f.read()        # one big string including newlines
f.read()        # empty string
f.close()

