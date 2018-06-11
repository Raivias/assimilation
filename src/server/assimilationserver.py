import argparse
import sys

import map
import agent
import location


class AssimilationServer:
    """
    Class that produces a server instance of Assimilation
    """
    def __init__(self, port):
        """
        Initialize a new instance of Assimilation
        :param port: Port to open communications on.
        """
        self.port = port
        agents = []
        for i in range(1,5):
            agents.append(agent.TestAgent(location=location.Location2D(i,i), shape=agent.TestAgentShape(), limits=agent.TestLimits()))
        self.map = map.Map(agents)
        return

    def start(self):
        for ob in self.map.objects:
            print(ob)
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starts a server version of Assimulation.")
    # parser.add_argument("-p", "--port", help="Port number to open the game on", type=int)

    args = parser.parse_args()

    server = AssimilationServer(2)
    ecode = server.start()
    sys.exit(ecode)
