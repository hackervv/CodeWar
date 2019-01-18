import math
def in_array(array1,array2):
    """ Give two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2 """
    res = []
    for item1 in array1:
        for item2 in array2:
            if item1  in item2 and item1 not in res:
                res.append(item1)
    res.sort()
    return res

def notin_array(arr):
    """ Find which one is miss in the list of int """
    return (arr[0] + arr[-1]) * (len(arr) + 1)/2 - sum(arr)


# sring1 in string2: 返回string1是否为sring2的子字符串
# list.sort(key=None,reverse=False):list根据key来排序，reverse为Ture为降序，False为升序
arr = [1,3,5,7,9,13]
print(notin_array(arr))
array1 = ['haha','hehe','23123','832']
array2 = ['hehehe','hahahahaha','hahahahah','2312399','83254','1231']
print(in_array(array1,array2))
