# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import base64


## keys
#

xor_arr=[0x19,0x92,0x28,0x07,0x31,0xbe]
xor_crack_arr = reversed(xor_arr)


#########################################


# the file 
f = open("README","rb")
f_arr =[]
for lines in f:
	for elems in lines:
		f_arr.append(ord(elems))


# man this is poetry
gl_arr=[]
gl_arr.append(f_arr)
counter = 0
for xo in xor_arr:
	mini_arr = []
	for keys in gl_arr[counter]:
		mini_arr.append(keys^xo)
	gl_arr.append(mini_arr)
	counter += 1

last_coded = gl_arr[len(gl_arr)-1]

message = ""
for elems in last_coded:
	message += chr(elems)

last_output = base64.b64encode(message)

w = open("encoded","w")
w.write(last_output)