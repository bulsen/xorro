# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import base64
# utf-8 uyumlu

## keys
#

xor_arr=[0x19,0x92,0x28,0x07,0x31,0xbe]
xor_crack_arr = reversed(xor_arr)


#########################################


# thefile
message_arr = []
f = open("encoded","rb")
for elems in f:
	message_arr.append(elems)

message = ""
for elsm in message_arr:
	message += elsm

unbased = base64.b64decode(message)


gl_arr =[]
lilly= []
for buffers in unbased:
	lilly.append(ord(buffers))


gl_arr.append(lilly)
counter = 0
for ox in xor_crack_arr:
	mini_arr = []
	for keys in gl_arr[counter]:
		mini_arr.append(keys^ox)
	gl_arr.append(mini_arr)
	counter += 1

asd = gl_arr[len(gl_arr)-1]

mess= ""
for ellm in asd:
	mess += chr(ellm)

print mess
