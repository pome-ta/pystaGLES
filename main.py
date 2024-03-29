import time
import sys
import copy
import random

import ui
from objc_util import on_main_thread

import OpenGLES.Util
import OpenGLES.Util.Model
import OpenGLES.Util.Shader
import OpenGLES.GLES as GLES
import OpenGLES.EAGL as EAGL
import OpenGLES.Util as Util
import OpenGLES.GLKit as GLKit
from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.Util import Physics
import OpenGLES.Util.LightsCameras as LightsCameras
from OpenGLES.Util.LightsCameras import PhysicsCamera
import OpenGLES.GLKit.texture as texture
from OpenGLES.GLKit.glkmath import matrix4 as m4
from OpenGLES.GLKit.glkmath import vector3 as v3

OpenGLES.Util.Physics.resetPhysicsWorld()
PhysicsWorld = OpenGLES.Util.Physics.getPhysicsWorld()

LightsCameras.setPhysicsWorld(PhysicsWorld)
Util.Model.setPhysicsWorld(PhysicsWorld)

MAX_DIST = 50

with open("shader.vs", "rb") as f:
  VERTEX_SHADER_SOURCE = f.read()

with open("shader.fs", "rb") as f:
  FRAGMENT_SHADER_SOURCE = f.read()
glviewv = GLKit.GLKView(frame=(0, 0, 800, 600))

at_front = False


def physics_info(sender):
  global at_front
  global PhysicsWorld
  if at_front:
    PhysicsWorld.js.send_to_back()
    at_front = False
  else:
    PhysicsWorld.js.bring_to_front()
    at_front = True


btn = ui.ButtonItem()
btn.title = "Physics Info"
btn.action = physics_info


def change(sender):
  glviewv.tc.accelerometer_speed = 1 + sender.value * 5


setting_front = False
setting_view = ui.View()
setting_view.background_color = '#FFFFFF'
setting_view.width = 800
setting_view.height = 300
accelerometer_speed = ui.Slider()
accelerometer_speed.action = change
accelerometer_speed.continuous = True
setting_view.add_subview(accelerometer_speed)


def settings(sender):
  global setting_front
  if setting_front:
    setting_front = False
    setting_view.send_to_back()
  else:
    setting_front = True
    setting_view.bring_to_front()


sbtn = ui.ButtonItem()
sbtn.image = ui.Image.named('iob:ios7_gear_outline_32')
sbtn.action = settings
glviewv.left_button_items = [btn, sbtn]


class Renderer(Util.RenderCycle):
  def __init__(self):
    Util.RenderCycle.__init__(self)

    self.objects = []
    for x in range(-10, 10, 4):
      for y in range(10, 14, 4):
        for z in range(-10, 10, 4):
          o1 = Util.Model.PhysicsObject("test_model.xml",
                                        v3.GLKVector3Make(x, y, z))
          self.objects.append(o1)

    for _ in range(0, 25):
      o1 = Util.Model.PhysicsObject("test_model.xml",
                                    v3.GLKVector3Make(0, 0, 0))
      self.objects.append(o1)

    o1 = Util.Model.XMLModel("plane.xml", v3.GLKVector3Make(-20, 0, -20))
    o1.model = m4.GLKMatrix4Scale(o1.model, 100, 100, 100)
    self.objects.append(o1)

    self.v = Util.Shader.ShaderSource(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
    self.f = Util.Shader.ShaderSource(FRAGMENT_SHADER_SOURCE,
                                      GL_FRAGMENT_SHADER)
    self.sp = Util.Shader.ShaderProgram(self.v, self.f)

    self.eye = PhysicsCamera(v3.GLKVector3Make(-20, 10, -20), yaw=0, pitch=0)

    self.projection = m4.GLKMatrix4MakePerspective(45.0, 800.0 / 600.0, 0.1,
                                                   1000.0)
    self.view = self.eye.view
    self.model = m4.GLKMatrix4Identity()

    self.rt = 0
    self.ut = 0

    self.texture = None

    glviewv.add_subview(setting_view)
    setting_view.send_to_back()

  def setup(self, context):
    if EAGL.setCurrentContext(context):
      self.sp.build()
      self.sp.bind()

      #self.texture = texture.loadTexture('test.png', 0)

      print(len(self.objects), " object/s in the world")
      for rObj in self.objects:
        rObj.setup_object()

      glEnable(GL_CULL_FACE)
      glCullFace(GL_BACK)
      glEnable(GL_DEPTH_TEST)
      glDepthFunc(GL_LESS)
      glViewport(0, 0, int(glviewv.width * 2), int(glviewv.height * 2))

      glClearColor(0.1, 0.12, 0.45, 1.0)

      PhysicsWorld.js.eval_js('startUpdates();')
      glviewv.add_subview(PhysicsWorld.js)
      PhysicsWorld.js.send_to_back()
    else:
      print("Could not Setup OpenGLES")
    self.last = time.clock()

  def teardown(self):
    self.sp.teardown()
    EAGL.setCurrentContext(None)
    PhysicsWorld.js.eval_js('done();')

  def update(self, dt):
    start = time.clock()
    end = time.clock()
    # glviewv.name = "FPS: %i. Frames: %s" % (self.fps, self.framesDisplayed)
    glviewv.name = "Render Time: %.3f\tUpdate Time: %.3f\tFrames: %i\tFPS: %i" % (
      self.rt, self.ut, self.framesDisplayed, self.fps)
    su = time.clock()
    for rObj in self.objects:
      so = time.clock()
      if rObj.distance_from_point(self.eye.position) < MAX_DIST:
        rObj.update(dt)
        rObj.renderable = True
      else:
        rObj.renderable = False
      eo = time.clock()
    eu = time.clock()
    self.eye.update(dt)
    self.view = self.eye.view

    end = time.clock()
    self.ut = end - start

  def move_f(self, mdir):
    mdir = [mdir[1], mdir[0]]
    self.eye.move(*mdir)

  def look_f(self, ldir):
    self.eye.look(*ldir)

  def render(self, context):
    start = time.clock()

    if EAGL.setCurrentContext(context):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glViewport(0, 0, int(glviewv.width * 2), int(glviewv.height * 2))
      self.sp.bind()
      self.sp.uniform4x4("V", list(self.view.s1.m))
      self.sp.uniform4x4("P", list(self.projection.s1.m))
      for rObj in self.objects:
        rObj.render(self.sp)
      self.eye.debug_draw(self.sp)
    else:
      raise RuntimeError('Render Failed as context could not be set.')
    end = time.clock()
    # print 'render', (end - self.last)
    self.rt = end - start
    self.last = end


@on_main_thread
def main():
  from ui import Image
  i = Image.named('test:Lenna')
  with open('test.png', 'wb') as f:
    f.write(i.to_png())

  contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES2)
  GLKit.setRenderEngine(Renderer())
  glviewv.setDelegate(GLKit.GLKViewDelegate())
  glviewv.setContext(contextc)
  glviewv.present("sheet")


if __name__ == '__main__':
  main()

