
lst=[]
ip=int(input('no of ip to be inserted'))
for i in range(ip):
        a=int(input())
        lst.append(a)
print("the list is :",lst)
length=len(lst)
def large(lst,length):
        if length==0:
                return lst[0]
        return max(lst[length-1],large(lst,length-1))
# [6,0,2,8,9]
# length is 5
# if length is 0 returns first element
# else max(9,large(lst,4))=>max(9,8,large(lst,3))=>.........max(9,8,2,0,6)=>9

                

b=large(lst,length)
print('the largest array element is ',b)

