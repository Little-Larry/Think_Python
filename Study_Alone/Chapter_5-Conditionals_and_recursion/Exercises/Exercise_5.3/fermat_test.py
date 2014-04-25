# fermat_test.py
# by Lawrence X. Amlord
# Apr 25, 2014
# Xi'an, China
# GNU GPLv3

def check_fermat(a, b, c, n):
	if (((a ** n) + (b ** n)) == (c ** n)):
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."

def fermat_experiment():
	print "Starting Fermat Experiment..."
	a = int(raw_input("a = "))
	b = int(raw_input("b = "))
	c = int(raw_input("c = "))
	n = int(raw_input("n = "))
	check_fermat(a, b, c, n)

if __name__ == '__main__':
    print "Checking Fermat Hypothesis ..."
    print "Case: a = 3, b = 4, c = 8, n = 3"
    check_fermat(3, 4, 8, 3)
    print "Your turn ;)"
    fermat_experiment()


