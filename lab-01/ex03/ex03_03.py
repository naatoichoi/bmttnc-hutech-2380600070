def taotupletulist(lst):
    return tuple(lst)
inputlst = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers=list(map(int, inputlst.split(',')))
mytuple=taotupletulist(numbers)
print("List: ",numbers)
print("Tuple từ List: ",mytuple)