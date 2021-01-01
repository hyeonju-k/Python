# until 1
# N-1 or N/K

N, K = map(int, input().split())

result = 0

# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
while True:
    # (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // K) * K
    result += (N-target)
    N = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N<K:
        break
    result += 1
    N //= K

# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (N-1)



# 나의 답안
# while N > 1:
#     if N % K == 0:
#         N //= K
#     else:
#         N -= 1
#     result += 1

# 단순하게 푸는 답안
# N이 K 이상이라면 K로 계속 나누기
# while N >= K:
#     # N이 K로 나누어 떨어지지 않는다면 N에서 1빼기
#     while N % K != 0:
#         N -= 1
#         result += 1
#     # K로 나누기
#     N //= K
#     result += 1
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# while N > 1:
#     N -= 1
#     result += 1

print(result)