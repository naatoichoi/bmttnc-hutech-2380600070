import re
s = "-100#^sdfkj8902w3ir021@swf-20"
numbers = re.findall(r'-?\d+', s)
sum_positive = 0
sum_negative = 0
for num in numbers:
    n = int(num)
    if n > 0:
        sum_positive += n
    elif n < 0:
        sum_negative += n
print("Giá trị dương:", sum_positive)
print("Giá trị âm:", sum_negative)
