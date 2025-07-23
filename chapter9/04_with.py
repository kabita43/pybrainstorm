num= 10
# f= open("file.txt","w")
# f.print(num)
# f.close()

# the same can be written using statement like this
with open("file.txt","w") as f:
   f.write(str(num))


# you donot have to expliclty close the sile 