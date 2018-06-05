

#  open  mbox-short.txt and figure out who has the sent the greatest number of mail messages
name = input("Enter file:")
try:
    fh = open(name)
except:
    print('File cannot be opened', name)
    exit()


#create a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
count_names = dict()

#looks for 'From ' lines and takes the second word of those lines as the person who sent the mail

for line in fh:  # loop through text file
    line = line.rstrip()  # strip white space right
    if not line.startswith("From:"): continue       #look for 'From'
    names = line.split()  # split line into words


    for name in names:
        count_names[name] = count_names.get(name,0) +1     #make histogram

#print(count_names)

#for name in count_names:
 #   print(name,count_names[name])

#for key,value in count_names.items():             #analyze key value pair in dictionary
 #   print(key, value)

#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
bigcount = None
bigword = None

for name,count in count_names.items():              #maximum loop for largest number
    if bigcount is None or count > bigcount:
        bigword = names
        bigcount = count

print(bigword, bigcount)

#if len(name) < 1 : name = "mbox-short.txt"



