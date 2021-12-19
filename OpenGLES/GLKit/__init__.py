# coding: utf-8

import ui
import ctypes
import weakref
# from objc_util import *

from OpenGLES.GLKit.view import GLKViewDelegate, setRenderEngine, getRenderEngine, GLKView
from OpenGLES.GLKit.effect import *
#from view import *
from OpenGLES.GLKit.glkmath import *
from OpenGLES.GLKit.fog import *
from OpenGLES.GLKit.light import *
from OpenGLES.GLKit.texture import *
from OpenGLES.GLKit.material import *


# ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/GLKit.framework").load()

__all__ = ["GLKView", "GLKViewDelegate", "setRenderEngine", "getRenderEngine"]

if __name__ == "__main__":
  from OpenGLES.GLKit.view import GKLViewController,GLKViewControllerDelegate, TouchController

  v = GLKView(frame=(0, 0, 800, 600))
  d = GLKViewDelegate()
  vc = GKLViewController("GLKit Demo", v)
  vcd = GLKViewControllerDelegate()
  vc.delegate = vcd
  t = TouchController()
  t.present(debug=True)
  # print v
  # print d
  # print vc
  # print vcd
