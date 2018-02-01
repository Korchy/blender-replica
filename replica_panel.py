# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-replica

import bpy


class Replica_panel(bpy.types.Panel):
    bl_idname = 'replica.panel'
    bl_label = 'replica'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Replica'

    def draw(self, context):
        self.layout.operator("replica.replica", text="Replica")


def register():
    bpy.utils.register_class(Replica_panel)


def unregister():
    bpy.utils.unregister_class(Replica_panel)
