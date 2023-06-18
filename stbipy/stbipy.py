from ctypes import *

import os, sys

sys.path.append(os.path.join(os.path.split(__file__)[0], "bin"))
stbiDLL = WinDLL(os.path.join(os.path.split(__file__)[0], "bin/stb_image.dll"))

def STBIFUNC(name, restype, argtypes):
    func = getattr(stbiDLL, name)
    func.restype = restype
    func.argtypes = argtypes
    globals()[name] = func

STBI_VERSION = 1
STBI_default = 0
STBI_grey = 1
STBI_grey_alpha = 2
STBI_rgb = 3
STBI_rgb_alpha = 4

stbi_uc = c_ubyte
stbi_us = c_ushort

STBIFUNC("stbi_load_gif_from_memory", POINTER(stbi_uc), (POINTER(stbi_uc), c_int32, POINTER(POINTER(c_int32)), POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_load_from_memory", POINTER(stbi_uc), (POINTER(stbi_uc), c_int32, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_load", POINTER(stbi_uc), (c_char_p, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_load_16_from_memory", POINTER(stbi_us), (POINTER(stbi_uc), c_int32, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_load_16", POINTER(stbi_us), (c_char_p, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_loadf_from_memory", POINTER(c_float), (POINTER(stbi_uc), c_int32, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_loadf", POINTER(c_float), (c_char_p, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), c_int32))
STBIFUNC("stbi_hdr_to_ldr_gamma", None, (c_float, ))
STBIFUNC("stbi_hdr_to_ldr_scale", None, (c_float, ))
STBIFUNC("stbi_ldr_to_hdr_gamma", None, (c_float, ))
STBIFUNC("stbi_ldr_to_hdr_scale", None, (c_float, ))
STBIFUNC("stbi_is_hdr_from_memory", c_int32, (POINTER(stbi_uc), c_int32))
STBIFUNC("stbi_is_hdr", c_int32, (c_char_p, ))
STBIFUNC("stbi_failure_reason", c_void_p, ())
STBIFUNC("stbi_image_free", None, (c_void_p, ))
STBIFUNC("stbi_info_from_memory", c_int32, (POINTER(stbi_uc), c_int32, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32)))
STBIFUNC("stbi_info", c_int32, (c_char_p, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32)))
STBIFUNC("stbi_is_16_bit_from_memory", c_int32, (POINTER(stbi_uc), c_int32))
STBIFUNC("stbi_is_16_bit", c_int32, (c_char_p, ))
STBIFUNC("stbi_set_unpremultiply_on_load", None, (c_int32, ))
STBIFUNC("stbi_convert_iphone_png_to_rgb", None, (c_int32, ))
STBIFUNC("stbi_set_flip_vertically_on_load", None, (c_int32, ))
STBIFUNC("stbi_set_flip_vertically_on_load_thread", None, (c_int32, ))