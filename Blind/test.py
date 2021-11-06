def timer():
    global timeTotal
    timeTotal = 15
    while timeTotal:
        timer = '{:02d}'.format(timeTotal)
        print(timer, end="\r")
        time.sleep(1)
        timeTotal -= 1
    print('Game Over!!!')