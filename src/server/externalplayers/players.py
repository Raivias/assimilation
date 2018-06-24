from enum import Enum, unique


class Players:
    """
    Players of current game
    """
    def __init__(self):
        self.players = []

    def add(self, player):
        """
        Adds a player to the player list
        :param player: Player to be added to list
        :return:
        """
        if type(player) != type(Player):
            raise TypeError("Bad type %s" % type(Player))
        self.players.append(player)
        return True

    def get_players(self, p_type=None):
        # TODO make deep copies
        if p_type is None:
            return self.players
        if type(p_type) != type(PlayerType):
            raise TypeError("Bad type %s" % type(PlayerType))
        ret = []
        for p in self.players:
            if p.p_type == p_type:
                ret.append(p)
        return ret


class Player:
    """
    Player
    """
    def __init__(self, host, port, p_type):
        self.host = host
        self.port = port
        self.p_type = p_type


@unique
class PlayerType(Enum):
    Observer = 0
    Agent = 1
