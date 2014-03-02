from rgkit import rg
from base import BaseRobot


class Robot(BaseRobot):

    '''Bully Robot.
    Identify and move towards the weakest enemy robot,
    attacking the weakest adjacent enemy robot along the way.
    '''

    def act(self, game):
        enemies = self.enemies(game)
        global_weakest = self.weakest(enemies)

        local_weakest = self.weakest(
            self.adjacent_enemies(enemies))

        if local_weakest:
            return ['attack', local_weakest.location]
        return ['move', rg.toward(self.location, global_weakest.location)]

    def adjacent_enemies(self, enemies):
        return {loc: enemy
                for loc, enemy
                in enemies.iteritems()
                if rg.dist(loc, self.location) <= 1}
