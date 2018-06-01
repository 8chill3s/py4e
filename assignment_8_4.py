# use romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.strip()   #strip right side
    words = line.split()  #split line into words
    total_words = lst + words
    print(total_words)

    if words not in lst:
        lst.append(words)


lst.sort()
print(lst)

