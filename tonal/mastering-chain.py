from coldtype import *
from coldtype.blender import *

@b3d_animation((1920, 1080), bg=hsl(0.75))
def mastering_chain(f):
    return (StSt("Mastering Chain\nfor Beat Tapes",
        Font.Find("Reiner"), 350, leading=100)
        .f(1)
        .align(f.a.r, tv=1)
        .pen()
        .ch(b3d(lambda bp: bp
            .extrude(0.3))))
