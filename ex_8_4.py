# use romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:             #loop through text file
    words = line.split()  #split line into words
  
    for word in words:     #loop through line 
        if word not in lst:  #append word to list
        	lst.append(word)
    
lst.sort()
print(lst)

