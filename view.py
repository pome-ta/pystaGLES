from objc_util import ObjCClass, on_main_thread, CGRect, CGPoint, CGSize
import ui


GLKView_OBJC = ObjCClass('GLKView')

class GLKView(ui.View):
  @on_main_thread
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    print(self.width, self.height)
    self.name = "GLKView"
    frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    flex_width, flex_height = (1 << 1), (1 << 4)
    self.glview = GLKView_OBJC.alloc().initWithFrame_(frame).autorelease()
    self.glview.setDrawableDepthFormat_(2)
    self.glview.setAutoresizingMask_(flex_width|flex_height)


if __name__ == '__main__':
  pass

