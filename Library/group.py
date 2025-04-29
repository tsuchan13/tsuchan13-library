from itertools import combinations

def partition(lst):
    """リストのすべての可能なグループ分けを生成する"""
    if not lst:
        return [[]]
    
    first = lst[0]
    rest_partitions = partition(lst[1:])
    
    result = []
    
    for part in rest_partitions:
        # 既存のグループに first を追加
        for i in range(len(part)):
            new_partition = part[:i] + [part[i] + [first]] + part[i+1:]
            result.append(new_partition)
        
        # first を新しいグループとして追加
        result.append([[first]] + part)
    
    return result