raw_text = open("lox1.txt", "r") #Opens raw file
data = raw_text.read()
raw_text.close()
clean_text = data.split()#Transforms into dict
c = ' '.join(clean_text)#Transforms into string
b = open("otvet1.txt", "w")#Write result to new file
b.write(c)
b.close()
