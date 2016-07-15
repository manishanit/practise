def count(char,content):
    count=0
    for c in content:
        if c == char:
            count += 1
    return count

file = input("Enter the filename")
with open(file) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    count1 = count(char,text)
    perc = 100*(count1/len(text))
    print("{0},{1}".format(char,round(perc,2)))
    
    
