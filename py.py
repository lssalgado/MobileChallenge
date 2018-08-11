from ctypes import *


hello_lib = cdll.LoadLibrary("main.so")
hello = hello_lib.valueExchanger
hello.argtypes = [c_double]
hello.restype = c_double

a = hello(255)

print a
print ">>>> " + str(a)