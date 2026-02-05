def daolist(lst):
    return lst[::-1]
inputlst = input ("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputlst.split(',')))
listdaonguoc=daolist(numbers)
print("List sau khi đảo ngược: ",listdaonguoc)