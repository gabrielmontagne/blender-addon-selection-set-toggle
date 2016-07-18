import bpy
import addon_utils

bl_info = {
    'name': 'Toggle Selection Sets from the Properties Panel',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 77, 0),
    'description': 'Adds buttons for switching to Selection Sets in Pose Mode',
    'tracker_url': 'https://bitbucket.org/gabriel.montagne/blender-addon-selection-set-toggle/issues?status=new&status=open',
    'category': 'Animation'
}

class SelectionSetTogglePanel(bpy.types.Panel):
    """Creates a Panel in the View 3D UI for toggling selection sets."""

    bl_idname = 'OBJECT_PT_selection-set-toggle'
    bl_label = 'Selection Set Toggle '
    bl_options = {'DEFAULT_CLOSED'}
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    def draw(self, context):
        layout = self.layout
        for index, selection_set in enumerate(context.object.selection_sets):
            row = layout.row()
            layout.operator(
                'pose.toggle_selection_by_number',
                text=selection_set.name
            ).index = index

    @classmethod
    def poll(cls, context):
        loaded, state = addon_utils.check('bone_selection_sets')
        if not loaded:
            return False

        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

class SwitchToSelectionSet(bpy.types.Operator):
    bl_idname = 'pose.toggle_selection_by_number'
    bl_label = 'Toggle Selection Set'
    bl_description = 'Toggle selection set by number'
    bl_options = {'UNDO', 'REGISTER'}

    index = bpy.props.IntProperty(
        name='Active Selection Index for Toggle',
        description='Index of the currently active selection set',
        default=0
    )

    def execute(self, context):
        arm = context.object
        bpy.ops.pose.select_all(action='DESELECT')
        arm.active_selection_set = self.index
        bpy.ops.pose.selection_set_select()
        return { 'FINISHED' }

def register():
    bpy.utils.register_class(SelectionSetTogglePanel)
    bpy.utils.register_class(SwitchToSelectionSet)

def unregister():
    bpy.utils.unregister_class(SelectionSetTogglePanel)

if __name__ == '__main__':
    register()
