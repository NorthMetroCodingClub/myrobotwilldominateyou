from rgkit import rg
from base import BaseRobot


class Robot(BaseRobot):

    '''Bully Robot.
    Identify and move towards the weakest enemy robot,
    attacking any adjacent enemy robot along the way.
    '''

    def act(self, game):
        enemies = self.enemies(game)
        weakest = self.weakest(enemies)

        for loc, enemy in enemies.iteritems():
            if rg.dist(loc, self.location) <= 1:
                return ['attack', loc]
        return ['move', rg.toward(self.location, weakest.location)]
