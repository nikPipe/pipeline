from widget.node_editor import node_graphic_edge
from widget.node_editor.node_serializable import Serializable
from collections import OrderedDict

try:
    from importlib import reload
except:
    pass

for each in [node_graphic_edge]:
    reload(node_graphic_edge)


EDGE_TYPE_DIRECT = 1
EDGE_TYPE_BEZIER = 2

class Edge(Serializable):
    def __init__(self, scene, start_socket=None, end_socket=None, edge_type=EDGE_TYPE_DIRECT):
        super().__init__()
        self.scene = scene
        self.start_socket = start_socket
        self.end_socket = end_socket
        self.edge_type = edge_type



        #self.grEdge = node_graphic_edge.QDMGraphicsEdgeDirect(self) if edge_type == EDGE_TYPE_DIRECT else node_graphic_edge.QDMGraphicsEdgeBezier(self)

        #self.scene.grScene.addItem(self.grEdge)
        self.scene.addEdge(self)

    def __str__(self):
        '''

        :return:
        '''
        return '<Edge %s...%s>' % (hex(id(self))[2:5], hex(id(self))[-3:])
    
    @property
    def start_socket(self): return self._start_socket
    @start_socket.setter
    def start_socket(self, value):
        self._start_socket = value
        if self._start_socket is not None:
            self.start_socket.edge = self

    @property
    def end_socket(self):
        return self._end_socket

    @end_socket.setter
    def end_socket(self, value):
        self._end_socket = value
        if self._end_socket is not None:
            self.end_socket.edge = self

    @property
    def edge_type(self):
        return self._edge_type

    @edge_type.setter
    def edge_type(self, value):
        if hasattr(self, 'grEdge') and self.grEdge is not None:
            self.scene.grScene.removeItem(self.grEdge)

        self._edge_type = value
        if self._edge_type == EDGE_TYPE_DIRECT:
            self.grEdge = node_graphic_edge.QDMGraphicsEdgeDirect(self)

        elif self._edge_type == node_graphic_edge.QDMGraphicsEdgeBezier:
            self.grEdge = node_graphic_edge.QDMGraphicsEdgeBezier(self)

        else:
            self.grEdge = node_graphic_edge.QDMGraphicsEdgeBezier(self)

        self.scene.grScene.addItem(self.grEdge)
        if self.start_socket is not None:
            self.update_position()




    def update_position(self):
        '''

        :return:
        '''
        source_pos = self.start_socket.getSocketPosition()
        source_pos[0] += self.start_socket.node.grNode.pos().x()
        source_pos[1] += self.start_socket.node.grNode.pos().y()
        self.grEdge.setSource(*source_pos)
        if self.end_socket is not None:
            end_pos = self.end_socket.getSocketPosition()
            end_pos[0] += self.end_socket.node.grNode.pos().x()
            end_pos[1] += self.end_socket.node.grNode.pos().y()
            self.grEdge.setDesination(*end_pos)
        else:
            self.grEdge.setDesination(*source_pos)

        self.grEdge.update()

    def remove_from_socket(self):
        '''

        :return:
        '''
        if self.start_socket is not None:
            self.start_socket.edge = None
        if self.end_socket is not None:
            self.end_socket.edge = None

        self.start_socket = None
        self.end_socket = None

    def remove(self):
        '''

        :return:
        '''
        self.remove_from_socket()
        self.scene.grScene.removeItem(self.grEdge)
        self.grEdge = None
        try:
            self.scene.removeEdge(self)
        except ValueError:
            pass

    def serialize(self):
        '''

        :return:
        '''
        return OrderedDict([
            ('id', self.id),
            ('edge_type', self.edge_type),
            ('start', self.start_socket.id),
            ('end', self.end_socket.id),
        ])

    def deseralize(self, data, hashmap={}, restore_id=True):
        '''

        :return:
        '''
        if restore_id: self.id = data['id']
        self.start_socket = hashmap[data['start']]
        self.end_socket = hashmap[data['end']]
        self.edge_type = data['edge_type']

        return True


