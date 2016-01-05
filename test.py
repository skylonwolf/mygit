from scrape import *
s.go('http://finfra.com/w')
print s.headers
print s.content[:100]
