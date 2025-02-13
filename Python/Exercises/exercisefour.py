a = str("apple")                                #str
b = int(123)                                    #int
c = float(1.23)                                 #float
d = complex(1j)                                 #complex
e = list["apple", "banana", "orange"]           #list         
g = range(5)                                    #range
       #dict
i = set("apple", "banana", "orange")            #set
j = frozenset({"apple", "banana", "orange"})    #frozenset
k = bool(True)                                  #bool
l = b"Hello"                                    #byte
m = bytearray(5)                                #bytearray
n = memoryview(bytes(5))                        #memoryview
o = None                                        #nonetype

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(g))

print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))