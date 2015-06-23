# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import base64

class Xorro:
	def __init__(self,xorr_arr,asegmental):
		self.xo_arr = xorr_arr
		self.ox_arr = reversed(xorr_arr)
		self.asegmental = asegmental


	def encrpyt(self,message):
		f_arr =[]
		for elems in message:
			f_arr.append(ord(elems))

		gl_arr=[]
		gl_arr.append(f_arr)
		counter = 0
		for xo in self.xo_arr:
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
		return last_output

	def decrypt(self,encrypted):
		message_arr = []
		for elems in encrypted:
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
		for ox in self.ox_arr:
			mini_arr = []
			for keys in gl_arr[counter]:
				mini_arr.append(keys^ox)
			gl_arr.append(mini_arr)
			counter += 1
		asd = gl_arr[len(gl_arr)-1]
		mess= ""
		for ellm in asd:
			mess += chr(ellm)
		return mess
