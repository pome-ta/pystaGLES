# coding: utf-8
"""
OpenGLES.Util.__init__.py
Utilities Module
This module contains most of the commonly required and most
used components that are not a part of OpenGLES, GLKit or EAGL.
"""
import ctypes
from objc_util import *
import math

#from GLES.gles1 import *
#from OpenGLES.GLES.gles2 import *
#from OpenGLES.GLES.gles3 import *
#from OpenGLES.GLES.headers.GLConstants import *
# import euclid

from OpenGLES.GLKit.glkmath import vector3 as v3
#from OpenGLES.GLKit.glkmath import matrix4 as m4

__all__ = [
  "RenderCycle", "RenderObject", "LookObject", "Model", "Shader", "Physics"
]


class RenderCycle(object):
  def __init__(self):
    """
        Base Class to Handle Input, Update and Render. Should be overrided
        Attributes:
            fps (int): The frames per second. This is generated by GLKitViewController.
            framesDisplayed (int): The number of frames that have been displayed since
                                   a GLKView was created and started to render.
        """
    self.fps = 0
    self.framesDisplayed = 0

  def teardown(self):
    """
        Called Just before the programs exists to give you a chance to get rid of
        any unused data.
        """
    raise NotImplementedError

  def render(self, context):
    """
        Called every time a frame is to be rendered
        Args:
            context (OpenGLES.EAGL.EAGLContext): The current rendering context
        """
    raise NotImplementedError

  def update(self, dt):
    """
        Called before every frame is rendered
        Args:
            dt (int): the time since the last update
        """
    raise NotImplementedError

  def setup(self, context):
    """
        Called only once to set OpenGLES up before rendering occures
        Args:
            context (OpenGLES.EAGL.EAGLContext): The current rendering context
        """
    raise NotImplementedError

  def move_f(self, mdir):
    """
        Args:
            mdir (list[int]): A list in the form of [x,y] to represent the up/down
                              left/right movement
        """
    raise NotImplementedError

  def look_f(self, ldir):
    """
        Args:
            ldir (list[int]): A list in the form of [x,y] to represent the up/down
                              left/right movement
        """
    raise NotImplementedError


class RenderObject(object):
  def __init__(self, pos, vertices=[], colour=[], uv=[], indices=[]):
    """
        Base Class for a rendering object.
        Look at OpenGLES.Util.Model.XMLModel or OpenGLES.Util.Model.PhysicsObject
        Args:
            pos (list[float]): The starting position in the form [x,y,z]
            vertices (Optional[list[float]]): The vertex array of the object
            colour (Optional[list[float]]): The colour array of the object
                                            NOT YET IMPLIMENTED
            uv (Optional[list[float]]): The uv array of the object
                                        NOT YET IMPLIMENTED
            indices (Optional[list[float]]): The indices array of the object
                                             NOT YET IMPLIMENTED
        Attributes:
            vVertices (OpenGLES.GLES.headers.GLConstants.GLfloat): An array of the verticies
            vSize (int): The size of vVertices
            model (euclid.Matrix4): The model matrix of the MVP
            renderable (bool): If true object should be rendered
        """
    self.vVertices = (GLfloat * len(vertices))(*vertices)
    self.vSize = len(vertices)
    self.cItems = (GLfloat * len(colour))(*colour)
    self.cSize = len(colour)
    self.uItems = (GLfloat * len(uv))(*uv)
    self.uSize = len(uv)
    self.IItems = (GLfloat * len(indices))(*indices)
    self.ISize = len(indices)
    self.model = m4.GLKMatrix4MakeTranslation(pos.x, pos.y, pos.z)
    # self.model = euclid.Matrix4.new_identity()
    # self.model.translate(*list(pos))
    self.renderable = True

  def setup_object(self):
    """
        Called once to initialise the object for rendering
        """
    pass

  def teardown(self):
    """
        Called once at the end before termination do delete unused attributes
        """
    pass

  def distance_from_point(self, point):
    # p2 = euclid.Point3(*point)
    # p1 = euclid.Point3(self.model.d, self.model.h, self.model.l)
    # p1 = p1.distance(p2)
    return 10  # p1

  def render(self, sp):
    """
        Called every time the scene needs to be rendered
        Args:
            sp (OpenGLES.Util.Shader.ShaderProgram): the currently bound shader program
                                                     to pass the model matrix to.
        """
    if self.renderable:
      sp.uniform4x4("M", list(self.model.s1.m))
      glVertexAttribPointer(
        0,
        3,
        GL_FLOAT,
        GL_FALSE,
        0,
        self.vVertices,
        voidpointer_t=(GLfloat * self.vSize))
      glEnableVertexAttribArray(0)
      glDrawArrays(GL_TRIANGLES, 0, self.vSize / 3)

  def update(self, dt):
    """
        Called before every scene render
        Args:
            dt (int): Time since the last update
        """
    pass


