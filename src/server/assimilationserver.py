import argparse
import sys

import externalplayers
import join
import map
from mapobjects import location, testagent


class AssimilationServer:
    """
    Class that produces a server instance of Assimilation
    """
    def __init__(self, host, port):
        """
        Initialize a new instance of Assimilation
        :param port: Port to open communications on.
        """
        self.host = host
        self.port = port

        self.players = externalplayers.players.Players()
        self.connector = join.Join(host, port, self.players)
        self.connector.open()

        agents = []
        for i in range(1, 5):
            agents.append(testagent.TestAgent(
                location=location.Location2D(i, i),
                shape=testagent.TestAgentShape(),
                limits=testagent.TestLimits()))
        self.map = map.Map(agents)
        return

    def start(self):
        for ob in self.map.objects:
            print(ob)
        return 0

    def round(self):
        # get all players
        all_players = self.players.get_players(type(externalplayers.players.Player))
        # add new players to map
        # get next map state
        # check for end game
        # save new map
        # send to observers
        all_observers = self.players.get_players(type(externalplayers.observer.Observer))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starts a server version of Assimulation.")
    # parser.add_argument("-p", "--port", help="Port number to open the game on", type=int)

    args = parser.parse_args()

    server = AssimilationServer("localhost", 2)
    ecode = server.start()
    sys.exit(ecode)
