def xoaphantu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
mydict={'a': 1, 'b': 2, 'c': 3, 'd': 4}
keytodl='b'
result=xoaphantu(mydict,keytodl)
if result:
    print("Phần tử đã được xoá từ Dictionary: ",mydict)
else:
    print("Không tìm thấy phần tử cần xoá trong Dictionary")