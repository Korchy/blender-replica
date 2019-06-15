# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-replica

from .addon import Addon
from . import replica
from . import replica_panel


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


def register():
    if not Addon.dev_mode():
        replica.register()
        replica_panel.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        replica.unregister()
        replica_panel.unregister()


if __name__ == '__main__':
    register()
