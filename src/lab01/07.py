crashSTR=input("string: ")
answer=""
A=0
B=0
x=0
for i in range(0,len(crashSTR)):
    if crashSTR[i].isupper():
        answer+=crashSTR[i]
        A=int(i)
        for I in range(len(crashSTR[A]),len(crashSTR)):
            if crashSTR[I] in "0123456789":
                B=int(I)+1
                break
        #print(crashSTR,A,B,crashSTR[A:B+1])
        #if len(crashSTR)+1%(B-A)!=0:
            #crashSTR=crashSTR.zfill(len(crashSTR)+(B-A))
            #print(crashSTR)
        #for x in range(len(crashSTR[A]),len(crashSTR)+1,(B-A)):
            #answer+=crashSTR[x]
        while A+x<len(crashSTR):
            x+=(B-A)
            if A+x<len(crashSTR):
                answer+=crashSTR[A+x]
if answer[-1]!=".":
    answer+=crashSTR[-1]
print(answer)
