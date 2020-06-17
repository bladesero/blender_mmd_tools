import bpy
from bpy.types import Menu
import mmd_tools.core.model as mmd_model
from mmd_tools import register_wrap

@register_wrap
class VIEW3D_MMD_SHADING(Menu):
    bl_label = "MMD Pie"

    def draw(self,context):
        layout=self.layout
        pie = layout.menu_pie()
        row=pie.row()
        box = row.box()
        boxrow = box.column(align=True)
        boxrow.label(text="Shading")
        boxrow.operator("mmd_tools.set_glsl_shading",text="GLSL")
        boxrow.operator("mmd_tools.set_shadeless_glsl_shading",text="Shadeless")
        boxrow.operator("mmd_tools.reset_shading",text="Reset")
        
        obj = context.object
        if(obj.type == 'ARMATURE'):
            root = mmd_model.Model.findRoot(context.active_object)
            if root!=None and root.mmd_root.is_built:
                pie.operator("mmd_tools.bake_physics",text="Bake Action")
        if(obj.type == 'MESH'):
            root = mmd_model.Model.findRoot(context.active_object)
            if root!=None:
                pie.operator("mmd_tools.convert_material_universe",text="Convert Material")

classes=(
    VIEW3D_MMD_SHADING,
)

addon_keymaps=[]

def register():
    wm=bpy.context.window_manager
    km=wm.keyconfigs.addon.keymaps.new(name='Object Mode')
    kmi=km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS')
    kmi.properties.name = "VIEW3D_MMD_SHADING"
    addon_keymaps.append((km, kmi))

def unregister():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()