from pyexpat import model
from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend, grafito, newS, barcodeEffect 


rend = Renderer(960, 540)

rend.active_texture = Texture("models/model.bmp")
modelPosition = V3(0, 0, -10)
rend.active_shader = barcodeEffect
rend.glLoadModel("models/model.obj",
                translate = V3(0, 0, -10),
                scale = V3(3,3,3),
                rotate = V3(0,0,0))
rend.glFinish("outputs/barcodeEffect.bmp")

