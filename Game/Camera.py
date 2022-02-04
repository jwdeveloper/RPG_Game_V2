from Engine.GameObject import GameObject
from Engine import Math


class Camera(GameObject):
    target = None
    followSmooth = 0.3
    cameraZoom = 4
    maxZoom = 300
    minZoom = 100
    zoomSmooth = 0.1

    def onEnable(self, engine):
        self.group = "camera"
        self.name = "camera"

    def setTarget(self, target):
        self.target = target

    def setZoom(self, cameraZoom):
        self.cameraZoom = cameraZoom

    def onTick(self, engine):
        self.zoom(engine)
        self.follow(engine)

    def zoom(self, engine):
        result = Math.lerpL(engine.zoom_factor, self.cameraZoom, self.zoomSmooth)
        if result < self.minZoom:
            result = self.minZoom
        if result > self.maxZoom:
            result = self.maxZoom

        engine.setZoom(result)

    def follow(self, engine):
        if self.target == None:
            return
        camera = engine.camera
        cameraLoc = self.location.set(camera.x, camera.y)
        targetLoc = self.target.location.clone()
        result = Math.lerp(cameraLoc, targetLoc, self.followSmooth)
        engine.setCamera(result.X(), result.Y())
