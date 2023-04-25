#From stephen.marquard@uct.ac.za Sat Jan 5, 09:14:16 2008
#let's find and extract the host of the mail

data="stephen.marquard@uct.ac.za Sat Jan 5, 09:14:16 2008"

atpos=data.find("@") #looking for the position of "@"
print(atpos)
#21

sppos=data.find(" ",atpos) #space position
print(sppos)
#31

host=data[atpos+1:sppos] #sppos not included
print(host)
