from ctre import WPI_TalonSRX
class Shooter:
    motor: WPI_TalonSRX

    def __init__(self):
        self.ref_velocity = 0

    def enable(self):
        self.ref_velocity = 1

    def disable(self):
        self.ref_velocity = 0

    def ready(self):
        return self.motor.getQuadratureVelocity() > 4500

    def execute(self):
        self.motor.set(WPI_TalonSRX.ControlMode.PercentOutput, self.ref_velocity)

