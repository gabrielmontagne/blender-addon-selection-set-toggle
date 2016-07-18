import bpy

class SelectionSetTogglePanel(bpy.types.Panel):
    """Creates a Panel in the View 3D UI for toggling selectin sets."""

    bl_idname = "OBJECT_PT_selection-set-toggle"
    bl_label = "Selection Set Toggle "
    bl_options = {'DEFAULT_CLOSED'}
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"

    def draw(self, context):
        layout = self.layout
        for selection_set in context.object.selection_sets:
            row = layout.row()
            layout.operator("pose.toggle_selection_by_number", text=selection_set.name)

    @classmethod
    def poll(cls, context):
        return (context.object and
                context.object.type == 'ARMATURE' and
                context.mode == 'POSE')

class ToggleSelectionSetByNumber(bpy.types.Operator):
    bl_idname = "pose.toggle_selection_by_number"
    bl_label = "Toggle Selection Set"
    bl_description = "Toggle selection set by number"
    bl_options = {'UNDO', 'REGISTER'}

    def execute(self, context):
        arm = context.object
        print('did it')
        return { 'FINISHED' }




def register():
    bpy.utils.register_class(SelectionSetTogglePanel)
    bpy.utils.register_class(ToggleSelectionSetByNumber)

def unregister():
    bpy.utils.unregister_class(SelectionSetTogglePanel)

if __name__ == "__main__":
    print('main')
    register()
