#!/usr/bin/env python 
import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.joystick = wpilib.Joystick(1)

        self.dio = wpilib.DigitalInput(1)

        self.solenoid1 = wpilib.Solenoid(1)
        self.solenoid4 = wpilib.Solenoid(4)

    
    def teleopPeriodic(self):
        self.solenoid1.set(self.joystick.getTrigger())

        self.solenoid4.set(self.dio.get())

if __name__ == '__main__':
    wpilib.run(MyRobot)
