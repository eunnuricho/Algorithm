_input = input()
cnt = 0
flag = False

for i in range(len(_input)):
    #공백이 아닌 문자일 때
    if _input[i] != ' ':
        flag = True
    #문자가 있다가 공백이 생겼을 때
    elif _input[i] == ' ' and flag == True:
        cnt += 1
        #False로 되돌림
        flag = False

#공백으로 끝난 경우
if flag == False:
    print(cnt)
#문자로 끝난 경우
else:
    print(cnt + 1)

#
# _input = input().split()
# print(len(_input))