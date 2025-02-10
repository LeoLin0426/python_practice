for i in range(0, 2): #python的範圍是半閉區間 右開
    print(i)

#計算等差級數，從1加到n
n=int(input("輸入n:"))
sum=0
for i in range(1,n+1):
    sum += i
    
print(sum)


#用迴圈產生list
#1. 若不使用迴圈
xlist=[]
xlist.append(0)
xlist.append(1)
xlist.append(2)
xlist.append(3)
xlist.append(4)
xlist.append(5)
xlist

#2.使用迴圈方式
xlist = []
for i in range(0,6):
    xlist.append(i)

xlist

#3. 用list generator的觀念
xlist = [n for n in range(0,6)]
xlist

#含條件的for 迴圈
#1.建立篩選出奇數的list
oddlist = []
num = int(input("輸入任意數:"))
for i in range(1,num + 1):
    if i % 2 ==1:
        oddlist.append(i)      
oddlist

#2. 建立篩選出奇數的list(進階)
num = int(input("輸入任意數:"))
oddlist = [i for i in range(1,num+1) if i % 2 == 1]
oddlist


#畢氏定理
x=[[a,b,c]
   for a in range(1,20)
   for b in range(a,20) 
   for c in range(b,20) 
   if a**2 + b**2 == c**2]
x
#傳統迴圈(巢狀)
x=[]
for a in range(1,20):
    for b in range(a,20):
        for c in range(b,20):
            if a**2 + b**2 == c**2:
                x.append([a,b,c])
x


#巢狀迴圈印出九九乘法
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print(f"{i}*{j}={result:<3d}",end="") #f""表示接下來是一個 f-string
    print()
# =============================================================================
# #f-string 是 Python 3.6 引入的一種字串格式化方式，
# #它讓你在字串中直接嵌入變數或運算式，使得字串的格式化變得更加直觀和簡潔。
# 
# #:<3d:
# #:：表示接下來是格式說明符。
# #3：指定輸出寬度為 3 個字符。
# #d：表示輸出的是一個十進位整數
# =============================================================================

#設立條件使判斷迴圈要不要繼續執行下去
#若符合條件，則之後的程式碼不用執行，直接跑下一個element
# example
for i in range(1, 6):
    if i == 3:
        continue  # 當 i 等於 3 時，跳過本次循環的剩餘部分
    print(i)



# =============================================================================
# for item in iterable:
#     # 迴圈中的程式碼
#     if condition:
#         break
# else:
#     # 如果迴圈正常結束，執行這裡的程式碼
# 
# =============================================================================
#example
#有找到數字3
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("找到了數字 3")
        break
else:
    print("沒有找到數字 3")
    
# 3 not found
numbers = [1, 2, 4, 5]
for num in numbers:
    if num == 3:
        print("找到了數字 3")
        break
else:
    print("沒有找到數字 3")




















