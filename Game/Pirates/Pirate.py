from Game.Npc import Npc


class Pirate(Npc):

    def onEnable(self, engine):
        super().onEnable(engine)
        sprites = engine.loadImages("Postacie\\Alojzy")
        self.image = sprites[0]
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Pirat")
        self.questSounds = engine.loadSounds("Pirat\\quest")

        self.location.set(30, 30)
        #self.setQuest(ExampleQuest())


class Captin(Npc):

    def onEnable(self, engine):
        super().onEnable(engine)
        self.image = engine.loadImage("Postacie\\Kapitan\\kapitan")
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Kapitan")
        self.location.set(30, 30)


class PirateKacper(Npc):

    def onEnable(self, engine):
        super().onEnable(engine)
        self.image = engine.loadImage("Postacie\\Pirat2\\Pirate")
        self.orignalImg = self.image
        self.sounds = engine.loadSounds("Pirat2")
        self.location.set(40, 40)
        #self.setQuest(ExampleQuest())
