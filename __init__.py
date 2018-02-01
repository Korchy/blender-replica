# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-replica


bl_info = {
    'name': 'Replica',
    'category': 'Mesh',
    'author': 'Nikita Akimov',
    'version': (0, 0, 1),
    'blender': (2, 79, 0),
    'location': '3DView window - T-panel - Replica subpanel',
    'wiki_url': '',
    'tracker_url': '',
    'description': 'Mesh replication'
}

from . import replica
from . import replica_panel

def register():
    replica.register()
    replica_panel.register()


def unregister():
    replica.unregister()
    replica_panel.unregister()


if __name__ == '__main__':
    register()
