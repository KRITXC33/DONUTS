@echo off & python -x "%~f0" %* & goto :eof 

# ==========================================================
# one way to place python script in a batch file
# place python code below (no need for .py file)
# ==========================================================

import sys
print "Hello World!"
for i,a in enumerate(sys.argv):
	print "argv[%d]=%s" % (i,a)
