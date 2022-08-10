kilos = int(input())

cnt = 0

while kilos >= 0:
    if kilos % 5 == 0: #5로 나눌 수 있으면 몫만큼 5키로 봉지를 가져감
        cnt += (kilos // 5)
        print(cnt)
        break
    kilos -= 3 #나눠지지 않으면 3키로 봉지를 가져감
    cnt += 1

else:
    print(-1)