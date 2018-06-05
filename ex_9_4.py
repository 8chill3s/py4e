

#  open  mbox-short.txt 
name = input("Enter file:")
try:
    fh = open(name)
except:
    print('File cannot be opened', name)
    exit()


#create a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
count_names = dict()

#looks for 'From' lines and takes the second word of those lines as the person who sent the mail

for line in fh:  # loop through text file
    line = line.rstrip()  # strip white space right
    if not line.startswith("From:"): continue       #look for 'From'
    words = line.split()  # split line into words


    for name in words:
        if "@" in name:
         count_names[name] = count_names.get(name,0) +1     #idiom for make histogram

	#print(words)
    
#for key,value in count_names.items():             #analyze key value pair in dictionary
 #   print(key, value)

    
    
    
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
bigcount = None
bigword = None

for name,count in count_names.items():              #maximum loop for largest number
    if bigcount is None or count > bigcount:		# determine max key value 
        bigcount = count
	bigword = words								# words from lines
        

print(bigword[1], bigcount)
