import os
logo='''
 __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"
'''
def calc(b,c):
    if c=='+':
        add(b)
    elif c=='-':
        sub(b)
    elif c=='*':
        mul(b)
    elif c=='/':
        div(b)
    else:
        print("( Invalid input! )")
        return True
    return False

def add(b):
    print(f"\nthe result is: {b[0]+b[1]}")
def sub(b):
    print(f"\nthe result is: {b[0]-b[1]}")
def mul(b):
    print(f"\nthe result is: {b[0]*b[1]}")
def div(b):
    print(f"\nthe result is: {b[0]/b[1]}")

d=True
while d:
    print(f"Two numbers calculater\n{logo}\n")
    b=[]
    for a in range(2):
        b.append(float(input(f"Enter the {a+1}. number: ")))
    while d:
        c=input("\nChoose one of the following operators [ + , - , * , / ]: ")
        d=calc(b,c)
    if input("\nType \"yes\" if you wanna go again: ").lower()=='yes':
        d=True
        os.system("clear")
print("\nGood bye ;)")
