from magicbot import StateMachine, state, timed_state, default_state

from components.ballpusher import BallPusher
from components.shooter import Shooter


class Shoot(StateMachine):
    shooter: Shooter
    ball_pusher: BallPusher

    def fire(self):
        self.engage()

    @default_state
    def default(self):
        self.shooter.disable()

    @state(first=True)
    def begin_firing(self, initial_call):
        """This function will only be called IFF fire is called and
           the FSM isn't currently in the 'firing' state. If fire
           was not called, this function will not execute."""
        if initial_call:
            self.shooter.enable()
        if self.shooter.ready():
            self.next_state('firing')

    @timed_state(duration=2.0, must_finish=True)
    def firing(self):
        """Because must_finish=True, once the FSM has reached this
           state, this state will continue executing even if engage
           isn't called"""
        self.ball_pusher.push()

    def __call__(self, *args, **kwargs):
        self.fire()
