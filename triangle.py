import os

i = 0

while i <= 5:    
    triangle = ''
    for k in range(0,i):
        triangle += '*'
    print(triangle)
    i += 1

print('******')

i = 0

while i <= 5:    
    triangle = ''
    for k in range(i,5):
        triangle += '*'
    print(triangle)
    i += 1

#os.system('Pause')
