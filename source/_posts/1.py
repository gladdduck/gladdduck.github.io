# 原字典
dt1={"BJ":"CHN","CA": "US","SH":"CHN","TW":"CHN","NY":"US","ON": "CA"}
# 新字典
new_dict={}

# 对老字典的每一个键值对,比如  "BJ":"CHN"
for k,v in dt1.items():
    # 如果值还没加进新字典里,就把值加进去
    if v not in new_dict:
        new_dict[v]=[]
    # 把键追加到值的列表里
    new_dict[v].append(k)
# 输出新字典
print(new_dict)