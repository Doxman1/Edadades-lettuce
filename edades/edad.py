#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Edades:
	def verificar(self,edad):
		try:
			edad1 = int(edad)
			if(edad1<0):
				return "no existes"
			elif(edad1<13 and edad1>0):
				return "eres nino"
			elif(edad1<18 and edad1>13):
				return "eres adolescente"
			elif(edad1<65 and edad1>18):
				return "eres adulto"
			elif(edad1<120 and edad1>65):
				return "eres adulto mayor"
			elif(edad1>120):
				return "eres mumm-ra"
			
		except ValueError:
			return "los datos deben ser numericos"	
if __name__ == "__main__":
	import doctest
	doctest.testfile("unit.txt")
	