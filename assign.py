import re
file_name=input('Enter the file name:')
handle=open(file_name)
handle1=handle.read()
y=re.findall('[0-9]+',handle1)
sum1=0
for x in y:
    x1=int(x)
    sum1=sum1+x1
print(sum1)

