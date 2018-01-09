from collections import deque

def operations(alist):
    q = deque()
    push = []
    p = []
    loc = 0
    pop = []
    #print a
    for i in range(len(alist)):
        while loc < alist[i]:
            loc += 1
            q.append((loc,"pushBack"))
            push.append("pushBack")
            q.appendleft((loc,"pushFront"))
            push.append("pushFront")
        #assert(c == a[i])
        if loc == alist[i]:
            z,s = q.pop()
            assert(z == alist[i])
            p.append(len(push)+len(p))
            continue
        if loc > alist[i]:
            if len(q) == 0:
                return "impossible"
            z,s = q.pop()
            while z != alist[i]:
                if len(q) == 0:
                    return "impossible"
                if s=="pushBack":
                    push[2*z-2] = -1
                else:
                    push[2*z-1] = -1
                z,s = q.pop()
            assert(z == alist[i])
            p.append(len(push)+len(pop))
    #assert(len(q) == 0)
    while len(q) > 0:
        z,s = q.pop()
        if s=="pushBack":
            push[2*z-2] = -1
        else:
            push[2*z-1] = -1

    assert(len(q)==0)
    pnew = deque(p)
    j = pnew.popleft()
    ans = []
    for i in range(len(push)):
        if i == j:
            ans.append("popBack")
            j = pnew.popleft()
        ans.append(push[i])
    ans.append("popBack")
    for _ in xrange(len(pnew)):
        ans.append("popBack")
    result = [x for x in ans if x != -1]
    return result

alist = [int(x) for x in raw_input().split(",")]
result = operations(alist)
if result == "impossible":
    print "impossible"
else:
    print ",".join(result)


#print(ops([3,4]))
