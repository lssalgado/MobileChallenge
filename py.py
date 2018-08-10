from ctypes import *


hello_lib = cdll.LoadLibrary("main.so")
hello = hello_lib.valueExchanger
hello.restype = c_float

a = hello(10)

print ">>>> " + str(a)