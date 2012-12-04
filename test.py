"""
    A test python file for our const keyword
"""

# Test basic functionality (make sure functionality isn't broken)
print "Testing basic functionality..."
x = 5
print 'x =', x, '(should be 5)'
x += 1
print 'x =', x, '(should be 6)'
print '\n'

# Test const (make sure keyword is seen as valid syntax)
print "Testing const..."
print "Trying statement: const y = 3"
const y = 3
print "y =", y
