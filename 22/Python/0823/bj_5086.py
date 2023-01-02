while True:
    _target, num = map(int, input().split())
    if _target == 0 and num == 0:
        break

    if _target > num and _target % num == 0:  # target이 num의 배수인지 확인
        print('multiple')

    elif num % _target == 0:  # target이 num의 약수인지 확인
        print('factor')

    else:
        print('neither')
