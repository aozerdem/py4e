fname=input("Enter the file name: ")

#let's put a try and except for the bad file name input
try:
    fhand=open(fname)
except:
    print("File cannot be opened: ", fname)


count=0

for line in fhand:
    if line.startswith("Subject:"):
        count=count+1
print("There are", count, "subject lines in", fname)
