a = [1,2,3, [10,11,12]]
print(a[1] + a[2])
print(a[3][2])

# 음수를 넣으면 뒤에서부터 센다.
print(a[-1])

# list slicing (0 이상, 2 미만)
print(a[0:2])

# 3번째 수는 간격을 말함
print(a[0::2])

# f-string 수식: 문자열 앞에 f를 붙이고, {} 안에 파이썬 수식을 넣는 방식
print(f"length: {len(a)}")

list = ['a','b','c','d','e']
del(list[1]) # 2번째 element 삭제
del(list[3:]) # 3번째부터 그 뒤까지 전부 삭제
list.append('f') # 새로운 요소 뒤에 추가 (list도 추가 가능)
list.insert(0, 'h') # 원소 삽입
list.reverse() # 배열 뒤집기

print(list.index('a')) # 2번째에 있는 index 리턴
print(list.pop()) # 리스트의 맨 마지막에 있는 요소를 리턴하고 해당 요소 삭제, argument에서 특정 index 삽입할 수도 있음

# extend vs append
list1 = [1,2,3]
list1.append([4,5])
print(f"append: {list1}")

list1.extend([4,5])
print(f"extend: {list1}")
