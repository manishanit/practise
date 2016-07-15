import urllib
fhand=urllib.urlopen('http://getbootstrap.com/')
for line in fhand:
    print(line.strip())
