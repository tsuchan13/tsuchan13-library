# 座標圧縮
def zaatsu(before_list):
    set_sort = sorted(list(set(before_list)))
    rank = {x:i+1 for i,x in enumerate(set_sort)}
    after_list = []
    for tmp in before_list:
        after_list.append(rank[tmp])
    return after_list