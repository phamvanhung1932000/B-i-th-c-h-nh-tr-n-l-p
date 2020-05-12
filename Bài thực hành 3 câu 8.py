#8
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    #nếu hướng lên thì ta cộng 1 bước
    if direction=="UP":
        pos[0]+=steps
    #còn hướng xuống thì ta trừ 1 bước
    elif direction=="DOWN":
        pos[0]-=steps
    #còn nếu hướng sang trái thì ta trừ đi 1 bước
    elif direction=="LEFT":
        pos[1]-=steps
    #còn nếu hướng sang phải thì ta cộng đi 1 bước
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))