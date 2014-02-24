from rgkit import rg
from base import BaseRobot


class Robot(BaseRobot):

    '''Defender Robot.
    Identify and move towards the strongest ally robot, attacking
    any adjacent enemy robot along the way.  When within a number
    of blocks from the strongest ally, guard.
    '''

    def act(self, game):
        allies = self.allies(game)
        enemies = self.enemies(game)
        strongest = self.strongest(allies)

        # Attack any adjacent enemies
        for loc, enemy in enemies.iteritems():
            if rg.dist(loc, self.location) <= 1:
                return ['attack', loc]

        # Guard when nearby allies
        if rg.dist(self.location, strongest.location) <= 3:
            return ['guard']

        return ['move', rg.toward(self.location, strongest.location)]
