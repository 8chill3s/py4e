# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0

try: fh = open(fname)
except:
    print('Error, file does not exist. Try again :(')
    exit()

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        x = float(line[20:])  # extract spam numbers from opened file
       # continue
        count = count + 1  # update count number of lines
        total = total + x  # running total of spam numbers


#calculate avg number
avg = total / count #calculate average number
print('Average spam confidence:',avg)



