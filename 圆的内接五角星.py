import math

# 从键盘上接收圆的半径
radius = float(input())

# 五角星示意图
# https://pic3.zhimg.com/80/v2-116cfc19c8a7a9964f569f81367ad626_720w.webp


# 计算内接五角星的一条全边长AC,AC=直径*cos(18°)
side_length = 2 * radius * math.cos(math.radians(18))


# r=(根号5-1)/2
# AC = 2R+R*(根号5-1)/2
# 得到R即图中b的长度
R=side_length/(2+(pow(5,0.5)-1)/2)


# 输出内接五角星的边长
print("{:.2f}".format(R))