#open mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
#lst = list()
count = 0

for line in fh:             #loop through text file
    
    for words in line:      #loop through line
        line =  line.rstrip()   #strip white space right
        words = line.split()    #split line into words
        
    if "From" in words:
        print(words[1])  #print address			
        count = count + 1       #counter 
        
    
    
print('There were',count,'lines in the file with From as the first word')                         
