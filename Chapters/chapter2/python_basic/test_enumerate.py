import pprint

if __name__ == '__main__':
    a = [1, 2, 3, 2, 45, 2, 5]
    print(enumerate(a))
    print(list(enumerate(a)))
    
    for i, v in enumerate(a):
        print(i, v)
        
    print()
    pprint.pprint(locals())