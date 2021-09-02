from coldtype import *

ufo = raw_ufo(__sibling__("../assets/GhzSymbolsAll.ufo"))

glyphs = {
    "G": "gordy",
    "S": "surf",
    "T": "baseball",
    "g": "gordy_short",
    "s": "surf_short",
    "m": "television",
    "a": "gordy_single",
}

class logos(animation):
    def pass_suffix(self, index=0):
        suffix = super().pass_suffix(index=index)
        return list(glyphs.items())[index][1]

@logos(timeline=len(glyphs), bg=1, fmt="svg")
def goodhertz_logo(f):
    g = ufo[list(glyphs.keys())[f.i]]
    return (DP()
        .glyph(g)
        .f(0)
        .scaleToRect(f.a.r.inset(50))
        .align(f.a.r))
