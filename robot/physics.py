import math

from pyfrc.physics.motor_cfgs import MOTOR_CFG_CIM
class PhysicsEngine:
    def __init__(self, controller):
        self.controller = controller
        self.accel = 0
        self.velocity = 0

        G = 1
        Kt = 2.42 / 133
        R = 12 / 133
        Kv = (5310 / 60 * 2 * math.pi )/ (12 - 2.3 * R)
        J = .5 * .51 * .03775

        self.A = -(Kt)/(Kv*R*J)
        self.B =(Kt)/(R*J)

        print(self.A, self.B)

    def initialize(self, hal_data):
        pass

    def update_sim(self, hal_data, now, dt):
        voltage = 12 * hal_data['CAN'][10]['value']
        self.velocity = math.pow(math.e, self.A * dt) * self.velocity + \
                         1/self.A * (math.pow(math.e, self.A*dt) - 1) * self.B * voltage


        hal_data['CAN'][10]['quad_position'] = int(self.velocity / (2 * math.pi) * 60)
        hal_data['CAN'][10]['quad_velocity'] = int(self.velocity / (2 * math.pi) * 60)
