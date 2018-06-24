import externalplayers


class Observer(externalplayers.Player):
    def __init__(self, host, port):
        super(externalplayers.Player).__init__(host=host, port=port, p_type=type(self))
