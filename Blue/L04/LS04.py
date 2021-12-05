from collections import deque

tc = 1
while True:
    P, C = map(int, input().split())
    if P == 0 and C == 0:
        break

    q = deque()
    for i in range(1, min(P, C) + 1):
        q.append(i)

    print('Case {}:'.format(tc))
    tc += 1

    for _ in range(C):
        command = input().split()
        cmd = command[0]
        if cmd == "N":
            print(q[0])
            q.append(q.popleft())
        else:
            n = len(q)
            priority = int(command[1])
            q.append(priority)
            for i in range(n):
                tmp = q.popleft()
                if tmp != priority:
                    q.append(tmp)
