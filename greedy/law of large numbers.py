# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input("N, M, K를 입력하세요: ").split())
# N개의 수를 공백으로 구분하여 입력받기
n_data = list(map(int, input("N개의 자연수를 입력하세요: ").split()))

# 입력받은 수 정렬하기
n_data.sort()
largest = n_data[N-1]   # 가장 큰 수
second = n_data[N-2]    # 두 번째 큰 수

result = 0

'''
while True:
    for i in range(K):      # 가장 큰 수를 K번 더하기
        if M == 0:
            break
        result += largest
        M -= 1
    if M == 0:
        break
    result += second    # 두 번째 큰 수를 한 번 더하기
    M -= 1
'''

count = int(M/(K+1))*K  # 가장 큰 수가 더해지는 횟수 계산
count += M % (K+1)     # M이 K+1로 나누어떨어지지 않는 경우 나머지

result += count * largest   # 가장 큰 수
result += (M-count) * second    # 두 번째 큰 수

print(result)   # 최종 답
