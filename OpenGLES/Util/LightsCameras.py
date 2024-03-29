# coding: utf-8
import math
# import euclid
from OpenGLES.Util import LookObject
from OpenGLES.Util.Model import XMLModel
from OpenGLES.GLKit.glkmath import vector3 as v3
from OpenGLES.GLKit.glkmath import matrix4 as m4
from OpenGLES.GLKit.glkmath import matrix3 as m3
from OpenGLES.GLKit.glkmath import quaternion as quat

__all__ = ['setPhysicsWorld', 'Light', 'PhysicsCamera']

_PhysicsWorld = None


def setPhysicsWorld(pw):
  global _PhysicsWorld
  _PhysicsWorld = pw


class PhysicsCamera(LookObject):
  def __init__(self, position=v3.GLKVector3Make(0, 0, 0), up=v3.GLKVector3Make(0, 1, 0), yaw=0.0, pitch=0.0):
    self.camera_id = None
    self.debug_model = None
    LookObject.__init__(self, position, up, yaw, pitch)
    self.camera_id = _PhysicsWorld.add_camera(self)
    print("Camera ID:", self.camera_id)
    self.debug_model = XMLModel(__file__.replace('LightsCameras.py', '../test_model.xml'))
    self.update(0)

  @property
  def view(self):
    """
    Returns:
        (euclid.Matrix4): The view matrix to be applied to a MVP
    """
    pos = self.position
    p = v3.GLKVector3Make(pos.x, pos.y + 1, pos.z)
    e = v3.GLKVector3Add(p, self.front)
    u = self.up
    return m4.GLKMatrix4MakeLookAt(p.x, p.y, p.z, e.x, e.y, e.z, u.x, u.y, u.z)

  def debug_draw(self, sp):
    if self.debug_model:
      self.debug_model.render(sp)

  def update(self, dt):
    self.front = v3.GLKVector3MultiplyScalar(
      v3.GLKVector3Make(math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
                        math.sin(math.radians(self.pitch)),
                        math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))), 1)

    self.right = v3.GLKVector3CrossProduct(self.front, self.worldup)
    self.up = v3.GLKVector3CrossProduct(self.right, self.front)

    if self.camera_id:
      (npos, nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
      position = npos
      speed = dt * self.speed
      if self.strafe[0] != 0:
        position = v3.GLKVector3Add(position,
                                    v3.GLKVector3MultiplyScalar(self.front, speed * self.strafe[0]))
      if self.strafe[1] != 0:
        position = v3.GLKVector3Add(position,
                                    v3.GLKVector3MultiplyScalar(self.right, speed * self.strafe[1]))

      (npos, nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
      _PhysicsWorld.js.eval_js('set_object_pos(%i, %f, %f, %f);' % (
        self.camera_id,
        position.x,
        npos.y,
        position.z))
      # I don't like how rotations are handled.
      # They should pay more attention to what is happening in the physics environment as well.
      rotation_matrix = m3.GLKMatrix3MakeWithQuaternion(nrot)
      r = math.radians(-self.yaw)
      q = quat.GLKQuaternionMakeWithMatrix3(m3.GLKMatrix3MakeZRotation(r))
      _PhysicsWorld.js.eval_js('set_object_rot(%i, %f, %f, %f, %f);' % (self.camera_id, q.w, q.x, q.y, q.z))
      (npos, nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
      position = npos
      self.position = position
      if self.debug_model:
        nmodel = m4.GLKMatrix4MakeTranslation(*position.v)
        nmodel = m4.GLKMatrix4Multiply(nmodel, m4.GLKMatrix4MakeWithQuaternion(q))
        self.debug_model.model = nmodel
    else:
      speed = dt * self.speed
      if self.strafe[0] != 0:
        self.position = v3.GLKVector3Add(self.position,
                                         v3.GLKVector3MultiplyScalar(self.front, speed * self.strafe[0]))
        # self.position += self.front * speed * self.strafe[0]
      if self.strafe[1] != 0:
        self.position = v3.GLKVector3Add(self.position,
                                         v3.GLKVector3MultiplyScalar(self.right, speed * self.strafe[1]))
        # self.position += self.right * speed * self.strafe[1]
    if self.debug_model:
      self.debug_model.update(dt)


if __name__ == '__main__':
  import OpenGLES.Util.Physics

  reload(OpenGLES.Util.Physics)
  _PhysicsWorld = OpenGLES.Util.Physics.getPhysicsWorld()
  c = PhysicsCamera(v3.GLKVector3Make(10, 10, 10))
  c.update(123)

  print(c.view)
