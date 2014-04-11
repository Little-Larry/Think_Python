# grid.py
# by Lawrence X. Amlord
# Apr 11th, 2014
# Xi'an, China

# part 1.
def print_bound_unit():
    print '+ - - - -',

def print_body_unit():
    print '|        ',

def do_twice(f):
    f()
    f()

def do_four_times(f):
    do_twice(f)
    do_twice(f)

def print_bound_line():
    do_twice(print_bound_unit)
    print '+'

def print_body():
    def print_body_line():
        do_twice(print_body_unit)
        print '|'
    do_four_times(print_body_line)

def print_grid():
    print_bound_line()
    print_body()
    print_bound_line()
    print_body()
    print_bound_line()

print_grid()


# the delimiter begin
print " "
print " "
# the delimiter end

# part 2.
def print_bound_line2():
    do_four_times(print_bound_unit)
    print '+'

def print_body2():
    def print_body_line():
        do_four_times(print_body_unit)
        print '|'
    do_four_times(print_body_line)

def print_quarter():
    print_bound_line2()
    print_body2()

def print_grid2():
    do_four_times(print_quarter)
    print_bound_line2()

print_grid2()
