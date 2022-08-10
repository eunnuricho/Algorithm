A, B, V = map(int, input().split())
ans = 0

# (V - B) -> 다 올라갔을 때 오르는 거리, (A - B) -> 하루에 오르는 거리
if (V - B) % (A - B) != 0: #나누어 떨어지지 않으므로 하루 더 필요
    ans = ((V - B) // (A - B)) + 1
else: #낮에 다 오르고 밤에 미끄러지지 않음
    ans = ((V - B) // (A - B))

print(ans)