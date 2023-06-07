import math

def Formulasi():
    global L1, L2, L3
    global h, Z
    global X, Y, theta1
    global c3, s3, s3a, theta3
    global theta2
    global T1a, T2a, T3a
    global T1, T2, T3

    L1 = 85     # mm
    L2 = 165    # mm
    L3 = 155    # mm

    # Formulasi Invers Kinematics Robot Manipulator
    theta1 = math.atan2(Y, X)    # Radian

    h = Z - L1  # mm    # This is for theta3
    c3 = (X*X + Y*Y + h*h - L2*L2 - L3*L3) / (2*L2*L3)  # This is cos theta 3
    s3 = -math.sqrt(1 - c3*c3)  # For down elbow
    s3a = math.sqrt(1 - c3*c3)  # For up elbow
    theta3 = math.atan2(s3, c3) # Radian

    alfa = math.atan2(h , math.sqrt(X*X + Y*Y))
    beta = math.atan2(math.sin(math.acos(c3)) * L3, L2 + math.cos(math.acos(c3)) * 155)
    theta2 = alfa + beta

    T1a = theta1 * 180.0 / math.pi  # Degree    # T1a is theta1 in Degree
    T2a = theta2 * 180.0 / math.pi  # Degree    # T2a is theta2 in Degree
    T3a = theta3 * 180.0 / math.pi  # Degree    # T3a is theta3 in Degree

    
    T1 = 510 + (T1a / 0.29297)
    T2 = 204 + (T2a / 0.29297)
    T3 = 460 + (T3a / 0.29297)

X = 240
Y = 80
Z = 15

Formulasi()



print("T1a : %d" % (T1a))
print("T2a : %d" % (T2a))
print("T3a : %d" % (T3a))

print("T1 : %d" % (T1))
print("T2 : %d" % (T2))
print("T3 : %d" % (T3))