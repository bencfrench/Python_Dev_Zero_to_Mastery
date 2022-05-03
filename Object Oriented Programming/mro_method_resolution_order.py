# MRO: Method Resolution Order
class A():
	num = 10

class B(A):
	pass

class C(A):
	num = 1

class D(B, C):
	pass

print(D.num) # 1
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, 
# <class '__main__.C'>, <class '__main__.A'>, 
# <class 'object'>]

#     A 
#   <– –>
# B		  C 
#   –> <–
#     D

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass
print(M.mro())
# M > B > A > X > Y > Z