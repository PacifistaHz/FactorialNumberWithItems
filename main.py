num=input("Enter a number: ")
num=int(num)
result=1
text=""
for i in range(num,0,-1):
    result*=i;
    text+=str(i)+"*"
text=text[0:len(text)-1]
print(text+"="+str(result))