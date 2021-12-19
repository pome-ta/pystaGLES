# coding: utf-8
import ctypes
from objc_util import ObjCClass
#import OpenGLES.GLKit.glkmath as GLKMath
from OpenGLES.GLKit.glkmath.vector4 import setGLKVector4, getGLKVector4



class GLKEffectPropertyMaterial:
  def __init__(self, c_mat=None):
    if c_mat is None:
      self._mat = ObjCClass('GLKEffectPropertyMaterial').alloc().init()
      print(dir(self._mat))
    else:
      self._mat = c_mat

  def __str__(self):
    return str(self._mat.description())

  def setAmbientColor(self, color):
    return setGLKVector4(self._mat.setAmbientColor_, color)

  def getAmbientColor(self):
    return getGLKVector4(self._mat.ambientColor)

  ambientColor = property(getAmbientColor, setAmbientColor)

  def setDiffuseColor(self, color):
    return setGLKVector4(self._mat.setDiffuseColor_, color)

  def getDiffuseColor(self):
    return getGLKVector4(self._mat.diffuseColor)

  diffuseColor = property(getDiffuseColor, setDiffuseColor)

  def setEmissiveColor(self, color):
    return setGLKVector4(self._mat.setEmissiveColor_, color)

  def getEmissiveColor(self):
    return getGLKVector4(self._mat.emissiveColor)

  emissiveColor = property(getEmissiveColor, setEmissiveColor)

  def setSpecularColor(self, color):
    return setGLKVector4(self._mat.setSpecularColor_, color)

  def getSpecularColor(self):
    return getGLKVector4(self._mat.specularColor)

  specularColor = property(getSpecularColor, setSpecularColor)


__all__ = ['GLKEffectPropertyMaterial']

if __name__ == '__main__':
  m = GLKEffectPropertyMaterial()
  m.ambientColor = GLKVector4(r=0.0, g=1.0, b=0.5, a=0.2)
  print('ambientColor', m.ambientColor)
  print('diffuseColor', m.diffuseColor)
  print('emissiveColor', m.emissiveColor)
  print('specularColor', m.specularColor)

