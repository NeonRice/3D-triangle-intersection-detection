import numpy as np
import sys
from TriangleInteresects import tri_tri_intersect_with_isectline

# Examples


""" # No intersect
V0 = np.array([1.102, 7.440, 5.820])
V1 = np.array([8.507, 9.527, 6.819])
V3 = np.array([0.233, 3.748, 2.091])
U1 = np.array([8.503, 5.923, 5.588])
U2 = np.array([4.003, 7.255, 7.132])
U3 = np.array([6.163, 3.036, 9.676])

print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))

# Intersect
V0 = np.array([7.664, 8.061, 5.590])
V1 = np.array([2.576, 7.697, 2.495])
V3 = np.array([6.088, 2.811, 1.195])
U1 = np.array([3.712, 5.526, 1.875])
U2 = np.array([9.694, 8.396, 4.380])
U3 = np.array([8.589, 0.860, 1.667])

print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))

# Coplanar No intersect
V0 = np.array([1, 1, 0])
V1 = np.array([1, 5, 0])
V3 = np.array([4, 1, 0])
U1 = np.array([11, 1, 0])
U2 = np.array([11, 5, 0])
U3 = np.array([14, 1, 0])

print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))

# Coplanar Intersect
V0 = np.array([1, 1, 0])
V1 = np.array([1, 5, 0])
V3 = np.array([4, 1, 0])
U1 = np.array([2, 1, 0])
U2 = np.array([2, 5, 0])
U3 = np.array([5, 1, 0])

print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3)) """
""" print("false")
V0 = np.array([0.243, 0.393, 0.755])
V1 = np.array([0.434, 0.757, 0.958])
V2 = np.array([0.907, 0.029, 0.915])
U1 = np.array([0.891, 0.769, 0.822])
U2 = np.array([0.674, 0.832, 0.756])
U3 = np.array([0.622, 0.525, 0.231])
print(tri_tri_intersect_with_isectline(V0, V1, V2, U1, U2, U3))
V0 = np.array([0.198, 0.519, 0.325])
V1 = np.array([0.054, 0.393, 0.767])
V2 = np.array([0.749, 0.923, 0.525])
U1 = np.array([0.291, 0.009, 0.916])
U2 = np.array([0.962, 0.205, 0.598])
U3 = np.array([0.957, 0.391, 0.148])
print(tri_tri_intersect_with_isectline(V0, V1, V2, U1, U2, U3))
V0 = np.array([0.945, 0.860, 0.482])
V1 = np.array([0.353, 0.244, 0.013])
V2 = np.array([0.107, 0.780, 0.612])
U1 = np.array([0.007, 0.239, 0.987])
U2 = np.array([0.835, 0.034, 0.553])
U3 = np.array([0.368, 0.422, 0.815])
print(tri_tri_intersect_with_isectline(V0, V1, V2, U1, U2, U3))
V0 = np.array([0.910, 0.435, 0.392])
V1 = np.array([0.877, 0.168, 0.177])
V2 = np.array([0.582, 0.544, 0.749])
U1 = np.array([0.783, 0.932, 0.038])
U2 = np.array([0.093, 0.038, 0.898])
U3 = np.array([0.347, 0.700, 0.944])
print(tri_tri_intersect_with_isectline(V0, V1, V2, U1, U2, U3))
V0 = np.array([0.818, 0.430, 0.798])
V1 = np.array([0.380, 0.387, 0.626])
V2 = np.array([0.957, 0.793, 0.827])
U1 = np.array([0.220, 0.035, 0.617])
U2 = np.array([0.613, 0.523, 0.958])
U3 = np.array([0.379, 0.257, 0.425])
print(tri_tri_intersect_with_isectline(V0, V1, V2, U1, U2, U3))
print("true")
V0 = np.array([6.087, 4.020, 1.830])
V1 = np.array([6.921, 3.012, 3.967])
V3 = np.array([6.818, 9.713, 4.930])
U1 = np.array([5.352, 4.033, 5.671])
U2 = np.array([1.547, 8.536, 7.705])
U3 = np.array([7.832, 3.273, 0.601])
print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))
V0 = np.array([5.790, 9.870, 2.628])
V1 = np.array([6.572, 4.942, 1.053])
V3 = np.array([7.939 ,2.860, 1.922])
U1 = np.array([5.892 ,5.015, 4.031])
U2 = np.array([8.874, 9.951, 2.820])
U3 = np.array([0.054 ,5.089, 0.300])
print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))
V0 = np.array([2.122, 6.273, 3.155])
V1 = np.array([7.787, 0.959, 6.768])
V3 = np.array([0.618 ,6.558, 0.444])
U1 = np.array([0.911 ,1.869, 1.445])
U2 = np.array([2.562, 6.024, 9.916])
U3 = np.array([4.275 ,3.684, 1.813])
print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))
V0 = np.array([2.567, 6.464, 9.242])
V1 = np.array([3.936, 9.506, 1.128])
V3 = np.array([7.740 ,2.365, 2.224])
U1 = np.array([8.336 ,1.585, 2.203])
U2 = np.array([2.689, 4.811, 1.084])
U3 = np.array([6.166 ,3.953, 4.912])
print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))
V0 = np.array([8.761, 9.205, 3.480])
V1 = np.array([4.238, 5.150, 7.019])
V3 = np.array([1.680 ,4.242, 0.266])
U1 = np.array([7.164 ,8.976, 6.716])
U2 = np.array([8.464, 1.031, 7.496])
U3 = np.array([0.182 ,4.119, 3.625])
print(tri_tri_intersect_with_isectline(V0, V1, V3, U1, U2, U3))
 """
