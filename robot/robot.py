#!/usr/bin/env python
import wpilib
import magicbot
import ctre

from components.shooter import Shooter
from components.ballpusher import BallPusher
from sequences.shoot import Shoot


class MyRobot(magicbot.MagicRobot):

    shoot: Shoot
    shooter: Shooter
    ball_pusher: BallPusher

    def createObjects(self):
        self.shooter_motor = ctre.WPI_TalonSRX(10)
        self.ball_pusher_piston = wpilib.Solenoid(1)

        self.joystick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        if self.joystick.getTrigger():
            self.shoot()

if __name__ == '__main__':
    wpilib.run(MyRobot)
