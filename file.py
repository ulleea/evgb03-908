def writearray (file,output):
    with open('/home-local/student/Desktop/hellogays','r') as file, open('/home-local/student/Desktop/input','w') as output:
        q=file.read()
        print(q)
        output.write(q)
        print('-------------------')
    with open('/home-local/student/Desktop/input','r') as output:
        print(output.read())
    pass
a,b=0,0
file=open('/home-local/student/Desktop/input','r')
print(file.read())
file.close()
print('---------')
writearray(a,b)
print('---------')
file=open('/home-local/student/Desktop/input','r')
print(file.read())
file.close()