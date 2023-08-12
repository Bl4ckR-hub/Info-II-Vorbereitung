def frame_check():
    c = [1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0]
    g = [1,1,1,0,1,0,1,0,1]
    n = len(c)-8

    while(n > 0):
        print(c)
        if (not bool(c[0])):
            c.remove(0)
        else:
            for i in range(len(g)):
                c[i] = int(bool(c[i])^bool(g[i]))
            c.remove(0)
        n -= 1
    
frame_check()