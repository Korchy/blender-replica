# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
# https://github.com/Korchy/blender-replica

import bpy


class Replica(bpy.types.Operator):
    bl_idname = 'replica.replica'
    bl_label = 'Replica'
    bl_description = 'Replica'

    status = None

    def modal(self, context, event):
        if self.status:
            return {'PASS_THROUGH'}
        else:
            return {'FINISHED'}

    def execute(self, context):
        if self.status:
            return {'FINISHED'}
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        return None


def register():
    bpy.utils.register_class(Replica)


def unregister():
    bpy.utils.unregister_class(Replica)
