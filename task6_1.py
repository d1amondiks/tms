import re

fileinput=open('task1_input.txt','r')
b=fileinput.readlines()
regex=re.compile('(?<=[\s\n])[A-Z][a-z]{2,9}(?=[\s\,\.\;\:\n])')
try:
    fileoutput = open('task1_output.txt','w')
except:
    fileoutput = open('task1_output.txt', "x")
print b
fileoutput.write("words:")
fileoutput.flush()
print (b, type(b))
for word in regex.findall(str(b)):
    fileoutput.write(', ')
    fileoutput.write(word)
fileinput.close()
fileoutput.close()


