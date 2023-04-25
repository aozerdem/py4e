fruit="banana"
index=0
while index<len(fruit): #this is our loop but it will end when index=len(fruit)
    letter=fruit[index] #[index] indicates the position of each letter, starting from 0
    print(index, letter) #prints out position and the letter
    index=index+1 #to break out eventually
