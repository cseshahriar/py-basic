# Files 
# windows backslash /  
try:
    with open('data.txt') as fobj:
        cotents = fobj.read()
        print(cotents)
except Exception as e:
    print("File Error: ", e)

'''
try:
    fobj = open('data\\article.txt')
except Exception as e:
    print('File Error: ', e)
else: 
    content = fobj.read()
    print(content)
finally:
    fobj.close() 
'''

## Write text in a file
'''
w = write
a = append 
r = read # default
or
wt = write
at = append 
rt = read
t is for text mode with is set by default
'''
# file write 
'''
try:
    with open('data.txt', 'w') as obj:
        obj.write('1')
        obj.write('\n')
        obj.write('28484')
except Exception as e:
    print(e)
'''