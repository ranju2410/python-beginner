n=int(input("ENTER A NUMBER : "))

# FINDING FACTORIAL USING WHILE LOOP FUNCTION
c=1
ln=n
fn=n
if ln!=0:
    c=ln
    while ln >= 2:
        c=c*(ln-1)
        ln=ln-1

print("Factorial for ", n , "While Loop Method is ", c)

#FINDING FACTORIAL USING RECURSIVE METHOD

def fact(fn):
    if fn<2:
        return 1
    else:
        return fn*fact(fn-1)

r=fact(fn)
print("Factorial for ", fn , "Recursive Function Method is ", r)

