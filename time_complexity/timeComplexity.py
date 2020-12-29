from random import randint
import time

# 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교
# 선택 정렬 최악의 경우 O(N^2)
# 기본 정렬 라이브러리 최악의 경우 O(N*logN)


# 배열에 10,000개의 정수 랜덤값 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))    # 1부터 100 사이 랜덤 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

for i in range(len(array)):
    min_index = i # 가장 작은 원소 index
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]     # swap

end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정:", end_time-start_time) # 수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))   # 1부터 100 사이 랜덤 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()   # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time-start_time)    # 수행 시간 출력

