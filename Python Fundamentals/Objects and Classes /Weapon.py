class Weapon:
  def __init__ (self, bullets):
    self.bullets = bullets
  
  def shoot(self):
    if self.bullets > 0:
      self.bullets -= 1
      return f'shooting...'
    return f'No bullets left...'

  def __repr__(self):
    return f'Remaining Bullets: {self.bullets}'

weapon = Weapon(5)
print(weapon)