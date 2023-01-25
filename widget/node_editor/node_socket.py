from widget.node_editor import node_graphic_socket
from widget.node_editor.node_serializable import Serializable
from collections import OrderedDict
LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket(Serializable):
    def __init__(self, node, index=0, position=LEFT_TOP, socket_type=1):
        super().__init__()
        self.node = node
        self.index = index
        self.position = position
        self.socket_type = socket_type

        self.grSocket = node_graphic_socket.QDMGraphicsSocket(self, self.socket_type)

        self.grSocket.setPos(*self.node.getSocketPosition(index=self.index, position=self.position))

        self.edge = None

    def getSocketPosition(self):
        '''

        :return:
        '''


        return self.node.getSocketPosition(self.index, self.position)

    def setConnectedEdge(self, edge=None):
        '''

        :param edge:
        :return:
        '''
        self.edge = edge

    def hasEdge(self):
        '''

        :return:
        '''
        return self.edge is not None

    def __str__(self):
        '''

        :return:
        '''
        return '<Socket %s...%s>' % (hex(id(self))[2:5], hex(id(self))[-3:])

    def serialize(self):
        '''

        :return:
        '''
        return OrderedDict([
            ('id', self.id),
            ('index', self.index),
            ('position', self.position),
            ('type', self.socket_type),

        ])
    def deseralize(self, data, hashmap={}, restore_id=True):
        '''

        :return:
        '''
        if restore_id: self.id = data['id']
        hashmap[data['id']] = self
        return True
