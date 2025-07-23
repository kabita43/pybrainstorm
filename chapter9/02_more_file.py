
# lines= f.readlines()
# print(lines)
# print(type(lines))
# f.close()
f= open("file.txt")
line= f.readline()

while( line!= ""):
    print(line)
    line= f.readline()  # Print the line

f.close()    