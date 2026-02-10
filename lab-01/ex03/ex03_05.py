def demsolanxuathien(lst):
    countdict={}
    for item in lst:
        if item in countdict:
            countdict[item]+=1
        else:
            countdict[item]=1
    return countdict
inputstr = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
wordlst=inputstr.split()
solanxh=demsolanxuathien(wordlst)
print("Số lần xuất hiện của các phần tử: ",solanxh)