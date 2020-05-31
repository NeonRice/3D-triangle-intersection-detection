import numpy as np
import math

# Global declarations
RGB = [[], []]
output_filename = ""
input_filename = ""

# Algorithm starts here


def isect2(VTX0, VTX1, VTX2, VV0, VV1, VV2, D0, D1, D2, isect0, isect1, isectpoint0, isecpoint1):
    tmp = D0 / (D0 - D1)
    diff = [0, 0, 0]
    isect0 = VV0 + (VV1 - VV0) * tmp

    diff = VTX1 - VTX0
    diff[0] = tmp * diff[0]
    diff[1] = tmp * diff[0]
    diff[2] = tmp * diff[0]

    isectpoint0 = np.add(diff, VTX0)
    tmp = D0 / (D0 - D2)
    isect1 = VV0 + (VV2 - VV0) * tmp
    diff = VTX2 - VTX0

    diff[0] = tmp * diff[0]
    diff[1] = tmp * diff[0]
    diff[2] = tmp * diff[0]

    isectpoint1 = np.add(VTX0, diff)

    return isect0, isect1, isectpoint0, isectpoint1


def compute_intervals_isectline(VERT0, VERT1, VERT2, VV0, VV1, VV2, D0, D1, D2, D0D1, D0D2, isect0, isect1, isectpoint0, isectpoint1):
    if D0D1 > 0.0:
        return isect2(VERT2, VERT0, VERT1, VV2, VV0, VV1, D2, D0, D1, isect0, isect1, isectpoint0, isectpoint1), False
    elif D0D2 > 0.0:
        return isect2(VERT1, VERT0, VERT2, VV1, VV0, VV2, D1, D0, D2, isect0, isect1, isectpoint0, isectpoint1), False
    elif D1 * D2 > 0.0 or D0 != 0.0:
        return isect2(VERT0, VERT1, VERT2, VV0, VV1, VV2, D0, D1, D2, isect0, isect1, isectpoint0, isectpoint1), False
    elif D1 != 0.0:
        return isect2(VERT1, VERT0, VERT2, VV1, VV0, VV2, D1, D0, D2, isect0, isect1, isectpoint0, isectpoint1), False
    elif D2 != 0.0:
        return isect2(VERT2, VERT0, VERT1, VV2, VV0, VV1, D2, D0, D1, isect0, isect1, isectpoint0, isectpoint1), False
    else:
        # triangles are coplanar
        return (isect0, isect1, isectpoint0, isectpoint1), True
    return False


def edge_edge_test(V0, U0, U1, i0, i1, Ax, Ay):
    Bx = By = Cx = Cy = f = d = e = 0.0
    By = U0[i0] - U1[i0]  # B = U0 - U1 (projected onto the i0-i1 plane)
    Bx = U0[i1] - U1[i1]
    Cx = V0[i0] - U0[i0]  # C = V0 - U0 (projected onto the i0-i1 plane)
    Cy = V0[i1] - U0[i1]

    # if the edges intersect, |f| is half the area of the convex quadrilateral spanned by the vertices
    f = Ay * Bx - Ax * By
    # if the edges intersect, |d| is half the area of the triangle U0, U1, V0
    d = By * Cx - Bx * Cy
    if (f > 0 and d >= 0 and d <= f) or (f < 0 and d <= 0 and d >= f):
        # if edges intersect, |e| is half the area of the triangle V0, V1, U0
        e = Ax * Cy - Ay * Cx
        if f > 0:
            if e >= 0 and e <= f:
                return True
        else:
            if e <= 0 and e >= f:
                return True
    # all vertices are colinear if f == 0 and d == 0, but for some reason this is not tested here ???
    return False


def edge_against_tri_edge(V0, V1, U0, U1, U2, i0, i1):
    Ax = Ay = 0.0  # coordinates of the edge relative to V0

    Ax = V1[i0] - V0[i0]
    Ay = V1[i1] - V0[i1]

    # test intersection of edge U0, U1 with edge V0, V1
    if edge_edge_test(V0, U0, U1, i0, i1, Ax, Ay):
        return True
    if edge_edge_test(V0, U1, U2, i0, i1, Ax, Ay):
        return True
    if edge_edge_test(V0, U2, U0, i0, i1, Ax, Ay):
        return True
    return False


def point_in_tri(V0, U0, U1, U2, i0, i1):
    a = b = c = d0 = d1 = d2 = 0.0
    # is T1 completely inside T2?
    # check if V0 is inside tri(U0, U1, U2)

    a = U1[i1] - U0[i1]
    b = -(U1[i0] - U0[i0])
    c = -a * U0[i0] - b * U0[i1]
    d0 = a * V0[i0] + b * V0[i1] + c

    a = U2[i1] - U1[i1]
    b = -(U2[i0] - U1[i0])
    c = -a * U1[i0] - b * U1[i1]
    d1 = a * V0[i0] + b * V0[i1] + c

    a = U0[i1] - U2[i1]
    b = -(U0[i0] - U2[i0])
    c = -a * U2[i0] - b * U2[i1]
    d2 = a * V0[i0] + b * V0[i1] + c

    if d0 * d1 > 0.0:
        if d0 * d2 > 0.0:
            return True
    return False


