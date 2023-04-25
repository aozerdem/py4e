fhand=open("sample text file.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line)

 
