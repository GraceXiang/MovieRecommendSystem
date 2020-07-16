import itertools
list1=['科幻', '悬疑', '喜剧']
res_list=[]
for i in range(1,len(list1)+1):
    iter = itertools.permutations(list1,i)
    res_list.append(list(iter))
res=[]
for item in res_list:
    for i in item:
        if len(item)==1:
            res.append("".join(i))
        else:
            res.append("/".join(i))
print(res)