def coplanar_tri_tri(N, V0, V1, V2, U0, U1, U2):
    A = np.array([0.0, 0.0, 0.0])
    i0 = i1 = 0
    # first project onto an axis-aligned plane that maximizes the area
    # of the triangles, compute indices: i0, i1.
    A[0] = math.fabs(N[0])
    A[1] = math.fabs(N[1])
    A[2] = math.fabs(N[2])

    if A[0] > A[1]:
        if A[0] > A[2]:
            i0 = 1
            i1 = 2
        else:
            i0 = 0
            i1 = 1
    else:
        if A[2] > A[1]:
            i0 = 0
            i1 = 1
        else:
            i0 = 0
            i1 = 2

    if edge_against_tri_edge(V0, V1, U0, U1, U2, i0, i1):
        return True
    if edge_against_tri_edge(V1, V2, U0, U1, U2, i0, i1):
        return True
    if edge_against_tri_edge(V2, V0, U0, U1, U2, i0, i1):
        return True

    # finally, test if tri1 is totally contained in tri2 or vice versa

    if point_in_tri(V0, U0, U1, U2, i0, i1):
        return True
    if point_in_tri(U0, V0, V1, V2, i0, i1):
        return True
    return False


def tri_tri_intersect_with_isectline(V0, V1, V2, U0, U1, U2):

    # Initializing empty np.arrays
    E1 = np.zeros(shape=3)
    E2, N1, N2, D = np.zeros_like(E1), np.zeros_like(
        E1), np.zeros_like(E1), np.zeros_like(E1)

    isect1, isect2 = np.zeros(shape=(2)), np.zeros(shape=(2))
    isectpointA1, isectpointA2, isectpointB1, isectpointB2 = np.zeros_like(
        E1), np.zeros_like(E1), np.zeros_like(E1), np.zeros_like(E1)

    du0du1 = du0du2 = dv0dv1 = dv0dv2 = 0.0
    d1 = d2 = du0 = du1 = du2 = dv0 = dv1 = dv2 = 0.0
    vp0 = vp1 = vp2 = up0 = up1 = up2 = 0.0
    b = c = maxVal = 0.0
    index = 0

    # compute plane equation of triangle (V0, V1, V2)
    E1 = V1 - V0
    E2 = V2 - V0
    N1 = np.cross(E1, E2)
    # normalization?
    d1 = -np.dot(N1, V0)
    # plane equation 1: N1.X + d1 = 0

    # put U0, U1, U2 into plane equation 1 to compute signed distances to the plane
    du0 = np.dot(N1, U0) + d1
    du1 = np.dot(N1, U1) + d1
    du2 = np.dot(N1, U2) + d1

    du0du1 = du0 * du1
    du0du2 = du0 * du2

    if du0du1 > 0.0 and du0du2 > 0.0:
        return False

    # compute plane of triangle U0, U2, U2
    E1 = U1 - U0
    E2 = U2 - U0
    N2 = np.cross(E1, E2)
    # normalization?
    d2 = -np.dot(N2, U0)

    # plane equation 2: N2.X+d2=0

    # put V0, V1, V2 into plane equation 2
    dv0 = np.dot(N2, V0) + d2
    dv1 = np.dot(N2, V1) + d2
    dv2 = np.dot(N2, V2) + d2

    dv0dv1 = dv0 * dv1
    dv0dv2 = dv0 * dv2

    if dv0dv1 > 0.0 and dv0dv2 > 0.0:
        return False

    # compute direction of intersection line
    D = np.cross(N1, N2)
    # compute index into the largest component of D
    maxVal = math.fabs(D[0])
    b = math.fabs(D[1])
    c = math.fabs(D[2])
    if b > maxVal:
        maxVal = b
        index = 1
    if c > maxVal:
        maxVal = c
        index = 2

    # Projection onto athe axis correspoding to index
    # This corresponds to projection onto x, y, or z, whichver is closer to the direction of isectline D
    vp0, vp1, vp2, up0, up1, up2 = V0[index], V1[index], V2[index], U0[index], U1[index], U2[index]

    res, coplanar = compute_intervals_isectline(
        V0, V1, V2, vp0, vp1, vp2, dv0, dv1, dv2, dv0dv1, dv0dv2, isect1[0], isect1[1], isectpointA1, isectpointA2)
    isect1[0], isect1[1], isectpointA1, isectpointA2 = res

    """ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
    !!!!!!!  at this point we know whether the triangles are coplanar  !!!!!!!! 
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! """

    if coplanar:
        return coplanar_tri_tri(N1, V0, V1, V2, U0, U1, U2)

    # compute interval for triangle 2
    res, coplanar = compute_intervals_isectline(
        U0, U1, U2, up0, up1, up2, du0, du1, du2, du0du1, du0du2, isect2[0], isect2[1], isectpointB1, isectpointB2)
    isect2[0], isect2[1], isectpointB1, isectpointB2 = res

    isect1.sort()
    isect2.sort()

    if isect1[1] < isect2[0] or isect2[1] < isect1[0]:
        return False

    """ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
    !!!!!!!  at this point we know that the triangles intersect   !!!!!!!! 
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  """

    return True
