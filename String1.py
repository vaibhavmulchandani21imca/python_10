s=input("Enter String : ")

up=0
lw=0
al=0
nm=0
sp=0

for i in s:
    if i.isupper():
        up=up+1
    elif i.islower():
        lw=lw+1
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    
print("Total Upper Case : " ,up)
print("Total Lower Case : " ,lw)
print("Total Alphabets : " ,al)
print("Total Numeric : " ,nm)
print("Total Space : " ,sp)

        
