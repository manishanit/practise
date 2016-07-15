#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of
#mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who
#sent the mail. The program creates a Python dictionary
#that maps the sender's mail address to a count of the
#number of times they appear in the file. After the
#dictionary is produced, the program reads through the
#dictionary
#using a maximum loop to find the most prolific committer.
solution:
    name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail=list()
for line in handle:
    lst=list()
    if line.startswith('From '):
        lst=line.split()
        mail.append(lst[1])
email=dict();
for counts in mail:
    email[counts]=email.get(counts,0)+1
bigcount=None
bigemail=None
for b in email:
    if(bigcount==None or bigcount<email[b]):
        bigcount=email[b]
        bigemail=b
        
print bigemail,bigcount
