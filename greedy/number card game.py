N, M = map(int, input().split())

result = 0

for n in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)


# 2중 반복문 구조 이용
# result = 0
#
# for n in range(N):      # 한 줄씩 입력받기
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = 10001   # 입력하는 수 1~10,000
#     for a in data:
#         min_value = min(min_value, a)
#     # '가장 작은 수'들 중 가장 큰 수 찾기
#     result = max(result, min_value)


print(result)