hour, minute = map(int, input().split())
time = int(input())

_hour, _minute = time // 60, time % 60
hour += _hour
minute += _minute

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)