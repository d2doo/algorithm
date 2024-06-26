import sys
input = sys.stdin.readline

# N = int(input()) # 용액 수
# liquid = []
#
# for _ in range(N):
#     liquid.append(int(input()))
#
# liquid.sort() # 필수
# result = [0, 0, 0]
# now = float('inf')
#
# for i in range(N-2):
#     start = i + 1 # start point
#     end = N - 1 # end point
#
#     while start < end: # 만날때까지
#         # 절대값 계산 abs()
#         summ = liquid[start] + liquid[end] + liquid[i]
#         if abs(summ) < abs(now):
#             result = [liquid[i], liquid[start], liquid[end]]
#             now = summ
#
#         if summ > 0: # 양수면 제일 큰 숫자 하나 줄여보고
#             end -= 1
#         elif summ < 0: # 음수면 제일 작은 숫자 하나 늘려보고
#             start += 1
#         else:
#             break
# print(*result)

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = sys.maxsize
three = []
for i in range(N-2):
    left = i+1
    right = N-1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        if abs(temp) < result:
            result = abs(temp)
            three = [arr[i], arr[left], arr[right]]
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            break

print(*three)