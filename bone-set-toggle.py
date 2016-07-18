import bpy

class SelectionSetTogglePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_selection-set-toggle"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")

def register():
    bpy.utils.register_class(SelectionSetTogglePanel)

def unregister():
    bpy.utils.unregister_class(SelectionSetTogglePanel)

if __name__ == "__main__":
    print('main')
    register()
