def boo(*arg):
    return arg
def foo(**kwarg):
    return kwarg

dic=foo()
dic['kwarg']={'name1': 'moses', 'name2': 'HAKIM', 'name3': 'CAESAR'}
elem=dic['kwarg'].__len__()
print(str(elem)+ ' elements')
for i,j in dic['kwarg'].items():
    print(i,':',j)

lt=boo()
lt=[1,(1,2),'name1','moses',45]
elem=lt.__len__()
len(lt)
print(str(elem)+ ' elements')
for i in lt[1]:
    print(i)
for i in lt:
    print(i)

list1=['first name','second name']
list2=['Moses','Hakim']
for i,j in enumerate(list1):
    print(i,'',j)

for i,j in zip(list1,list2):
    print(i,'',j)

for i in range(len(list1)):
    print(i,'',list1[i])

list1=[('first name','second name')]
list2=[('Moses','Hakim')]  
l=list1+list2
for i in l:
    print(i,':')





    
    
