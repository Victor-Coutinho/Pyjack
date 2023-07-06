from tupy import *

class Star(Image):
  def update(self):
    self.x = mouse.x
    self.y = mouse.y

    if mouse.is_button_just_down():
      self.angle += 30

s = Star()

run(globals())