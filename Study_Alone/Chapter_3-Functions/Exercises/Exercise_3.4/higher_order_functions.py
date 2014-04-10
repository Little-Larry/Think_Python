# higher_order_function.py
# by Lawrence X. Amlord
# Apr 10th, 2014

# part 1.
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)


# part 2.
def do_twice(f, n):
	f(n)
	f(n)

def print_stuff(n):
	print n

do_twice(print_stuff, 'sucker')

# part 3.
def print_twice(s):
	print s
	print s

do_twice(print_twice, 'spam')

# part 4.
def do_four(f, val):
	do_twice(f, val)
	do_twice(f, val)

do_four(print_stuff, 'quux')