class LookObject(object):
  def __init__(self,
               position=v3.GLKVector3Make(0, 0, 0),
               up=v3.GLKVector3Make(0, 1, 0),
               yaw=0.0,
               pitch=0.0):
    """
        A simple camera class, for a basic fly camera.
        Uses similar math to gluLookAt
        Args:
            position (Optional[euclid.Vector3]): The initial position for the camera
            up (Optional[euclid.Vector3]): World up
            yaw (Optional[float]): Initial yaw of the camera
            pitch (Optional[float]): Initial pitch of the camera
        Attributes:
            camera_id (int): The physics object camera id (see OpenGLES.Util.LightsCameras.PhysicsCamera)
            position (euclid.Vector3): The position of the camera
            worldup (euclid.Vector3): The world up direction (default euclid.Vector(0,1,0))
            up (euclid.Vector3): Up direction relative to the world and the camera
            front (euclid.Vector3): Front facing direction of the camera
            right (euclid.Vector3): right facing direction of the camera
            yaw (float): camera yaw (default 0.0)
            pitch (float): camera pitch (default 0.0)
            strafe (list[int]): Strafe direction in the format [x,y]
            speed (float): The speed the camera moves at
        """
    self.camera_id = None
    self.position = position
    self.worldup = up
    self.up = v3.GLKVector3Make(0, 0, 0)
    self.front = v3.GLKVector3Make(0, 0, -1)
    self.right = v3.GLKVector3Make(0, 0, 0)
    self.yaw = yaw
    self.pitch = pitch
    self.strafe = [0, 0]
    self.speed = 10.0

    self.update(0)

  @property
  def view(self):
    """
        Returns:
            (euclid.Matrix4): The view matrix to be applied to a MVP
        """
    p = self.position
    p.y += 1.0
    e = v3.GLKVector3Add(p, self.front)
    u = self.up
    res = m4.GLKMatrix4MakeLookAt(p.x, p.y, p.z, e.x, e.y, e.z, u.x, u.y, u.z)
    # res = euclid.Matrix4.new_look_at(p, p + self.front, self.up)
    return res

  def look(self, dx, dy):
    """
        Set the yaw and pitch of a camera
        Args:
            dx (float): The new yaw to be subtracted from the old yaw
            dy (float): The new pitch to be added to the old pitch
        """
    self.yaw -= dx
    self.yaw %= 360
    self.pitch += dy
    if self.pitch > 89.0:
      self.pitch = 89.0
    elif self.pitch < -89.0:
      self.pitch = -89.0

  def move(self, dx, dy):
    """
        Set strafe values
        Args:
            dx (int): The new strafe x value
            dy (int): The new negative strafe y value
        """
    self.strafe = [dx, -dy]

  def update(self, dt):
    """
        Called before every scene is rendered
        Args:
            dt (int): The time since the last update
        """
    self.front = v3.GLKVector3MultiplyScalar(
      v3.GLKVector3Make(
        math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
        math.sin(math.radians(self.pitch)),
        math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))),
      1)

    self.right = v3.GLKVector3CrossProduct(self.front, self.worldup)
    # self.right = self.front.cross(self.worldup)
    self.up = v3.GLKVector3CrossProduct(self.right, self.front)
    # self.up = self.right.cross(self.front)

    speed = dt * self.speed

    if self.strafe[0] != 0:
      self.position = v3.GLKVector3Add(self.position,
                                       v3.GLKVector3MultiplyScalar(
                                         self.front, speed * self.strafe[0]))
      # self.position += self.front * speed * self.strafe[0]
    if self.strafe[1] != 0:
      self.position = v3.GLKVector3Add(self.position,
                                       v3.GLKVector3MultiplyScalar(
                                         self.right, speed * self.strafe[1]))
      # self.position += self.right * speed * self.strafe[1]


if __name__ == "__main__":
  c = LookObject()
  print(c.front)
  print(c.right)
  c.look(10, 20)
  c.move(10, 20)
  c.update(10)
  print(c.front)
  print(c.right)
  print(c.view)

  print(list(c.view.s1.m))

