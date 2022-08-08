A = int(input())
B = int(input())
C = int(input())

cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

output = str(A * B * C)

for i in range(len(output)):
    if output[i] == '0':
        cnt_0 += 1
    elif output[i] == '1':
        cnt_1 += 1
    elif output[i] == '2':
        cnt_2 += 1
    elif output[i] == '3':
        cnt_3 += 1
    elif output[i] == '4':
        cnt_4 += 1
    elif output[i] == '5':
        cnt_5 += 1
    elif output[i] == '6':
        cnt_6 += 1
    elif output[i] == '7':
        cnt_7 += 1
    elif output[i] == '8':
        cnt_8 += 1
    elif output[i] == '9':
        cnt_9 += 1

print(cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9, sep='\n')

#count
# output = list(str(A * B * C))
# 
# for i in range(10):
#     print(output.count(str(i)))
