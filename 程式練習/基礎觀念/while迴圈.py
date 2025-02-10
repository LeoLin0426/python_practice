#做一個從1加到10的迴圈
sum=0
i=1

while i <= 10:
    sum += i
    i += 1 # 這邊i就是哨兵值(sentinel value)
print(sum)

#巢狀結構
#建立九九乘法表
i=1
while i <= 9:
    j=1
    while j <= 9:
        result = i*j
        print(f"{i}*{j}={result:<3d}",end="")
        j+=1
    print()
    i+=1

#建立購物車系統
products=["A","B","C","D","E"]
cart=[]
print(products,"\n")
while True: #用while true 是為了讓程式無限執行，直到我想讓他停止的條件成立為止
    msg=input("please choose the goods you want:")
    if msg == "q" or msg == "Q":
        break
    else:
        if msg in products:
            cart.append(msg)
        else:
            print("This good is not in our sell-list !")
print(cart)


#算等比級數
sum = 1
for i in range(64):
    sum += 2**i
print(sum)



































