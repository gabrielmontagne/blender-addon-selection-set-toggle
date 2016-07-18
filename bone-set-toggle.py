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
            row.label(text="set: " + selection_set.name)

    @classmethod
    def poll(cls, context):
        return len(context.object.selection_sets)

def register():
    bpy.utils.register_class(SelectionSetTogglePanel)

def unregister():
    bpy.utils.unregister_class(SelectionSetTogglePanel)

if __name__ == "__main__":
    print('main')
    register()
