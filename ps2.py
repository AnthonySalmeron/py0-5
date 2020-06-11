var1 = () #tuple-immutable
var2 = var1 + (1,) #if only one element, write like this
var3 = 'a'
var4 = "b"
(var3,var4) = (var4,var3)
print(var3) # b
