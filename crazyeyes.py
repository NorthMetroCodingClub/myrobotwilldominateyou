import rg

class Robot:
    def strongest_enemy(self, game):
        tmp_strongest = None
        for loc,bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if tmp_strongest is None:
                    tmp_strongest = bot
                elif bot.hp > tmp_strongest.hp:
                    tmp_strongest = bot
        return tmp_strongest

    def weakest_enemy(self, game):
        tmp_weakest = None
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if tmp_weakest is None:
                    tmp_weakest = bot
                elif bot.hp < tmp_weakest.hp:
                    tmp_weakest = bot
        return tmp_weakest

    def act(self, game):

        # if there are >1 enemies around, suicide
        nhostiles = 0
        enemylocs = []
        enemyadjs = []
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                enemylocs.append(loc)
                if rg.wdist(loc, self.location) <= 1:
                    nhostiles = nhostiles + 1
                    enemyadjs.append(loc);
        if nhostiles > 1:
            return ['suicide']
        elif nhostiles == 1:
            return ['attack',enemyadjs.pop()]
        else:
            # move toward the center
            return ['move', rg.toward(self.location, self.strongest_enemy(game).location)]