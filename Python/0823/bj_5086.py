while True:
    _target, num = map(int, input().split())
    if _target == 0 and num == 0:
        break

    if _target > num:  # target이 num의 배수인지 확인
        if _target % num == 0:
            print('multiple')
        else:
            print('neither')

    else:  # target이 num의 약수인지 확인
        if num % _target == 0:
            print('factor')
        else:
            print('neither')
