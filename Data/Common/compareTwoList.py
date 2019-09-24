#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
__author__ = 'zhanghaiyan'


#对比两个list或者元组是否相同，如果相同则返回True,如果有一个为空、或者不相同，则返回False
#支持字典列表

def islistequal(listA , listB ):
    if listA == listB:
        return True
    if listA==None and listB == None:
        return True
    if listA ==None or listB==None:
        return False
    if len(listA)!=len(listB):
        return False
    else:
        for x in listA:
            if x not in listB:
                return False
                print('不一致的地方：' + str(y))
        for y in listB:
            if y not in listA:
                print('不一致的地方：'+str(y))
                return False
        return True

#比较两个字典是否相同
b={'name':'zhy','age':30,'hasChildren':'N','sex':'female'}
c={'age':30,'name':'zhy','hasChildren':'Y','sex':'female'}
d={'age':30,'name':'zhy'}
f={'name':'zhy','sex':'male'}
j=[{'a':1,'b':2},{'a':1,'b':2}]  #j[0]和k[0] k[1]比较，当有相同时，j 索引加1  当没有相同且k 遍历完之后 返回False
k=[{'a':1,'b':2},{'c':3,'d':4}]
#print(islistequal(j,k))

#print([i for i in j if i not in k])
'''
if j == k:
    print('j=k')
if j == None and k == None:
    print('j=k')
if j == None or k == None:
    print('j<>k')
if len(j) != len(k):
    print('j<>k')
else:
    for x in j:
        if x not in k:
            print('j<>k')
            print('不一样的地方：%s') % x
    for y in k:
        if y not in j:
            print('j<>k')
            print('不一样的地方：%s') % x

for x in range(len(j)):
    for y in range(len(k)):
        if islistequal(j[x],k[y]):#0 0 #0 1 # 0 2
            print('y')
        else:
            print('n')


x=['6280619071815619', 'ba665bbb-3e5b-4686-9fcd-77afe437bc3d', '宁波市', '合肥市']
y=['6280619071815619', '宁波市', '合肥市', 'ba665bbb-3e5b-4686-9fcd-77afe437bc3d']
a=islistequal(x,y)
print(a)



            for i, j in listA.items():
                if i in listB:
                    if j != listB[i]:
                        print(' value  not in B ,value:' + j)
                        return False
                else:
                    print(' key not in B ,key:'+i)
                    return False



'''