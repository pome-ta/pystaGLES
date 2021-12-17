# Generated Files. DO NOT EDIT
# Generated on: 12/17/21 09:04:38
import ctypes
from objc_util import c
from .GLConstants import *

DEBUG = 0
loaded = [0, 0]

# GLES Constants
__gles1_gl_h_ = 0x00000001
GL_VERSION_ES_CM_1_0 = 0x00000001
GL_VERSION_ES_CL_1_0 = 0x00000001
GL_VERSION_ES_CM_1_1 = 0x00000001
GL_VERSION_ES_CL_1_1 = 0x00000001
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0x00000000
GL_TRUE = 0x00000001
GL_POINTS = 0x00000000
GL_LINES = 0x00000001
GL_LINE_LOOP = 0x00000002
GL_LINE_STRIP = 0x00000003
GL_TRIANGLES = 0x00000004
GL_TRIANGLE_STRIP = 0x00000005
GL_TRIANGLE_FAN = 0x00000006
GL_NEVER = 0x00000200
GL_LESS = 0x00000201
GL_EQUAL = 0x00000202
GL_LEQUAL = 0x00000203
GL_GREATER = 0x00000204
GL_NOTEQUAL = 0x00000205
GL_GEQUAL = 0x00000206
GL_ALWAYS = 0x00000207
GL_ZERO = 0x00000000
GL_ONE = 0x00000001
GL_SRC_COLOR = 0x00000300
GL_ONE_MINUS_SRC_COLOR = 0x00000301
GL_SRC_ALPHA = 0x00000302
GL_ONE_MINUS_SRC_ALPHA = 0x00000303
GL_DST_ALPHA = 0x00000304
GL_ONE_MINUS_DST_ALPHA = 0x00000305
GL_DST_COLOR = 0x00000306
GL_ONE_MINUS_DST_COLOR = 0x00000307
GL_SRC_ALPHA_SATURATE = 0x00000308
GL_CLIP_PLANE0 = 0x00003000
GL_CLIP_PLANE1 = 0x00003001
GL_CLIP_PLANE2 = 0x00003002
GL_CLIP_PLANE3 = 0x00003003
GL_CLIP_PLANE4 = 0x00003004
GL_CLIP_PLANE5 = 0x00003005
GL_FRONT = 0x00000404
GL_BACK = 0x00000405
GL_FRONT_AND_BACK = 0x00000408
GL_FOG = 0x00000b60
GL_LIGHTING = 0x00000b50
GL_TEXTURE_2D = 0x00000de1
GL_CULL_FACE = 0x00000b44
GL_ALPHA_TEST = 0x00000bc0
GL_BLEND = 0x00000be2
GL_COLOR_LOGIC_OP = 0x00000bf2
GL_DITHER = 0x00000bd0
GL_STENCIL_TEST = 0x00000b90
GL_DEPTH_TEST = 0x00000b71
GL_POINT_SMOOTH = 0x00000b10
GL_LINE_SMOOTH = 0x00000b20
GL_SCISSOR_TEST = 0x00000c11
GL_COLOR_MATERIAL = 0x00000b57
GL_NORMALIZE = 0x00000ba1
GL_RESCALE_NORMAL = 0x0000803a
GL_VERTEX_ARRAY = 0x00008074
GL_NORMAL_ARRAY = 0x00008075
GL_COLOR_ARRAY = 0x00008076
GL_TEXTURE_COORD_ARRAY = 0x00008078
GL_MULTISAMPLE = 0x0000809d
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x0000809e
GL_SAMPLE_ALPHA_TO_ONE = 0x0000809f
GL_SAMPLE_COVERAGE = 0x000080a0
GL_NO_ERROR = 0x00000000
GL_INVALID_ENUM = 0x00000500
GL_INVALID_VALUE = 0x00000501
GL_INVALID_OPERATION = 0x00000502
GL_STACK_OVERFLOW = 0x00000503
GL_STACK_UNDERFLOW = 0x00000504
GL_OUT_OF_MEMORY = 0x00000505
GL_EXP = 0x00000800
GL_EXP2 = 0x00000801
GL_FOG_DENSITY = 0x00000b62
GL_FOG_START = 0x00000b63
GL_FOG_END = 0x00000b64
GL_FOG_MODE = 0x00000b65
GL_FOG_COLOR = 0x00000b66
GL_CW = 0x00000900
GL_CCW = 0x00000901
GL_CURRENT_COLOR = 0x00000b00
GL_CURRENT_NORMAL = 0x00000b02
GL_CURRENT_TEXTURE_COORDS = 0x00000b03
GL_POINT_SIZE = 0x00000b11
GL_POINT_SIZE_MIN = 0x00008126
GL_POINT_SIZE_MAX = 0x00008127
GL_POINT_FADE_THRESHOLD_SIZE = 0x00008128
GL_POINT_DISTANCE_ATTENUATION = 0x00008129
GL_SMOOTH_POINT_SIZE_RANGE = 0x00000b12
GL_LINE_WIDTH = 0x00000b21
GL_SMOOTH_LINE_WIDTH_RANGE = 0x00000b22
GL_ALIASED_POINT_SIZE_RANGE = 0x0000846d
GL_ALIASED_LINE_WIDTH_RANGE = 0x0000846e
GL_CULL_FACE_MODE = 0x00000b45
GL_FRONT_FACE = 0x00000b46
GL_SHADE_MODEL = 0x00000b54
GL_DEPTH_RANGE = 0x00000b70
GL_DEPTH_WRITEMASK = 0x00000b72
GL_DEPTH_CLEAR_VALUE = 0x00000b73
GL_DEPTH_FUNC = 0x00000b74
GL_STENCIL_CLEAR_VALUE = 0x00000b91
GL_STENCIL_FUNC = 0x00000b92
GL_STENCIL_VALUE_MASK = 0x00000b93
GL_STENCIL_FAIL = 0x00000b94
GL_STENCIL_PASS_DEPTH_FAIL = 0x00000b95
GL_STENCIL_PASS_DEPTH_PASS = 0x00000b96
GL_STENCIL_REF = 0x00000b97
GL_STENCIL_WRITEMASK = 0x00000b98
GL_MATRIX_MODE = 0x00000ba0
GL_VIEWPORT = 0x00000ba2
GL_MODELVIEW_STACK_DEPTH = 0x00000ba3
GL_PROJECTION_STACK_DEPTH = 0x00000ba4
GL_TEXTURE_STACK_DEPTH = 0x00000ba5
GL_MODELVIEW_MATRIX = 0x00000ba6
GL_PROJECTION_MATRIX = 0x00000ba7
GL_TEXTURE_MATRIX = 0x00000ba8
GL_ALPHA_TEST_FUNC = 0x00000bc1
GL_ALPHA_TEST_REF = 0x00000bc2
GL_BLEND_DST = 0x00000be0
GL_BLEND_SRC = 0x00000be1
GL_LOGIC_OP_MODE = 0x00000bf0
GL_SCISSOR_BOX = 0x00000c10
GL_COLOR_CLEAR_VALUE = 0x00000c22
GL_COLOR_WRITEMASK = 0x00000c23
GL_MAX_LIGHTS = 0x00000d31
GL_MAX_CLIP_PLANES = 0x00000d32
GL_MAX_TEXTURE_SIZE = 0x00000d33
GL_MAX_MODELVIEW_STACK_DEPTH = 0x00000d36
GL_MAX_PROJECTION_STACK_DEPTH = 0x00000d38
GL_MAX_TEXTURE_STACK_DEPTH = 0x00000d39
GL_MAX_VIEWPORT_DIMS = 0x00000d3a
GL_MAX_TEXTURE_UNITS = 0x000084e2
GL_SUBPIXEL_BITS = 0x00000d50
GL_RED_BITS = 0x00000d52
GL_GREEN_BITS = 0x00000d53
GL_BLUE_BITS = 0x00000d54
GL_ALPHA_BITS = 0x00000d55
GL_DEPTH_BITS = 0x00000d56
GL_STENCIL_BITS = 0x00000d57
GL_POLYGON_OFFSET_UNITS = 0x00002a00
GL_POLYGON_OFFSET_FILL = 0x00008037
GL_POLYGON_OFFSET_FACTOR = 0x00008038
GL_TEXTURE_BINDING_2D = 0x00008069
GL_VERTEX_ARRAY_SIZE = 0x0000807a
GL_VERTEX_ARRAY_TYPE = 0x0000807b
GL_VERTEX_ARRAY_STRIDE = 0x0000807c
GL_NORMAL_ARRAY_TYPE = 0x0000807e
GL_NORMAL_ARRAY_STRIDE = 0x0000807f
GL_COLOR_ARRAY_SIZE = 0x00008081
GL_COLOR_ARRAY_TYPE = 0x00008082
GL_COLOR_ARRAY_STRIDE = 0x00008083
GL_TEXTURE_COORD_ARRAY_SIZE = 0x00008088
GL_TEXTURE_COORD_ARRAY_TYPE = 0x00008089
GL_TEXTURE_COORD_ARRAY_STRIDE = 0x0000808a
GL_VERTEX_ARRAY_POINTER = 0x0000808e
GL_NORMAL_ARRAY_POINTER = 0x0000808f
GL_COLOR_ARRAY_POINTER = 0x00008090
GL_TEXTURE_COORD_ARRAY_POINTER = 0x00008092
GL_SAMPLE_BUFFERS = 0x000080a8
GL_SAMPLES = 0x000080a9
GL_SAMPLE_COVERAGE_VALUE = 0x000080aa
GL_SAMPLE_COVERAGE_INVERT = 0x000080ab
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x000086a2
GL_COMPRESSED_TEXTURE_FORMATS = 0x000086a3
GL_DONT_CARE = 0x00001100
GL_FASTEST = 0x00001101
GL_NICEST = 0x00001102
GL_PERSPECTIVE_CORRECTION_HINT = 0x00000c50
GL_POINT_SMOOTH_HINT = 0x00000c51
GL_LINE_SMOOTH_HINT = 0x00000c52
GL_FOG_HINT = 0x00000c54
GL_GENERATE_MIPMAP_HINT = 0x00008192
GL_LIGHT_MODEL_AMBIENT = 0x00000b53
GL_LIGHT_MODEL_TWO_SIDE = 0x00000b52
GL_AMBIENT = 0x00001200
GL_DIFFUSE = 0x00001201
GL_SPECULAR = 0x00001202
GL_POSITION = 0x00001203
GL_SPOT_DIRECTION = 0x00001204
GL_SPOT_EXPONENT = 0x00001205
GL_SPOT_CUTOFF = 0x00001206
GL_CONSTANT_ATTENUATION = 0x00001207
GL_LINEAR_ATTENUATION = 0x00001208
GL_QUADRATIC_ATTENUATION = 0x00001209
GL_BYTE = 0x00001400
GL_UNSIGNED_BYTE = 0x00001401
GL_SHORT = 0x00001402
GL_UNSIGNED_SHORT = 0x00001403
GL_FLOAT = 0x00001406
GL_FIXED = 0x0000140c
GL_CLEAR = 0x00001500
GL_AND = 0x00001501
GL_AND_REVERSE = 0x00001502
GL_COPY = 0x00001503
GL_AND_INVERTED = 0x00001504
GL_NOOP = 0x00001505
GL_XOR = 0x00001506
GL_OR = 0x00001507
GL_NOR = 0x00001508
GL_EQUIV = 0x00001509
GL_INVERT = 0x0000150a
GL_OR_REVERSE = 0x0000150b
GL_COPY_INVERTED = 0x0000150c
GL_OR_INVERTED = 0x0000150d
GL_NAND = 0x0000150e
GL_SET = 0x0000150f
GL_EMISSION = 0x00001600
GL_SHININESS = 0x00001601
GL_AMBIENT_AND_DIFFUSE = 0x00001602
GL_MODELVIEW = 0x00001700
GL_PROJECTION = 0x00001701
GL_TEXTURE = 0x00001702
GL_ALPHA = 0x00001906
GL_RGB = 0x00001907
GL_RGBA = 0x00001908
GL_LUMINANCE = 0x00001909
GL_LUMINANCE_ALPHA = 0x0000190a
GL_UNPACK_ALIGNMENT = 0x00000cf5
GL_PACK_ALIGNMENT = 0x00000d05
GL_UNSIGNED_SHORT_4_4_4_4 = 0x00008033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x00008034
GL_UNSIGNED_SHORT_5_6_5 = 0x00008363
GL_FLAT = 0x00001d00
GL_SMOOTH = 0x00001d01
GL_KEEP = 0x00001e00
GL_REPLACE = 0x00001e01
GL_INCR = 0x00001e02
GL_DECR = 0x00001e03
GL_VENDOR = 0x00001f00
GL_RENDERER = 0x00001f01
GL_VERSION = 0x00001f02
GL_EXTENSIONS = 0x00001f03
GL_MODULATE = 0x00002100
GL_DECAL = 0x00002101
GL_ADD = 0x00000104
GL_TEXTURE_ENV_MODE = 0x00002200
GL_TEXTURE_ENV_COLOR = 0x00002201
GL_TEXTURE_ENV = 0x00002300
GL_NEAREST = 0x00002600
GL_LINEAR = 0x00002601
GL_NEAREST_MIPMAP_NEAREST = 0x00002700
GL_LINEAR_MIPMAP_NEAREST = 0x00002701
GL_NEAREST_MIPMAP_LINEAR = 0x00002702
GL_LINEAR_MIPMAP_LINEAR = 0x00002703
GL_TEXTURE_MAG_FILTER = 0x00002800
GL_TEXTURE_MIN_FILTER = 0x00002801
GL_TEXTURE_WRAP_S = 0x00002802
GL_TEXTURE_WRAP_T = 0x00002803
GL_GENERATE_MIPMAP = 0x00008191
GL_TEXTURE0 = 0x000084c0
GL_TEXTURE1 = 0x000084c1
GL_TEXTURE2 = 0x000084c2
GL_TEXTURE3 = 0x000084c3
GL_TEXTURE4 = 0x000084c4
GL_TEXTURE5 = 0x000084c5
GL_TEXTURE6 = 0x000084c6
GL_TEXTURE7 = 0x000084c7
GL_TEXTURE8 = 0x000084c8
GL_TEXTURE9 = 0x000084c9
GL_TEXTURE10 = 0x000084ca
GL_TEXTURE11 = 0x000084cb
GL_TEXTURE12 = 0x000084cc
GL_TEXTURE13 = 0x000084cd
GL_TEXTURE14 = 0x000084ce
GL_TEXTURE15 = 0x000084cf
GL_TEXTURE16 = 0x000084d0
GL_TEXTURE17 = 0x000084d1
GL_TEXTURE18 = 0x000084d2
GL_TEXTURE19 = 0x000084d3
GL_TEXTURE20 = 0x000084d4
GL_TEXTURE21 = 0x000084d5
GL_TEXTURE22 = 0x000084d6
GL_TEXTURE23 = 0x000084d7
GL_TEXTURE24 = 0x000084d8
GL_TEXTURE25 = 0x000084d9
GL_TEXTURE26 = 0x000084da
GL_TEXTURE27 = 0x000084db
GL_TEXTURE28 = 0x000084dc
GL_TEXTURE29 = 0x000084dd
GL_TEXTURE30 = 0x000084de
GL_TEXTURE31 = 0x000084df
GL_ACTIVE_TEXTURE = 0x000084e0
GL_CLIENT_ACTIVE_TEXTURE = 0x000084e1
GL_REPEAT = 0x00002901
GL_CLAMP_TO_EDGE = 0x0000812f
GL_LIGHT0 = 0x00004000
GL_LIGHT1 = 0x00004001
GL_LIGHT2 = 0x00004002
GL_LIGHT3 = 0x00004003
GL_LIGHT4 = 0x00004004
GL_LIGHT5 = 0x00004005
GL_LIGHT6 = 0x00004006
GL_LIGHT7 = 0x00004007
GL_ARRAY_BUFFER = 0x00008892
GL_ELEMENT_ARRAY_BUFFER = 0x00008893
GL_ARRAY_BUFFER_BINDING = 0x00008894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x00008895
GL_VERTEX_ARRAY_BUFFER_BINDING = 0x00008896
GL_NORMAL_ARRAY_BUFFER_BINDING = 0x00008897
GL_COLOR_ARRAY_BUFFER_BINDING = 0x00008898
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x0000889a
GL_STATIC_DRAW = 0x000088e4
GL_DYNAMIC_DRAW = 0x000088e8
GL_BUFFER_SIZE = 0x00008764
GL_BUFFER_USAGE = 0x00008765
GL_SUBTRACT = 0x000084e7
GL_COMBINE = 0x00008570
GL_COMBINE_RGB = 0x00008571
GL_COMBINE_ALPHA = 0x00008572
GL_RGB_SCALE = 0x00008573
GL_ADD_SIGNED = 0x00008574
GL_INTERPOLATE = 0x00008575
GL_CONSTANT = 0x00008576
GL_PRIMARY_COLOR = 0x00008577
GL_PREVIOUS = 0x00008578
GL_OPERAND0_RGB = 0x00008590
GL_OPERAND1_RGB = 0x00008591
GL_OPERAND2_RGB = 0x00008592
GL_OPERAND0_ALPHA = 0x00008598
GL_OPERAND1_ALPHA = 0x00008599
GL_OPERAND2_ALPHA = 0x0000859a
GL_ALPHA_SCALE = 0x00000d1c
GL_SRC0_RGB = 0x00008580
GL_SRC1_RGB = 0x00008581
GL_SRC2_RGB = 0x00008582
GL_SRC0_ALPHA = 0x00008588
GL_SRC1_ALPHA = 0x00008589
GL_SRC2_ALPHA = 0x0000858a
GL_DOT3_RGB = 0x000086ae
GL_DOT3_RGBA = 0x000086af
GL_OES_compressed_paletted_texture = 0x00000001
GL_PALETTE4_RGB8_OES = 0x00008b90
GL_PALETTE4_RGBA8_OES = 0x00008b91
GL_PALETTE4_R5_G6_B5_OES = 0x00008b92
GL_PALETTE4_RGBA4_OES = 0x00008b93
GL_PALETTE4_RGB5_A1_OES = 0x00008b94
GL_PALETTE8_RGB8_OES = 0x00008b95
GL_PALETTE8_RGBA8_OES = 0x00008b96
GL_PALETTE8_R5_G6_B5_OES = 0x00008b97
GL_PALETTE8_RGBA4_OES = 0x00008b98
GL_PALETTE8_RGB5_A1_OES = 0x00008b99
GL_OES_point_size_array = 0x00000001
GL_POINT_SIZE_ARRAY_OES = 0x00008b9c
GL_POINT_SIZE_ARRAY_TYPE_OES = 0x0000898a
GL_POINT_SIZE_ARRAY_STRIDE_OES = 0x0000898b
GL_POINT_SIZE_ARRAY_POINTER_OES = 0x0000898c
GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES = 0x00008b9f
GL_OES_point_sprite = 0x00000001
GL_POINT_SPRITE_OES = 0x00008861
GL_COORD_REPLACE_OES = 0x00008862
GL_OES_read_format = 0x00000001
GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = 0x00008b9a
GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = 0x00008b9b

