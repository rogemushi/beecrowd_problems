import math 

x = str(input())
y = str(input())

x_all = x.split(" ")
y_all = y.split(" ")

x1 = float(x_all[0])
x2 = float(x_all[1])

y1 = float(y_all[0])
y2 = float(y_all[1])


p1_x = (x1 - y1)**2
p2_y = (x2 - y2)**2
somas = p1_x + p2_y

resposta = math.sqrt(somas)

print(f"{resposta:.4f}")