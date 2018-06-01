#open mbox-short.txt

fname = input("Enter file name: ")
open(fname)

if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

print("There were", count, "lines in
