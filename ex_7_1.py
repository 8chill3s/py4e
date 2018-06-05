# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)

except:
    print('Error, file does not exist. Try again :(')
    exit()

#count = 0
#for line in fh:
#   count = count + 1
#print('Line count:', count)

new_file = fh.read()
new_file = new_file.strip()
new_file = new_file.upper()
print(new_file)

