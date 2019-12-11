"""
for exercises:
https://www.w3resource.com/python-exercises/file/
"""
#write
f= open("file_handler_trial.txt", "w")
f.close()
#read
f = open("file_handler_trial.txt", "r")
#append
f = open("file_handler_trial.txt", "a")
#to write
f.write("this is a trial run")
f.close()
#to read line
f.readline(1)
#To read a list of lines use:
fh.readlines()

#where the pointer is
f.tell()
#seek(offset[, whence])
f.seek(0,0)

line = f.readline()
print ("Read Line: %s" % (line))

for i in range(1, 50):
    f.write("line      %d\n" % (i))
f.close()
with open("file_handler_trial2","w") as f:
    for i in range(1, 50):
        f.write("line      %d\n" % (i))



def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read(f)


