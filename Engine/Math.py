from Engine.Location import Location

def lerp(start_value, end_value, t):

    if t > 1:
        t = 1
    if t < 0:
        t = 0

    x  = lerpL( start_value.X(), end_value.X(),t)
    y  = lerpL( start_value.Y(), end_value.Y(),t)
    location = Location(start_value.rect)
    location.set(x,y)
    return location


def lerpL(a,b,t):
      return (1.0 - t) * a + t * b;