# I/O


def get_vertex_array(vertex_str):
    arr = vertex_str.split()

    if len(arr) != 3:
        sys.exit("Invalid vertex count, must be 3")

    return arr


def get_hand_input():
    print("1st Triangle")
    vin11 = input("Input 1st vertex coordinates (3 numbers):")
    V0 = (np.array(get_vertex_array(vin11))).astype(np.float)
    vin12 = input("Input 2nd vertex coordinates (3 numbers):")
    V1 = (np.array(get_vertex_array(vin12))).astype(np.float)
    vin13 = input("Input 3rd vertex coordinates (3 numbers):")
    V2 = (np.array(get_vertex_array(vin13))).astype(np.float)

    print("\n2nd Triangle")
    vin21 = input("Input 1st vertex coordinates (3 numbers):")
    U0 = (np.array(get_vertex_array(vin21))).astype(np.float)
    vin22 = input("Input 2nd vertex coordinates (3 numbers):")
    U1 = (np.array(get_vertex_array(vin22))).astype(np.float)
    vin23 = input("Input 3rd vertex coordinates (3 numbers):")
    U2 = (np.array(get_vertex_array(vin23))).astype(np.float)

    return [V0, V1, V2, U0, U1, U2]


def output_object_file(*vertices):
    RGB[0] = list(map(str, RGB[0]))
    RGB[1] = list(map(str, RGB[1]))

    triangleConnection = ["\n3 0 1 2 ", "\n3 3 4 5 "]
    space = " "
    triangleConnection[0] += space.join(RGB[0])
    triangleConnection[1] += space.join(RGB[1])

    with open(output_filename, "w") as file:
        if not file.writable:
            sys.exit("File is not writable...")

        file.write("OFF\n\n6 2 6\n")
        for vertice in vertices:
            file.write(space.join(vertice.astype(str)) + '\n')
        file.writelines(triangleConnection)


def input_object_file(input_filename):
    readArr = []
    with open(input_filename, "r") as file:
        if not file.readable:
            sys.exit("Given file is not readable...")

        lines = file.readlines()
        for line in lines:
            if len(line.split()) == 3:
                readArr.extend(line.split())

    entry = readArr[:3]
    if entry != ['6', '2', '6']:
        sys.exit("Incorrect OFF file formatting...")

    V0, V1, V2, U0, U1, U2 = readArr[3:6], readArr[6:9], readArr[9:
                                                                 12], readArr[12:15], readArr[15:18], readArr[18:21]
    V0, V1, V2, U0, U1, U2 = np.array(V0).astype(np.float), np.array(V1).astype(np.float), np.array(V2).astype(
        np.float), np.array(U0).astype(np.float), np.array(U1).astype(np.float), np.array(U2).astype(np.float)

    return [V0, V1, V2, U0, U1, U2]


def read_from_file(input_filename):
    vertices = []
    with open(input_filename, "r") as file:
        if not file.readable:
            sys.exit("Given file is not readable...")

        lines = file.readlines()

        if len(lines) != 6:
            "Bad txt file formatting..."

        for line in lines:
            vertice = line.split()

            if len(vertice) != 3:
                sys.exit("Bad txt file formatting...")

            vertices.append(vertice)

    return np.array(vertices).astype(np.float)


# Program entry

# Global declarations
RGB = [[255, 0, 0], [0, 0, 255]]
output_filename = "output.off"
input_filename = "input.off"
read_off = False

answer = input("Read from file? Y / N: ").upper()

if answer == 'N' or answer == 'Y':
    if answer == 'N':
        vertices = get_hand_input()
        print("Given triangles",  "intersect" if tri_tri_intersect_with_isectline(
            *vertices) else "do not intersect")
        output_object_file(*vertices)

    elif answer == 'Y':
        vertices = []
        if input_filename.endswith('.off'):
            vertices = input_object_file(input_filename)
        else:
            vertices = read_from_file(input_filename)
        print("Given triangles",  "intersect" if tri_tri_intersect_with_isectline(
            *vertices) else "do not intersect")
        output_object_file(*vertices)
else:
    sys.exit("Invalid input...")
