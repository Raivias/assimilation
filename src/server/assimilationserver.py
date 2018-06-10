import argparse
import sys


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
        self.map = Map()
        return

    def start(self):
        """
        Kick it off
        :return: error code if anything goes wrong
        """
        print("Port:\t%d" % self.port)
        running = True
        # TODO open join connection
        while running:
            continue
            # TODO open port and wait for people to join
            # TODO
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starts a server version of Assimulation.")
    parser.add_argument("-p", "--port", help="Port number to open the game on", type=int)

    args = parser.parse_args()

    server = AssimilationServer(args.port)
    ecode = server.start()
    sys.exit(ecode)
