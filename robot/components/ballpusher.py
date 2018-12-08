import wpilib


class BallPusher:
    piston: wpilib.Solenoid

    def __init__(self):
        self.extended = False

    def push(self):
        self.extended = True

    def retract(self):
        self.extended = False

    def execute(self):
        self.piston.set(self.extended)
