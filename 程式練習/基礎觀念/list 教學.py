x=[0,1,1,2,3,4,5,6,7,8,9]

#python的計數是從第0個開始
#x[x:y] 意思是從第x個到第y-1個
#x[:y] 意思是從第0個到第y-1個



#物件導向 objective oriented  x.y() x是物件 是要對前面這個物件做的事
x.append(333) #再list裡面加東西
print(x)

x.index() #用來搜尋list中的某個元素
x.count(11) #list中某個值出現的次數
x.extend() #將兩個list連在一起


#分割字串
str1 = "silicon stone education"
str2 = "D:\python\ch6"
slist1 = str1.split() #用空格當分割符號
slist2 = str2.split("\\")
slist1
slist2

#組合字串
path = ["D:","ch6","ch6_41.py"]
connect = "\\"
print(connect.join(path))
