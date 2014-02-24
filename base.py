from rgkit import rg


class BaseRobot(object):

    def act(self, game):
        return ['guard']

    def allies(self, game):
        '''Allies.
        Return a dictionary of all ally robots on the field.
        '''
        allies = {}
        for loc, robot in game.robots.items():
            if 'robot_id' in robot:
                allies[loc] = robot
        return allies

    def enemies(self, game):
        '''Enemies.
        Return a dictionary of all enemy robots on the field.
        '''
        enemies = {}
        for loc, robot in game.robots.items():
            if 'robot_id' not in robot:
                enemies[loc] = robot
        return enemies

    def weakest(self, robots):
        '''Weakest.
        Given a dictionary of robots, return a reference to
        the weakest robot.
        '''
        weakest = None

        for loc, robot in robots.iteritems():
            if weakest is None:
                weakest = robot
                continue
            if weakest.hp > robot.hp:
                weakest = robot

        return weakest

    def weakest_ally(self, game):
        allies = self.allies(game)
        return self.weakest(allies)

    def weakest_enemy(self, game):
        enemies = self.enemies(game)
        return self.weakest(enemies)

    def strongest(self, robots):
        '''Strongest.
        Given a dictionary of robots, return a reference to
        the strongest robot.
        '''
        strongest = None

        for loc, robot in robots.iteritems():
            if strongest is None:
                strongest = robot
                continue
            if strongest.hp < robot.hp:
                strongest = robot

        return strongest

    def nearest(self, robots):
        nearest = None
        nearest_distance = None

        for loc, robot in robots.iteritems():
            if nearest is None:
                nearest = robot
                nearest_distance = rg.wdist(self.location, robot.location)
                continue
            distance = rg.wdist(self.location, robot.location)
            if distance < nearest_distance:
                nearest = robot
                nearest_distance = distance

        return nearest

    def nearest_enemy(self, game):
        enemies = self.enemies(game)
        return self.nearest(enemies)

    def nearest_ally(self, game):
        allies = self.allies(game)
        return self.nearest(allies)
