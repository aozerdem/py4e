fhand=open("sample text file.txt")
for line in fhand:
    line=line.rstrip()
    if line.startswith("From:"):
        print(line)