# GL Functions
try:

  def glAlphaFunc(func, ref, func_t=GLenum, ref_t=GLfloat):
    restype = None
    argtypes = [func_t, ref_t]
    cfunc = c.glAlphaFunc
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(func, ref)

  # Check if the function actually exists
  f = c.glAlphaFunc
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClearColor(red,
                   green,
                   blue,
                   alpha,
                   red_t=GLfloat,
                   green_t=GLfloat,
                   blue_t=GLfloat,
                   alpha_t=GLfloat):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glClearColor
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glClearColor
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClearDepthf(d, d_t=GLfloat):
    restype = None
    argtypes = [d_t]
    cfunc = c.glClearDepthf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(d)

  # Check if the function actually exists
  f = c.glClearDepthf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClipPlanef(p, param0, p_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [p_t, param0_t]
    cfunc = c.glClipPlanef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(p, param0)

  # Check if the function actually exists
  f = c.glClipPlanef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glColor4f(red,
                green,
                blue,
                alpha,
                red_t=GLfloat,
                green_t=GLfloat,
                blue_t=GLfloat,
                alpha_t=GLfloat):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glColor4f
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glColor4f
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDepthRangef(n, f, n_t=GLfloat, f_t=GLfloat):
    restype = None
    argtypes = [n_t, f_t]
    cfunc = c.glDepthRangef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, f)

  # Check if the function actually exists
  f = c.glDepthRangef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFogf(pname, param, pname_t=GLenum, param_t=GLfloat):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glFogf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glFogf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFogfv(pname, param0, pname_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glFogfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glFogfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFrustumf(l,
                 r,
                 b,
                 t,
                 n,
                 f,
                 l_t=GLfloat,
                 r_t=GLfloat,
                 b_t=GLfloat,
                 t_t=GLfloat,
                 n_t=GLfloat,
                 f_t=GLfloat):
    restype = None
    argtypes = [l_t, r_t, b_t, t_t, n_t, f_t]
    cfunc = c.glFrustumf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(l, r, b, t, n, f)

  # Check if the function actually exists
  f = c.glFrustumf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetClipPlanef(plane, param0, plane_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [plane_t, param0_t]
    cfunc = c.glGetClipPlanef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(plane, param0)

  # Check if the function actually exists
  f = c.glGetClipPlanef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetFloatv(pname, param0, pname_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glGetFloatv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glGetFloatv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetLightfv(light,
                   pname,
                   param0,
                   light_t=GLenum,
                   pname_t=GLenum,
                   param0_t=GLfloat):
    restype = None
    argtypes = [light_t, pname_t, param0_t]
    cfunc = c.glGetLightfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param0)

  # Check if the function actually exists
  f = c.glGetLightfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetMaterialfv(face,
                      pname,
                      param0,
                      face_t=GLenum,
                      pname_t=GLenum,
                      param0_t=GLfloat):
    restype = None
    argtypes = [face_t, pname_t, param0_t]
    cfunc = c.glGetMaterialfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param0)

  # Check if the function actually exists
  f = c.glGetMaterialfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexEnvfv(target,
                    pname,
                    param0,
                    target_t=GLenum,
                    pname_t=GLenum,
                    param0_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexEnvfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexEnvfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexParameterfv(target,
                          pname,
                          param0,
                          target_t=GLenum,
                          pname_t=GLenum,
                          param0_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexParameterfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexParameterfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightModelf(pname, param, pname_t=GLenum, param_t=GLfloat):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glLightModelf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glLightModelf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightModelfv(pname, param0, pname_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glLightModelfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glLightModelfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightf(light,
               pname,
               param,
               light_t=GLenum,
               pname_t=GLenum,
               param_t=GLfloat):
    restype = None
    argtypes = [light_t, pname_t, param_t]
    cfunc = c.glLightf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param)

  # Check if the function actually exists
  f = c.glLightf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightfv(light,
                pname,
                param0,
                light_t=GLenum,
                pname_t=GLenum,
                param0_t=GLfloat):
    restype = None
    argtypes = [light_t, pname_t, param0_t]
    cfunc = c.glLightfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param0)

  # Check if the function actually exists
  f = c.glLightfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLineWidth(width, width_t=GLfloat):
    restype = None
    argtypes = [width_t]
    cfunc = c.glLineWidth
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(width)

  # Check if the function actually exists
  f = c.glLineWidth
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLoadMatrixf(param0, param0_t=GLfloat):
    restype = None
    argtypes = [param0_t]
    cfunc = c.glLoadMatrixf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(param0)

  # Check if the function actually exists
  f = c.glLoadMatrixf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMaterialf(face,
                  pname,
                  param,
                  face_t=GLenum,
                  pname_t=GLenum,
                  param_t=GLfloat):
    restype = None
    argtypes = [face_t, pname_t, param_t]
    cfunc = c.glMaterialf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param)

  # Check if the function actually exists
  f = c.glMaterialf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMaterialfv(face,
                   pname,
                   param0,
                   face_t=GLenum,
                   pname_t=GLenum,
                   param0_t=GLfloat):
    restype = None
    argtypes = [face_t, pname_t, param0_t]
    cfunc = c.glMaterialfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param0)

  # Check if the function actually exists
  f = c.glMaterialfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMultMatrixf(param0, param0_t=GLfloat):
    restype = None
    argtypes = [param0_t]
    cfunc = c.glMultMatrixf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(param0)

  # Check if the function actually exists
  f = c.glMultMatrixf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMultiTexCoord4f(target,
                        s,
                        t,
                        r,
                        q,
                        target_t=GLenum,
                        s_t=GLfloat,
                        t_t=GLfloat,
                        r_t=GLfloat,
                        q_t=GLfloat):
    restype = None
    argtypes = [target_t, s_t, t_t, r_t, q_t]
    cfunc = c.glMultiTexCoord4f
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, s, t, r, q)

  # Check if the function actually exists
  f = c.glMultiTexCoord4f
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glNormal3f(nx, ny, nz, nx_t=GLfloat, ny_t=GLfloat, nz_t=GLfloat):
    restype = None
    argtypes = [nx_t, ny_t, nz_t]
    cfunc = c.glNormal3f
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(nx, ny, nz)

  # Check if the function actually exists
  f = c.glNormal3f
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glOrthof(l,
               r,
               b,
               t,
               n,
               f,
               l_t=GLfloat,
               r_t=GLfloat,
               b_t=GLfloat,
               t_t=GLfloat,
               n_t=GLfloat,
               f_t=GLfloat):
    restype = None
    argtypes = [l_t, r_t, b_t, t_t, n_t, f_t]
    cfunc = c.glOrthof
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(l, r, b, t, n, f)

  # Check if the function actually exists
  f = c.glOrthof
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointParameterf(pname, param, pname_t=GLenum, param_t=GLfloat):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glPointParameterf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glPointParameterf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointParameterfv(pname, param0, pname_t=GLenum, param0_t=GLfloat):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glPointParameterfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glPointParameterfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointSize(size, size_t=GLfloat):
    restype = None
    argtypes = [size_t]
    cfunc = c.glPointSize
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(size)

  # Check if the function actually exists
  f = c.glPointSize
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPolygonOffset(factor, units, factor_t=GLfloat, units_t=GLfloat):
    restype = None
    argtypes = [factor_t, units_t]
    cfunc = c.glPolygonOffset
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(factor, units)

  # Check if the function actually exists
  f = c.glPolygonOffset
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glRotatef(angle,
                x,
                y,
                z,
                angle_t=GLfloat,
                x_t=GLfloat,
                y_t=GLfloat,
                z_t=GLfloat):
    restype = None
    argtypes = [angle_t, x_t, y_t, z_t]
    cfunc = c.glRotatef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(angle, x, y, z)

  # Check if the function actually exists
  f = c.glRotatef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glScalef(x, y, z, x_t=GLfloat, y_t=GLfloat, z_t=GLfloat):
    restype = None
    argtypes = [x_t, y_t, z_t]
    cfunc = c.glScalef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, z)

  # Check if the function actually exists
  f = c.glScalef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnvf(target,
                pname,
                param,
                target_t=GLenum,
                pname_t=GLenum,
                param_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexEnvf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexEnvf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnvfv(target,
                 pname,
                 param0,
                 target_t=GLenum,
                 pname_t=GLenum,
                 param0_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexEnvfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexEnvfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameterf(target,
                      pname,
                      param,
                      target_t=GLenum,
                      pname_t=GLenum,
                      param_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexParameterf
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexParameterf
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameterfv(target,
                       pname,
                       param0,
                       target_t=GLenum,
                       pname_t=GLenum,
                       param0_t=GLfloat):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexParameterfv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexParameterfv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTranslatef(x, y, z, x_t=GLfloat, y_t=GLfloat, z_t=GLfloat):
    restype = None
    argtypes = [x_t, y_t, z_t]
    cfunc = c.glTranslatef
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, z)

  # Check if the function actually exists
  f = c.glTranslatef
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glActiveTexture(texture, texture_t=GLenum):
    restype = None
    argtypes = [texture_t]
    cfunc = c.glActiveTexture
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(texture)

  # Check if the function actually exists
  f = c.glActiveTexture
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glAlphaFuncx(func, ref, func_t=GLenum, ref_t=GLfixed):
    restype = None
    argtypes = [func_t, ref_t]
    cfunc = c.glAlphaFuncx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(func, ref)

  # Check if the function actually exists
  f = c.glAlphaFuncx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glBindBuffer(target, buffer, target_t=GLenum, buffer_t=GLuint):
    restype = None
    argtypes = [target_t, buffer_t]
    cfunc = c.glBindBuffer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, buffer)

  # Check if the function actually exists
  f = c.glBindBuffer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glBindTexture(target, texture, target_t=GLenum, texture_t=GLuint):
    restype = None
    argtypes = [target_t, texture_t]
    cfunc = c.glBindTexture
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, texture)

  # Check if the function actually exists
  f = c.glBindTexture
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glBlendFunc(sfactor, dfactor, sfactor_t=GLenum, dfactor_t=GLenum):
    restype = None
    argtypes = [sfactor_t, dfactor_t]
    cfunc = c.glBlendFunc
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(sfactor, dfactor)

  # Check if the function actually exists
  f = c.glBlendFunc
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glBufferData(target,
                   size,
                   voiddata,
                   usage,
                   target_t=GLenum,
                   size_t=GLsizeiptr,
                   voiddata_t=ctypes.c_void_p,
                   usage_t=GLenum):
    restype = None
    argtypes = [target_t, size_t, voiddata_t, usage_t]
    cfunc = c.glBufferData
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, size, voiddata, usage)

  # Check if the function actually exists
  f = c.glBufferData
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glBufferSubData(target,
                      offset,
                      size,
                      voiddata,
                      target_t=GLenum,
                      offset_t=GLintptr,
                      size_t=GLsizeiptr,
                      voiddata_t=ctypes.c_void_p):
    restype = None
    argtypes = [target_t, offset_t, size_t, voiddata_t]
    cfunc = c.glBufferSubData
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, offset, size, voiddata)

  # Check if the function actually exists
  f = c.glBufferSubData
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClear(mask, mask_t=GLbitfield):
    restype = None
    argtypes = [mask_t]
    cfunc = c.glClear
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mask)

  # Check if the function actually exists
  f = c.glClear
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClearColorx(red,
                    green,
                    blue,
                    alpha,
                    red_t=GLfixed,
                    green_t=GLfixed,
                    blue_t=GLfixed,
                    alpha_t=GLfixed):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glClearColorx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glClearColorx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClearDepthx(depth, depth_t=GLfixed):
    restype = None
    argtypes = [depth_t]
    cfunc = c.glClearDepthx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(depth)

  # Check if the function actually exists
  f = c.glClearDepthx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClearStencil(s, s_t=GLint):
    restype = None
    argtypes = [s_t]
    cfunc = c.glClearStencil
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(s)

  # Check if the function actually exists
  f = c.glClearStencil
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClientActiveTexture(texture, texture_t=GLenum):
    restype = None
    argtypes = [texture_t]
    cfunc = c.glClientActiveTexture
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(texture)

  # Check if the function actually exists
  f = c.glClientActiveTexture
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glClipPlanex(plane, param0, plane_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [plane_t, param0_t]
    cfunc = c.glClipPlanex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(plane, param0)

  # Check if the function actually exists
  f = c.glClipPlanex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glColor4ub(red,
                 green,
                 blue,
                 alpha,
                 red_t=GLubyte,
                 green_t=GLubyte,
                 blue_t=GLubyte,
                 alpha_t=GLubyte):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glColor4ub
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glColor4ub
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glColor4x(red,
                green,
                blue,
                alpha,
                red_t=GLfixed,
                green_t=GLfixed,
                blue_t=GLfixed,
                alpha_t=GLfixed):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glColor4x
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glColor4x
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glColorMask(red,
                  green,
                  blue,
                  alpha,
                  red_t=GLboolean,
                  green_t=GLboolean,
                  blue_t=GLboolean,
                  alpha_t=GLboolean):
    restype = None
    argtypes = [red_t, green_t, blue_t, alpha_t]
    cfunc = c.glColorMask
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(red, green, blue, alpha)

  # Check if the function actually exists
  f = c.glColorMask
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glColorPointer(size,
                     type,
                     stride,
                     voidpointer,
                     size_t=GLint,
                     type_t=GLenum,
                     stride_t=GLsizei,
                     voidpointer_t=ctypes.c_void_p):
    restype = None
    argtypes = [size_t, type_t, stride_t, voidpointer_t]
    cfunc = c.glColorPointer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(size, type, stride, voidpointer)

  # Check if the function actually exists
  f = c.glColorPointer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glCompressedTexImage2D(target,
                             level,
                             internalformat,
                             width,
                             height,
                             border,
                             imageSize,
                             voiddata,
                             target_t=GLenum,
                             level_t=GLint,
                             internalformat_t=GLenum,
                             width_t=GLsizei,
                             height_t=GLsizei,
                             border_t=GLint,
                             imageSize_t=GLsizei,
                             voiddata_t=ctypes.c_void_p):
    restype = None
    argtypes = [
      target_t, level_t, internalformat_t, width_t, height_t, border_t,
      imageSize_t, voiddata_t
    ]
    cfunc = c.glCompressedTexImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, internalformat, width, height, border,
                 imageSize, voiddata)

  # Check if the function actually exists
  f = c.glCompressedTexImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glCompressedTexSubImage2D(target,
                                level,
                                xoffset,
                                yoffset,
                                width,
                                height,
                                format,
                                imageSize,
                                voiddata,
                                target_t=GLenum,
                                level_t=GLint,
                                xoffset_t=GLint,
                                yoffset_t=GLint,
                                width_t=GLsizei,
                                height_t=GLsizei,
                                format_t=GLenum,
                                imageSize_t=GLsizei,
                                voiddata_t=ctypes.c_void_p):
    restype = None
    argtypes = [
      target_t, level_t, xoffset_t, yoffset_t, width_t, height_t, format_t,
      imageSize_t, voiddata_t
    ]
    cfunc = c.glCompressedTexSubImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, xoffset, yoffset, width, height, format,
                 imageSize, voiddata)

  # Check if the function actually exists
  f = c.glCompressedTexSubImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glCopyTexImage2D(target,
                       level,
                       internalformat,
                       x,
                       y,
                       width,
                       height,
                       border,
                       target_t=GLenum,
                       level_t=GLint,
                       internalformat_t=GLenum,
                       x_t=GLint,
                       y_t=GLint,
                       width_t=GLsizei,
                       height_t=GLsizei,
                       border_t=GLint):
    restype = None
    argtypes = [
      target_t, level_t, internalformat_t, x_t, y_t, width_t, height_t,
      border_t
    ]
    cfunc = c.glCopyTexImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, internalformat, x, y, width, height, border)

  # Check if the function actually exists
  f = c.glCopyTexImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glCopyTexSubImage2D(target,
                          level,
                          xoffset,
                          yoffset,
                          x,
                          y,
                          width,
                          height,
                          target_t=GLenum,
                          level_t=GLint,
                          xoffset_t=GLint,
                          yoffset_t=GLint,
                          x_t=GLint,
                          y_t=GLint,
                          width_t=GLsizei,
                          height_t=GLsizei):
    restype = None
    argtypes = [
      target_t, level_t, xoffset_t, yoffset_t, x_t, y_t, width_t, height_t
    ]
    cfunc = c.glCopyTexSubImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, xoffset, yoffset, x, y, width, height)

  # Check if the function actually exists
  f = c.glCopyTexSubImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glCullFace(mode, mode_t=GLenum):
    restype = None
    argtypes = [mode_t]
    cfunc = c.glCullFace
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode)

  # Check if the function actually exists
  f = c.glCullFace
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDeleteBuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
    restype = None
    argtypes = [n_t, param0_t]
    cfunc = c.glDeleteBuffers
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, param0)

  # Check if the function actually exists
  f = c.glDeleteBuffers
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDeleteTextures(n, param0, n_t=GLsizei, param0_t=GLuint):
    restype = None
    argtypes = [n_t, param0_t]
    cfunc = c.glDeleteTextures
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, param0)

  # Check if the function actually exists
  f = c.glDeleteTextures
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDepthFunc(func, func_t=GLenum):
    restype = None
    argtypes = [func_t]
    cfunc = c.glDepthFunc
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(func)

  # Check if the function actually exists
  f = c.glDepthFunc
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDepthMask(flag, flag_t=GLboolean):
    restype = None
    argtypes = [flag_t]
    cfunc = c.glDepthMask
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(flag)

  # Check if the function actually exists
  f = c.glDepthMask
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDepthRangex(n, f, n_t=GLfixed, f_t=GLfixed):
    restype = None
    argtypes = [n_t, f_t]
    cfunc = c.glDepthRangex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, f)

  # Check if the function actually exists
  f = c.glDepthRangex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDisable(cap, cap_t=GLenum):
    restype = None
    argtypes = [cap_t]
    cfunc = c.glDisable
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(cap)

  # Check if the function actually exists
  f = c.glDisable
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDisableClientState(array, array_t=GLenum):
    restype = None
    argtypes = [array_t]
    cfunc = c.glDisableClientState
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(array)

  # Check if the function actually exists
  f = c.glDisableClientState
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDrawArrays(mode,
                   first,
                   count,
                   mode_t=GLenum,
                   first_t=GLint,
                   count_t=GLsizei):
    restype = None
    argtypes = [mode_t, first_t, count_t]
    cfunc = c.glDrawArrays
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode, first, count)

  # Check if the function actually exists
  f = c.glDrawArrays
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glDrawElements(mode,
                     count,
                     type,
                     voidindices,
                     mode_t=GLenum,
                     count_t=GLsizei,
                     type_t=GLenum,
                     voidindices_t=ctypes.c_void_p):
    restype = None
    argtypes = [mode_t, count_t, type_t, voidindices_t]
    cfunc = c.glDrawElements
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode, count, type, voidindices)

  # Check if the function actually exists
  f = c.glDrawElements
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glEnable(cap, cap_t=GLenum):
    restype = None
    argtypes = [cap_t]
    cfunc = c.glEnable
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(cap)

  # Check if the function actually exists
  f = c.glEnable
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glEnableClientState(array, array_t=GLenum):
    restype = None
    argtypes = [array_t]
    cfunc = c.glEnableClientState
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(array)

  # Check if the function actually exists
  f = c.glEnableClientState
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFinish(void, void_t=ctypes.c_void_p):
    restype = None
    argtypes = [void_t]
    cfunc = c.glFinish
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glFinish
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFlush(void, void_t=ctypes.c_void_p):
    restype = None
    argtypes = [void_t]
    cfunc = c.glFlush
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glFlush
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFogx(pname, param, pname_t=GLenum, param_t=GLfixed):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glFogx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glFogx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFogxv(pname, param0, pname_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glFogxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glFogxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFrontFace(mode, mode_t=GLenum):
    restype = None
    argtypes = [mode_t]
    cfunc = c.glFrontFace
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode)

  # Check if the function actually exists
  f = c.glFrontFace
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glFrustumx(l,
                 r,
                 b,
                 t,
                 n,
                 f,
                 l_t=GLfixed,
                 r_t=GLfixed,
                 b_t=GLfixed,
                 t_t=GLfixed,
                 n_t=GLfixed,
                 f_t=GLfixed):
    restype = None
    argtypes = [l_t, r_t, b_t, t_t, n_t, f_t]
    cfunc = c.glFrustumx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(l, r, b, t, n, f)

  # Check if the function actually exists
  f = c.glFrustumx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetBooleanv(pname, param0, pname_t=GLenum, param0_t=GLboolean):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glGetBooleanv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glGetBooleanv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetBufferParameteriv(target,
                             pname,
                             param0,
                             target_t=GLenum,
                             pname_t=GLenum,
                             param0_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetBufferParameteriv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetBufferParameteriv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetClipPlanex(plane, param0, plane_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [plane_t, param0_t]
    cfunc = c.glGetClipPlanex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(plane, param0)

  # Check if the function actually exists
  f = c.glGetClipPlanex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGenBuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
    restype = None
    argtypes = [n_t, param0_t]
    cfunc = c.glGenBuffers
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, param0)

  # Check if the function actually exists
  f = c.glGenBuffers
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGenTextures(n, param0, n_t=GLsizei, param0_t=GLuint):
    restype = None
    argtypes = [n_t, param0_t]
    cfunc = c.glGenTextures
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(n, param0)

  # Check if the function actually exists
  f = c.glGenTextures
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetError(void, void_t=ctypes.c_void_p):
    restype = GLenum
    argtypes = [void_t]
    cfunc = c.glGetError
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glGetError
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetFixedv(pname, param0, pname_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glGetFixedv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glGetFixedv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetIntegerv(pname, param0, pname_t=GLenum, param0_t=GLint):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glGetIntegerv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glGetIntegerv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetLightxv(light,
                   pname,
                   param0,
                   light_t=GLenum,
                   pname_t=GLenum,
                   param0_t=GLfixed):
    restype = None
    argtypes = [light_t, pname_t, param0_t]
    cfunc = c.glGetLightxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param0)

  # Check if the function actually exists
  f = c.glGetLightxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetMaterialxv(face,
                      pname,
                      param0,
                      face_t=GLenum,
                      pname_t=GLenum,
                      param0_t=GLfixed):
    restype = None
    argtypes = [face_t, pname_t, param0_t]
    cfunc = c.glGetMaterialxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param0)

  # Check if the function actually exists
  f = c.glGetMaterialxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetPointerv(pname,
                    voidparams,
                    pname_t=GLenum,
                    voidparams_t=ctypes.c_void_p):
    restype = None
    argtypes = [pname_t, voidparams_t]
    cfunc = c.glGetPointerv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, voidparams)

  # Check if the function actually exists
  f = c.glGetPointerv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexEnviv(target,
                    pname,
                    param0,
                    target_t=GLenum,
                    pname_t=GLenum,
                    param0_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexEnviv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexEnviv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexEnvxv(target,
                    pname,
                    param0,
                    target_t=GLenum,
                    pname_t=GLenum,
                    param0_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexEnvxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexEnvxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexParameteriv(target,
                          pname,
                          param0,
                          target_t=GLenum,
                          pname_t=GLenum,
                          param0_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexParameteriv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexParameteriv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glGetTexParameterxv(target,
                          pname,
                          param0,
                          target_t=GLenum,
                          pname_t=GLenum,
                          param0_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glGetTexParameterxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glGetTexParameterxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glHint(target, mode, target_t=GLenum, mode_t=GLenum):
    restype = None
    argtypes = [target_t, mode_t]
    cfunc = c.glHint
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, mode)

  # Check if the function actually exists
  f = c.glHint
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glIsBuffer(buffer, buffer_t=GLuint):
    restype = GLboolean
    argtypes = [buffer_t]
    cfunc = c.glIsBuffer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(buffer)

  # Check if the function actually exists
  f = c.glIsBuffer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glIsEnabled(cap, cap_t=GLenum):
    restype = GLboolean
    argtypes = [cap_t]
    cfunc = c.glIsEnabled
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(cap)

  # Check if the function actually exists
  f = c.glIsEnabled
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glIsTexture(texture, texture_t=GLuint):
    restype = GLboolean
    argtypes = [texture_t]
    cfunc = c.glIsTexture
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(texture)

  # Check if the function actually exists
  f = c.glIsTexture
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightModelx(pname, param, pname_t=GLenum, param_t=GLfixed):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glLightModelx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glLightModelx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightModelxv(pname, param0, pname_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glLightModelxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glLightModelxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightx(light,
               pname,
               param,
               light_t=GLenum,
               pname_t=GLenum,
               param_t=GLfixed):
    restype = None
    argtypes = [light_t, pname_t, param_t]
    cfunc = c.glLightx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param)

  # Check if the function actually exists
  f = c.glLightx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLightxv(light,
                pname,
                param0,
                light_t=GLenum,
                pname_t=GLenum,
                param0_t=GLfixed):
    restype = None
    argtypes = [light_t, pname_t, param0_t]
    cfunc = c.glLightxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(light, pname, param0)

  # Check if the function actually exists
  f = c.glLightxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLineWidthx(width, width_t=GLfixed):
    restype = None
    argtypes = [width_t]
    cfunc = c.glLineWidthx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(width)

  # Check if the function actually exists
  f = c.glLineWidthx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLoadIdentity(void, void_t=ctypes.c_void_p):
    restype = None
    argtypes = [void_t]
    cfunc = c.glLoadIdentity
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glLoadIdentity
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLoadMatrixx(param0, param0_t=GLfixed):
    restype = None
    argtypes = [param0_t]
    cfunc = c.glLoadMatrixx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(param0)

  # Check if the function actually exists
  f = c.glLoadMatrixx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glLogicOp(opcode, opcode_t=GLenum):
    restype = None
    argtypes = [opcode_t]
    cfunc = c.glLogicOp
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(opcode)

  # Check if the function actually exists
  f = c.glLogicOp
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMaterialx(face,
                  pname,
                  param,
                  face_t=GLenum,
                  pname_t=GLenum,
                  param_t=GLfixed):
    restype = None
    argtypes = [face_t, pname_t, param_t]
    cfunc = c.glMaterialx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param)

  # Check if the function actually exists
  f = c.glMaterialx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMaterialxv(face,
                   pname,
                   param0,
                   face_t=GLenum,
                   pname_t=GLenum,
                   param0_t=GLfixed):
    restype = None
    argtypes = [face_t, pname_t, param0_t]
    cfunc = c.glMaterialxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(face, pname, param0)

  # Check if the function actually exists
  f = c.glMaterialxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMatrixMode(mode, mode_t=GLenum):
    restype = None
    argtypes = [mode_t]
    cfunc = c.glMatrixMode
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode)

  # Check if the function actually exists
  f = c.glMatrixMode
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMultMatrixx(param0, param0_t=GLfixed):
    restype = None
    argtypes = [param0_t]
    cfunc = c.glMultMatrixx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(param0)

  # Check if the function actually exists
  f = c.glMultMatrixx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glMultiTexCoord4x(texture,
                        s,
                        t,
                        r,
                        q,
                        texture_t=GLenum,
                        s_t=GLfixed,
                        t_t=GLfixed,
                        r_t=GLfixed,
                        q_t=GLfixed):
    restype = None
    argtypes = [texture_t, s_t, t_t, r_t, q_t]
    cfunc = c.glMultiTexCoord4x
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(texture, s, t, r, q)

  # Check if the function actually exists
  f = c.glMultiTexCoord4x
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glNormal3x(nx, ny, nz, nx_t=GLfixed, ny_t=GLfixed, nz_t=GLfixed):
    restype = None
    argtypes = [nx_t, ny_t, nz_t]
    cfunc = c.glNormal3x
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(nx, ny, nz)

  # Check if the function actually exists
  f = c.glNormal3x
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glNormalPointer(type,
                      stride,
                      voidpointer,
                      type_t=GLenum,
                      stride_t=GLsizei,
                      voidpointer_t=ctypes.c_void_p):
    restype = None
    argtypes = [type_t, stride_t, voidpointer_t]
    cfunc = c.glNormalPointer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(type, stride, voidpointer)

  # Check if the function actually exists
  f = c.glNormalPointer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glOrthox(l,
               r,
               b,
               t,
               n,
               f,
               l_t=GLfixed,
               r_t=GLfixed,
               b_t=GLfixed,
               t_t=GLfixed,
               n_t=GLfixed,
               f_t=GLfixed):
    restype = None
    argtypes = [l_t, r_t, b_t, t_t, n_t, f_t]
    cfunc = c.glOrthox
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(l, r, b, t, n, f)

  # Check if the function actually exists
  f = c.glOrthox
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPixelStorei(pname, param, pname_t=GLenum, param_t=GLint):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glPixelStorei
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glPixelStorei
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointParameterx(pname, param, pname_t=GLenum, param_t=GLfixed):
    restype = None
    argtypes = [pname_t, param_t]
    cfunc = c.glPointParameterx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param)

  # Check if the function actually exists
  f = c.glPointParameterx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointParameterxv(pname, param0, pname_t=GLenum, param0_t=GLfixed):
    restype = None
    argtypes = [pname_t, param0_t]
    cfunc = c.glPointParameterxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(pname, param0)

  # Check if the function actually exists
  f = c.glPointParameterxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointSizex(size, size_t=GLfixed):
    restype = None
    argtypes = [size_t]
    cfunc = c.glPointSizex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(size)

  # Check if the function actually exists
  f = c.glPointSizex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPolygonOffsetx(factor, units, factor_t=GLfixed, units_t=GLfixed):
    restype = None
    argtypes = [factor_t, units_t]
    cfunc = c.glPolygonOffsetx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(factor, units)

  # Check if the function actually exists
  f = c.glPolygonOffsetx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPopMatrix(void, void_t=ctypes.c_void_p):
    restype = None
    argtypes = [void_t]
    cfunc = c.glPopMatrix
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glPopMatrix
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPushMatrix(void, void_t=ctypes.c_void_p):
    restype = None
    argtypes = [void_t]
    cfunc = c.glPushMatrix
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(void)

  # Check if the function actually exists
  f = c.glPushMatrix
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glReadPixels(x,
                   y,
                   width,
                   height,
                   format,
                   type,
                   voidpixels,
                   x_t=GLint,
                   y_t=GLint,
                   width_t=GLsizei,
                   height_t=GLsizei,
                   format_t=GLenum,
                   type_t=GLenum,
                   voidpixels_t=ctypes.c_void_p):
    restype = None
    argtypes = [x_t, y_t, width_t, height_t, format_t, type_t, voidpixels_t]
    cfunc = c.glReadPixels
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, width, height, format, type, voidpixels)

  # Check if the function actually exists
  f = c.glReadPixels
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glRotatex(angle,
                x,
                y,
                z,
                angle_t=GLfixed,
                x_t=GLfixed,
                y_t=GLfixed,
                z_t=GLfixed):
    restype = None
    argtypes = [angle_t, x_t, y_t, z_t]
    cfunc = c.glRotatex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(angle, x, y, z)

  # Check if the function actually exists
  f = c.glRotatex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glSampleCoverage(value, invert, value_t=GLfloat, invert_t=GLboolean):
    restype = None
    argtypes = [value_t, invert_t]
    cfunc = c.glSampleCoverage
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(value, invert)

  # Check if the function actually exists
  f = c.glSampleCoverage
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glSampleCoveragex(value, invert, value_t=GLclampx, invert_t=GLboolean):
    restype = None
    argtypes = [value_t, invert_t]
    cfunc = c.glSampleCoveragex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(value, invert)

  # Check if the function actually exists
  f = c.glSampleCoveragex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glScalex(x, y, z, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed):
    restype = None
    argtypes = [x_t, y_t, z_t]
    cfunc = c.glScalex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, z)

  # Check if the function actually exists
  f = c.glScalex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glScissor(x,
                y,
                width,
                height,
                x_t=GLint,
                y_t=GLint,
                width_t=GLsizei,
                height_t=GLsizei):
    restype = None
    argtypes = [x_t, y_t, width_t, height_t]
    cfunc = c.glScissor
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, width, height)

  # Check if the function actually exists
  f = c.glScissor
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glShadeModel(mode, mode_t=GLenum):
    restype = None
    argtypes = [mode_t]
    cfunc = c.glShadeModel
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mode)

  # Check if the function actually exists
  f = c.glShadeModel
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glStencilFunc(func, ref, mask, func_t=GLenum, ref_t=GLint,
                    mask_t=GLuint):
    restype = None
    argtypes = [func_t, ref_t, mask_t]
    cfunc = c.glStencilFunc
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(func, ref, mask)

  # Check if the function actually exists
  f = c.glStencilFunc
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glStencilMask(mask, mask_t=GLuint):
    restype = None
    argtypes = [mask_t]
    cfunc = c.glStencilMask
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(mask)

  # Check if the function actually exists
  f = c.glStencilMask
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glStencilOp(fail,
                  zfail,
                  zpass,
                  fail_t=GLenum,
                  zfail_t=GLenum,
                  zpass_t=GLenum):
    restype = None
    argtypes = [fail_t, zfail_t, zpass_t]
    cfunc = c.glStencilOp
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(fail, zfail, zpass)

  # Check if the function actually exists
  f = c.glStencilOp
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexCoordPointer(size,
                        type,
                        stride,
                        voidpointer,
                        size_t=GLint,
                        type_t=GLenum,
                        stride_t=GLsizei,
                        voidpointer_t=ctypes.c_void_p):
    restype = None
    argtypes = [size_t, type_t, stride_t, voidpointer_t]
    cfunc = c.glTexCoordPointer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(size, type, stride, voidpointer)

  # Check if the function actually exists
  f = c.glTexCoordPointer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnvi(target,
                pname,
                param,
                target_t=GLenum,
                pname_t=GLenum,
                param_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexEnvi
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexEnvi
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnvx(target,
                pname,
                param,
                target_t=GLenum,
                pname_t=GLenum,
                param_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexEnvx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexEnvx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnviv(target,
                 pname,
                 param0,
                 target_t=GLenum,
                 pname_t=GLenum,
                 param0_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexEnviv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexEnviv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexEnvxv(target,
                 pname,
                 param0,
                 target_t=GLenum,
                 pname_t=GLenum,
                 param0_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexEnvxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexEnvxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexImage2D(target,
                   level,
                   internalformat,
                   width,
                   height,
                   border,
                   format,
                   type,
                   voidpixels,
                   target_t=GLenum,
                   level_t=GLint,
                   internalformat_t=GLint,
                   width_t=GLsizei,
                   height_t=GLsizei,
                   border_t=GLint,
                   format_t=GLenum,
                   type_t=GLenum,
                   voidpixels_t=ctypes.c_void_p):
    restype = None
    argtypes = [
      target_t, level_t, internalformat_t, width_t, height_t, border_t,
      format_t, type_t, voidpixels_t
    ]
    cfunc = c.glTexImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, internalformat, width, height, border, format,
                 type, voidpixels)

  # Check if the function actually exists
  f = c.glTexImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameteri(target,
                      pname,
                      param,
                      target_t=GLenum,
                      pname_t=GLenum,
                      param_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexParameteri
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexParameteri
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameterx(target,
                      pname,
                      param,
                      target_t=GLenum,
                      pname_t=GLenum,
                      param_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param_t]
    cfunc = c.glTexParameterx
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param)

  # Check if the function actually exists
  f = c.glTexParameterx
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameteriv(target,
                       pname,
                       param0,
                       target_t=GLenum,
                       pname_t=GLenum,
                       param0_t=GLint):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexParameteriv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexParameteriv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexParameterxv(target,
                       pname,
                       param0,
                       target_t=GLenum,
                       pname_t=GLenum,
                       param0_t=GLfixed):
    restype = None
    argtypes = [target_t, pname_t, param0_t]
    cfunc = c.glTexParameterxv
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, pname, param0)

  # Check if the function actually exists
  f = c.glTexParameterxv
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTexSubImage2D(target,
                      level,
                      xoffset,
                      yoffset,
                      width,
                      height,
                      format,
                      type,
                      voidpixels,
                      target_t=GLenum,
                      level_t=GLint,
                      xoffset_t=GLint,
                      yoffset_t=GLint,
                      width_t=GLsizei,
                      height_t=GLsizei,
                      format_t=GLenum,
                      type_t=GLenum,
                      voidpixels_t=ctypes.c_void_p):
    restype = None
    argtypes = [
      target_t, level_t, xoffset_t, yoffset_t, width_t, height_t, format_t,
      type_t, voidpixels_t
    ]
    cfunc = c.glTexSubImage2D
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(target, level, xoffset, yoffset, width, height, format, type,
                 voidpixels)

  # Check if the function actually exists
  f = c.glTexSubImage2D
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glTranslatex(x, y, z, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed):
    restype = None
    argtypes = [x_t, y_t, z_t]
    cfunc = c.glTranslatex
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, z)

  # Check if the function actually exists
  f = c.glTranslatex
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glVertexPointer(size,
                      type,
                      stride,
                      voidpointer,
                      size_t=GLint,
                      type_t=GLenum,
                      stride_t=GLsizei,
                      voidpointer_t=ctypes.c_void_p):
    restype = None
    argtypes = [size_t, type_t, stride_t, voidpointer_t]
    cfunc = c.glVertexPointer
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(size, type, stride, voidpointer)

  # Check if the function actually exists
  f = c.glVertexPointer
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glViewport(x,
                 y,
                 width,
                 height,
                 x_t=GLint,
                 y_t=GLint,
                 width_t=GLsizei,
                 height_t=GLsizei):
    restype = None
    argtypes = [x_t, y_t, width_t, height_t]
    cfunc = c.glViewport
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(x, y, width, height)

  # Check if the function actually exists
  f = c.glViewport
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

try:

  def glPointSizePointerOES(type,
                            stride,
                            voidpointer,
                            type_t=GLenum,
                            stride_t=GLsizei,
                            voidpointer_t=ctypes.c_void_p):
    restype = None
    argtypes = [type_t, stride_t, voidpointer_t]
    cfunc = c.glPointSizePointerOES
    cfunc.restype = restype
    cfunc.argtypes = argtypes
    return cfunc(type, stride, voidpointer)

  # Check if the function actually exists
  f = c.glPointSizePointerOES
  del f
  loaded[0] += 1
except AttributeError as e:
  loaded[1] += 1
  if DEBUG > 0:
    print('could not load the function')
    print(e)

print(
  'Loaded %i functions and failed to load %i functions of %i functions in the header gl.h'
  % (loaded[0], loaded[1], sum(loaded)))

__all__ = [
  'glAlphaFunc', 'glClearColor', 'glClearDepthf', 'glClipPlanef', 'glColor4f',
  'glDepthRangef', 'glFogf', 'glFogfv', 'glFrustumf', 'glGetClipPlanef',
  'glGetFloatv', 'glGetLightfv', 'glGetMaterialfv', 'glGetTexEnvfv',
  'glGetTexParameterfv', 'glLightModelf', 'glLightModelfv', 'glLightf',
  'glLightfv', 'glLineWidth', 'glLoadMatrixf', 'glMaterialf', 'glMaterialfv',
  'glMultMatrixf', 'glMultiTexCoord4f', 'glNormal3f', 'glOrthof',
  'glPointParameterf', 'glPointParameterfv', 'glPointSize', 'glPolygonOffset',
  'glRotatef', 'glScalef', 'glTexEnvf', 'glTexEnvfv', 'glTexParameterf',
  'glTexParameterfv', 'glTranslatef', 'glActiveTexture', 'glAlphaFuncx',
  'glBindBuffer', 'glBindTexture', 'glBlendFunc', 'glBufferData',
  'glBufferSubData', 'glClear', 'glClearColorx', 'glClearDepthx',
  'glClearStencil', 'glClientActiveTexture', 'glClipPlanex', 'glColor4ub',
  'glColor4x', 'glColorMask', 'glColorPointer', 'glCompressedTexImage2D',
  'glCompressedTexSubImage2D', 'glCopyTexImage2D', 'glCopyTexSubImage2D',
  'glCullFace', 'glDeleteBuffers', 'glDeleteTextures', 'glDepthFunc',
  'glDepthMask', 'glDepthRangex', 'glDisable', 'glDisableClientState',
  'glDrawArrays', 'glDrawElements', 'glEnable', 'glEnableClientState',
  'glFinish', 'glFlush', 'glFogx', 'glFogxv', 'glFrontFace', 'glFrustumx',
  'glGetBooleanv', 'glGetBufferParameteriv', 'glGetClipPlanex', 'glGenBuffers',
  'glGenTextures', 'glGetError', 'glGetFixedv', 'glGetIntegerv',
  'glGetLightxv', 'glGetMaterialxv', 'glGetPointerv', 'glGetTexEnviv',
  'glGetTexEnvxv', 'glGetTexParameteriv', 'glGetTexParameterxv', 'glHint',
  'glIsBuffer', 'glIsEnabled', 'glIsTexture', 'glLightModelx',
  'glLightModelxv', 'glLightx', 'glLightxv', 'glLineWidthx', 'glLoadIdentity',
  'glLoadMatrixx', 'glLogicOp', 'glMaterialx', 'glMaterialxv', 'glMatrixMode',
  'glMultMatrixx', 'glMultiTexCoord4x', 'glNormal3x', 'glNormalPointer',
  'glOrthox', 'glPixelStorei', 'glPointParameterx', 'glPointParameterxv',
  'glPointSizex', 'glPolygonOffsetx', 'glPopMatrix', 'glPushMatrix',
  'glReadPixels', 'glRotatex', 'glSampleCoverage', 'glSampleCoveragex',
  'glScalex', 'glScissor', 'glShadeModel', 'glStencilFunc', 'glStencilMask',
  'glStencilOp', 'glTexCoordPointer', 'glTexEnvi', 'glTexEnvx', 'glTexEnviv',
  'glTexEnvxv', 'glTexImage2D', 'glTexParameteri', 'glTexParameterx',
  'glTexParameteriv', 'glTexParameterxv', 'glTexSubImage2D', 'glTranslatex',
  'glVertexPointer', 'glViewport', 'glPointSizePointerOES', '__gles1_gl_h_',
  'GL_VERSION_ES_CM_1_0', 'GL_VERSION_ES_CL_1_0', 'GL_VERSION_ES_CM_1_1',
  'GL_VERSION_ES_CL_1_1', 'GL_DEPTH_BUFFER_BIT', 'GL_STENCIL_BUFFER_BIT',
  'GL_COLOR_BUFFER_BIT', 'GL_FALSE', 'GL_TRUE', 'GL_POINTS', 'GL_LINES',
  'GL_LINE_LOOP', 'GL_LINE_STRIP', 'GL_TRIANGLES', 'GL_TRIANGLE_STRIP',
  'GL_TRIANGLE_FAN', 'GL_NEVER', 'GL_LESS', 'GL_EQUAL', 'GL_LEQUAL',
  'GL_GREATER', 'GL_NOTEQUAL', 'GL_GEQUAL', 'GL_ALWAYS', 'GL_ZERO', 'GL_ONE',
  'GL_SRC_COLOR', 'GL_ONE_MINUS_SRC_COLOR', 'GL_SRC_ALPHA',
  'GL_ONE_MINUS_SRC_ALPHA', 'GL_DST_ALPHA', 'GL_ONE_MINUS_DST_ALPHA',
  'GL_DST_COLOR', 'GL_ONE_MINUS_DST_COLOR', 'GL_SRC_ALPHA_SATURATE',
  'GL_CLIP_PLANE0', 'GL_CLIP_PLANE1', 'GL_CLIP_PLANE2', 'GL_CLIP_PLANE3',
  'GL_CLIP_PLANE4', 'GL_CLIP_PLANE5', 'GL_FRONT', 'GL_BACK',
  'GL_FRONT_AND_BACK', 'GL_FOG', 'GL_LIGHTING', 'GL_TEXTURE_2D',
  'GL_CULL_FACE', 'GL_ALPHA_TEST', 'GL_BLEND', 'GL_COLOR_LOGIC_OP',
  'GL_DITHER', 'GL_STENCIL_TEST', 'GL_DEPTH_TEST', 'GL_POINT_SMOOTH',
  'GL_LINE_SMOOTH', 'GL_SCISSOR_TEST', 'GL_COLOR_MATERIAL', 'GL_NORMALIZE',
  'GL_RESCALE_NORMAL', 'GL_VERTEX_ARRAY', 'GL_NORMAL_ARRAY', 'GL_COLOR_ARRAY',
  'GL_TEXTURE_COORD_ARRAY', 'GL_MULTISAMPLE', 'GL_SAMPLE_ALPHA_TO_COVERAGE',
  'GL_SAMPLE_ALPHA_TO_ONE', 'GL_SAMPLE_COVERAGE', 'GL_NO_ERROR',
  'GL_INVALID_ENUM', 'GL_INVALID_VALUE', 'GL_INVALID_OPERATION',
  'GL_STACK_OVERFLOW', 'GL_STACK_UNDERFLOW', 'GL_OUT_OF_MEMORY', 'GL_EXP',
  'GL_EXP2', 'GL_FOG_DENSITY', 'GL_FOG_START', 'GL_FOG_END', 'GL_FOG_MODE',
  'GL_FOG_COLOR', 'GL_CW', 'GL_CCW', 'GL_CURRENT_COLOR', 'GL_CURRENT_NORMAL',
  'GL_CURRENT_TEXTURE_COORDS', 'GL_POINT_SIZE', 'GL_POINT_SIZE_MIN',
  'GL_POINT_SIZE_MAX', 'GL_POINT_FADE_THRESHOLD_SIZE',
  'GL_POINT_DISTANCE_ATTENUATION', 'GL_SMOOTH_POINT_SIZE_RANGE',
  'GL_LINE_WIDTH', 'GL_SMOOTH_LINE_WIDTH_RANGE', 'GL_ALIASED_POINT_SIZE_RANGE',
  'GL_ALIASED_LINE_WIDTH_RANGE', 'GL_CULL_FACE_MODE', 'GL_FRONT_FACE',
  'GL_SHADE_MODEL', 'GL_DEPTH_RANGE', 'GL_DEPTH_WRITEMASK',
  'GL_DEPTH_CLEAR_VALUE', 'GL_DEPTH_FUNC', 'GL_STENCIL_CLEAR_VALUE',
  'GL_STENCIL_FUNC', 'GL_STENCIL_VALUE_MASK', 'GL_STENCIL_FAIL',
  'GL_STENCIL_PASS_DEPTH_FAIL', 'GL_STENCIL_PASS_DEPTH_PASS', 'GL_STENCIL_REF',
  'GL_STENCIL_WRITEMASK', 'GL_MATRIX_MODE', 'GL_VIEWPORT',
  'GL_MODELVIEW_STACK_DEPTH', 'GL_PROJECTION_STACK_DEPTH',
  'GL_TEXTURE_STACK_DEPTH', 'GL_MODELVIEW_MATRIX', 'GL_PROJECTION_MATRIX',
  'GL_TEXTURE_MATRIX', 'GL_ALPHA_TEST_FUNC', 'GL_ALPHA_TEST_REF',
  'GL_BLEND_DST', 'GL_BLEND_SRC', 'GL_LOGIC_OP_MODE', 'GL_SCISSOR_BOX',
  'GL_COLOR_CLEAR_VALUE', 'GL_COLOR_WRITEMASK', 'GL_MAX_LIGHTS',
  'GL_MAX_CLIP_PLANES', 'GL_MAX_TEXTURE_SIZE', 'GL_MAX_MODELVIEW_STACK_DEPTH',
  'GL_MAX_PROJECTION_STACK_DEPTH', 'GL_MAX_TEXTURE_STACK_DEPTH',
  'GL_MAX_VIEWPORT_DIMS', 'GL_MAX_TEXTURE_UNITS', 'GL_SUBPIXEL_BITS',
  'GL_RED_BITS', 'GL_GREEN_BITS', 'GL_BLUE_BITS', 'GL_ALPHA_BITS',
  'GL_DEPTH_BITS', 'GL_STENCIL_BITS', 'GL_POLYGON_OFFSET_UNITS',
  'GL_POLYGON_OFFSET_FILL', 'GL_POLYGON_OFFSET_FACTOR',
  'GL_TEXTURE_BINDING_2D', 'GL_VERTEX_ARRAY_SIZE', 'GL_VERTEX_ARRAY_TYPE',
  'GL_VERTEX_ARRAY_STRIDE', 'GL_NORMAL_ARRAY_TYPE', 'GL_NORMAL_ARRAY_STRIDE',
  'GL_COLOR_ARRAY_SIZE', 'GL_COLOR_ARRAY_TYPE', 'GL_COLOR_ARRAY_STRIDE',
  'GL_TEXTURE_COORD_ARRAY_SIZE', 'GL_TEXTURE_COORD_ARRAY_TYPE',
  'GL_TEXTURE_COORD_ARRAY_STRIDE', 'GL_VERTEX_ARRAY_POINTER',
  'GL_NORMAL_ARRAY_POINTER', 'GL_COLOR_ARRAY_POINTER',
  'GL_TEXTURE_COORD_ARRAY_POINTER', 'GL_SAMPLE_BUFFERS', 'GL_SAMPLES',
  'GL_SAMPLE_COVERAGE_VALUE', 'GL_SAMPLE_COVERAGE_INVERT',
  'GL_NUM_COMPRESSED_TEXTURE_FORMATS', 'GL_COMPRESSED_TEXTURE_FORMATS',
  'GL_DONT_CARE', 'GL_FASTEST', 'GL_NICEST', 'GL_PERSPECTIVE_CORRECTION_HINT',
  'GL_POINT_SMOOTH_HINT', 'GL_LINE_SMOOTH_HINT', 'GL_FOG_HINT',
  'GL_GENERATE_MIPMAP_HINT', 'GL_LIGHT_MODEL_AMBIENT',
  'GL_LIGHT_MODEL_TWO_SIDE', 'GL_AMBIENT', 'GL_DIFFUSE', 'GL_SPECULAR',
  'GL_POSITION', 'GL_SPOT_DIRECTION', 'GL_SPOT_EXPONENT', 'GL_SPOT_CUTOFF',
  'GL_CONSTANT_ATTENUATION', 'GL_LINEAR_ATTENUATION',
  'GL_QUADRATIC_ATTENUATION', 'GL_BYTE', 'GL_UNSIGNED_BYTE', 'GL_SHORT',
  'GL_UNSIGNED_SHORT', 'GL_FLOAT', 'GL_FIXED', 'GL_CLEAR', 'GL_AND',
  'GL_AND_REVERSE', 'GL_COPY', 'GL_AND_INVERTED', 'GL_NOOP', 'GL_XOR', 'GL_OR',
  'GL_NOR', 'GL_EQUIV', 'GL_INVERT', 'GL_OR_REVERSE', 'GL_COPY_INVERTED',
  'GL_OR_INVERTED', 'GL_NAND', 'GL_SET', 'GL_EMISSION', 'GL_SHININESS',
  'GL_AMBIENT_AND_DIFFUSE', 'GL_MODELVIEW', 'GL_PROJECTION', 'GL_TEXTURE',
  'GL_ALPHA', 'GL_RGB', 'GL_RGBA', 'GL_LUMINANCE', 'GL_LUMINANCE_ALPHA',
  'GL_UNPACK_ALIGNMENT', 'GL_PACK_ALIGNMENT', 'GL_UNSIGNED_SHORT_4_4_4_4',
  'GL_UNSIGNED_SHORT_5_5_5_1', 'GL_UNSIGNED_SHORT_5_6_5', 'GL_FLAT',
  'GL_SMOOTH', 'GL_KEEP', 'GL_REPLACE', 'GL_INCR', 'GL_DECR', 'GL_VENDOR',
  'GL_RENDERER', 'GL_VERSION', 'GL_EXTENSIONS', 'GL_MODULATE', 'GL_DECAL',
  'GL_ADD', 'GL_TEXTURE_ENV_MODE', 'GL_TEXTURE_ENV_COLOR', 'GL_TEXTURE_ENV',
  'GL_NEAREST', 'GL_LINEAR', 'GL_NEAREST_MIPMAP_NEAREST',
  'GL_LINEAR_MIPMAP_NEAREST', 'GL_NEAREST_MIPMAP_LINEAR',
  'GL_LINEAR_MIPMAP_LINEAR', 'GL_TEXTURE_MAG_FILTER', 'GL_TEXTURE_MIN_FILTER',
  'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', 'GL_GENERATE_MIPMAP',
  'GL_TEXTURE0', 'GL_TEXTURE1', 'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_TEXTURE4',
  'GL_TEXTURE5', 'GL_TEXTURE6', 'GL_TEXTURE7', 'GL_TEXTURE8', 'GL_TEXTURE9',
  'GL_TEXTURE10', 'GL_TEXTURE11', 'GL_TEXTURE12', 'GL_TEXTURE13',
  'GL_TEXTURE14', 'GL_TEXTURE15', 'GL_TEXTURE16', 'GL_TEXTURE17',
  'GL_TEXTURE18', 'GL_TEXTURE19', 'GL_TEXTURE20', 'GL_TEXTURE21',
  'GL_TEXTURE22', 'GL_TEXTURE23', 'GL_TEXTURE24', 'GL_TEXTURE25',
  'GL_TEXTURE26', 'GL_TEXTURE27', 'GL_TEXTURE28', 'GL_TEXTURE29',
  'GL_TEXTURE30', 'GL_TEXTURE31', 'GL_ACTIVE_TEXTURE',
  'GL_CLIENT_ACTIVE_TEXTURE', 'GL_REPEAT', 'GL_CLAMP_TO_EDGE', 'GL_LIGHT0',
  'GL_LIGHT1', 'GL_LIGHT2', 'GL_LIGHT3', 'GL_LIGHT4', 'GL_LIGHT5', 'GL_LIGHT6',
  'GL_LIGHT7', 'GL_ARRAY_BUFFER', 'GL_ELEMENT_ARRAY_BUFFER',
  'GL_ARRAY_BUFFER_BINDING', 'GL_ELEMENT_ARRAY_BUFFER_BINDING',
  'GL_VERTEX_ARRAY_BUFFER_BINDING', 'GL_NORMAL_ARRAY_BUFFER_BINDING',
  'GL_COLOR_ARRAY_BUFFER_BINDING', 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING',
  'GL_STATIC_DRAW', 'GL_DYNAMIC_DRAW', 'GL_BUFFER_SIZE', 'GL_BUFFER_USAGE',
  'GL_SUBTRACT', 'GL_COMBINE', 'GL_COMBINE_RGB', 'GL_COMBINE_ALPHA',
  'GL_RGB_SCALE', 'GL_ADD_SIGNED', 'GL_INTERPOLATE', 'GL_CONSTANT',
  'GL_PRIMARY_COLOR', 'GL_PREVIOUS', 'GL_OPERAND0_RGB', 'GL_OPERAND1_RGB',
  'GL_OPERAND2_RGB', 'GL_OPERAND0_ALPHA', 'GL_OPERAND1_ALPHA',
  'GL_OPERAND2_ALPHA', 'GL_ALPHA_SCALE', 'GL_SRC0_RGB', 'GL_SRC1_RGB',
  'GL_SRC2_RGB', 'GL_SRC0_ALPHA', 'GL_SRC1_ALPHA', 'GL_SRC2_ALPHA',
  'GL_DOT3_RGB', 'GL_DOT3_RGBA', 'GL_OES_compressed_paletted_texture',
  'GL_PALETTE4_RGB8_OES', 'GL_PALETTE4_RGBA8_OES', 'GL_PALETTE4_R5_G6_B5_OES',
  'GL_PALETTE4_RGBA4_OES', 'GL_PALETTE4_RGB5_A1_OES', 'GL_PALETTE8_RGB8_OES',
  'GL_PALETTE8_RGBA8_OES', 'GL_PALETTE8_R5_G6_B5_OES', 'GL_PALETTE8_RGBA4_OES',
  'GL_PALETTE8_RGB5_A1_OES', 'GL_OES_point_size_array',
  'GL_POINT_SIZE_ARRAY_OES', 'GL_POINT_SIZE_ARRAY_TYPE_OES',
  'GL_POINT_SIZE_ARRAY_STRIDE_OES', 'GL_POINT_SIZE_ARRAY_POINTER_OES',
  'GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES', 'GL_OES_point_sprite',
  'GL_POINT_SPRITE_OES', 'GL_COORD_REPLACE_OES', 'GL_OES_read_format',
  'GL_IMPLEMENTATION_COLOR_READ_TYPE_OES',
  'GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES', 'GLchar', 'GLenum', 'GLboolean',
  'GLbitfield', 'GLbyte', 'GLshort', 'GLint', 'GLint64', 'GLsizei', 'GLubyte',
  'GLushort', 'GLuint', 'GLfloat', 'GLclampf', 'GLfixed', 'GLintptr',
  'GLsizeiptr', 'GLclampx', 'void', 'GLvoid', 'GLsync', 'GLeglImageOES',
  'GLDEBUGPROCKHR', 'GLuint64'
]

