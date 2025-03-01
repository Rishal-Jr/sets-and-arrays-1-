setx={1,3,5,7,9,10}
sety={2,4,6,8,10}
print("Original Set:",setx,sety)
setz=setx.intersection(sety)
print(setz)
seta=setx.union(sety)
print(seta)
setb=setx.difference(sety)
print(setb)