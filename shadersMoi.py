import math
from mathLib import dotProduct

def dcHalf(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width

    angle = math.atan2(newX - 0.5, newY - 0.5)

    angle2 = math.atan2(newX - 0.5, newY - 0.6)
    angle2 /= -math.pi * 4
    angle2 += 0.5

    if newY > 0.56:
        intensity *= angle 
        intensity %= 1
        b, g, r = 1, 1, 0
    else:
        b, g, r = 1, 1, 1
    
    b *= (intensity )
    g *= (intensity )
    r *= (intensity )
    

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def piShadow(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width

    angle = math.atan2(newX - 0.5, newY - 0.6)
    angle /= -math.pi * 4
    angle += 0.5

    if newY > 0.1:
        intensity *= angle         
        b, g, r = 1, 1, 0
    else:
        b, g, r = 1, 1, 0
    
    if intensity <= 1:
        b *= (intensity )
        g *= (intensity )
        r *= (intensity )
    

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def dcCombined(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width

    angle = math.atan2(newX - 0.5, newY - 0.5)

    angle2 = math.atan2(newX - 0.5, newY - 0.6)
    angle2 /= -math.pi * 4
    angle2 += 0.5

    if newY > 0.56:
        intensity *= angle 
        intensity %= 1
        b, g, r = 1, 1, 0
    else:
        intensity *= angle2
        b, g, r = 1, 1, 0
    
    b *= (intensity )
    g *= (intensity )
    r *= (intensity )
    

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def sqrEffect(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width
    
    intensity *=  float(((newX*20)//1)/20) 
    intensity *=  ((newY*20)//1)/20


    b, g, r = 1, 1, 0
    
    b *= (intensity *3.1)
    g *= (intensity *3.1)
    r *= (intensity *3.1)
    

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gradient(render, **kwargs):
    
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width

    b, g, r = newX, (newY), 0
    
    b *= (intensity) 
    g *= (intensity) 
    r *= (intensity) 

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gradientMounts(render, **kwargs):
    
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    x = kwargs["xValue"]
    y = kwargs["yValue"]

    b /= 255
    g /= 255
    r /= 255

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    newY = y/render.height
    newX = x/render.width

    b, g, r = newX, newY, 0

    intensity *=  1 - (newX * 45) % 0.4 
    
    b *= (intensity) 
    g *= (intensity) 
    r *= (intensity) 

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0