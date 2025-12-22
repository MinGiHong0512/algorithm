def check(a,b,c,x1,x2,y1,y2):
    
    minx, maxx = min(x1,x2) , max(x1,x2)
    miny, maxy = min(y1,y2) , max(y1,y2)

    if a == 0:
        if miny < -c/b < maxy:
            return "Poor"
        return "Lucky"

    if b == 0:
        if minx < -c/a < maxx:
            return "Poor"
        return "Lucky"

    if ((miny < -(a*minx + c)/b < maxy) or (miny < -(a*maxx + c)/b < maxy)) or((minx < -(b*miny+ c)/a < maxx) or (minx < -(b*maxy + c)/a < maxx)):
        return "Poor"
    return "Lucky"        

a,b,c =  map(int, input().split())
x1,x2,y1,y2 = map(int, input().split())

print(check(a,b,c,x1,x2,y1,y2))        