def truycapphantu(tupledata):
    firstelement=tupledata[0]
    lastelement=tupledata[-1]
    return firstelement,lastelement
inputtuple = eval(input("Nhập tuple, ví dụ (1,2,3): "))
first, last = truycapphantu(inputtuple)
print("Phần tử đầu tiên: ",first)
print("Phần tử cuối cùng: ", last)