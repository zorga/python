def main():
    t = int(raw_input().strip())
    for i in range(t):
        n, k = raw_input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = map(int, raw_input().strip().split(' '))
        # 'a' is the list of arrival times
        # 'k' is the cancelation threshold

        # check whether the constraints are respected or not :
        assert 1 <= t <= 10
        assert 1 <= n <= 1000
        assert 1 <= k <= n
        for e in a:
            assert -100 <= e <= 100

        # if constraints are ok :
        count = 0
        for e in a:
            if e <= 0: 
                count = count + 1
            else:
                pass
        
        if (count < k):
            print("YES")
        else:
            print("NO")
    
    

if __name__ == '__main__':
    main()
