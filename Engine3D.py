from pyexpat import model
from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend, newS, barcodeEffect, justC, flatty, flatNcolor, squaredEffect, squaresNgradient, gouradyy
from shadersMoi import dcHalf, piShadow, dcCombined, sqrEffect, gradient, gradientMounts



# Photoshoot - My favs
def favsPhotoshoot():
    rend = Renderer(960, 540)
    rend.active_shader = sqrEffect
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))

    rend.active_shader = gradientMounts
    rend.glLoadModel("models/model.obj",
                    translate = V3(6, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))

    rend.active_shader = gradient
    rend.glLoadModel("models/model.obj",
                    translate = V3(-6, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))

    rend.glFinish("outputs/myFavsPhotoshoot.bmp")

def sqrsEffect():
    rend = Renderer(960, 540)
    rend.active_shader = sqrEffect
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/sqrsEffect.bmp")

def gradientM():
    rend = Renderer(960, 540)
    rend.active_shader = gradientMounts
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/gradientMounts.bmp")

def gradientShader():
    rend = Renderer(960, 540)
    rend.active_shader = gradient
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/gradientShader.bmp")

def dcHalfShader():
    rend = Renderer(960, 540)
    rend.active_shader = dcHalf
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/dcHalf.bmp")

def piShadowShader():
    rend = Renderer(960, 540)
    rend.active_shader = piShadow
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/piShadow.bmp")

def dcCombinedShader():
    rend = Renderer(960, 540)
    rend.active_shader = dcCombined
    rend.glLoadModel("models/model.obj",
                    translate = V3(0, 0, -10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/dcCombined.bmp")


def menu():
    print('\nLab 2 - Graficas\n\nOpciones:\n1. Squares Effect \
           \n2. Gradient Mounts\n3. Gradient Shader\n4. Half Dark Half Clear Shader \
           \n5. Pi Shadow Shader\n6. Dark Clear Combined Shader\n7. Photoshoot de shaders favoritos\n8. Salir\n')

menu()
option = int(input('Elija shader para el modelo: '))
while option != 8:
    if option == 1: sqrsEffect()
    elif option == 2: gradientM()
    elif option == 3: gradientShader()
    elif option == 4: dcHalfShader()
    elif option == 5: piShadowShader()
    elif option == 6: dcCombinedShader()
    elif option == 7: favsPhotoshoot()
    else: print('\nOpcion invalida\n')

    menu()
    option = int(input('Elija shader para el modelo: '))

print('Se ha acabado la seleccion de shaders! Chequee los resultados en la carpeta de outputs.\n')