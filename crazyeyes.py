import rg

class Robot:
    def act(self, game):

        # if there are >1 enemies around, suicide
        nhostiles = 0
        enemylocs = []
        enemyadjs = []
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                enemylocs.append(loc)
                if rg.dist(loc, self.location) <= 1:
                    nhostiles = nhostiles + 1
                    enemyadjs.append(loc);
                    #return ['attack', loc]
        if nhostiles > 1:
            return ['suicide']
        elif nhostiles == 1:
            return ['attack',enemyadjs.pop()]
        else:
            # move toward the center
            return ['move', rg.toward(self.location, enemylocs.pop())]