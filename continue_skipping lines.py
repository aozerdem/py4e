fhand=open("sample text file.txt")
for line in fhand:
    line=line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

#above, is a way to select particular lines. in our example it's the one starting with "From:"
print("\n")

#below, is another way

fhand=open("sample text file.txt")
for line in fhand:
    line=line.rstrip()
    if not "From:" in line:
        continue
    print(line)
