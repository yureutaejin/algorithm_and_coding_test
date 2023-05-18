import sys

# generator function
def generator(n):
    i = 1
    while i < n:
        yield i
        i += 1

if __name__ == '__main__':
    
    my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    
    # iterable한 my_list의 요소를 하나씩 출력. 하지만 my_list 내에 모두 넣어둬야하기 때문에 메모리 낭비
    for i in my_list:
        print(i)
    
    # 요소를 하나씩 출력하면서 함수의 상태를 유지하여 기준 값까지 계속하여 수행되도록 함. 하나씩 출력하기에 메모리 효율이 전자보다 높음.
    for x in generator(11):
        print(x)
    