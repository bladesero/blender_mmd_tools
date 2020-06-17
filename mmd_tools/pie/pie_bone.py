import bpy
from bpy.types import Menu
from mmd_tools import register_wrap

@register_wrap
class VIEW3D_MMD_PIE(Menu):
    bl_label = "MMD PIE MENU"

    def draw(self,context):
        layout = self.layout

        pie = layout.menu_pie()

        # pie.operator_enum("mesh.select_mode", "type")
        pie.operator("mmd_tools.set_glsl_shading",text="GLSL")
        pie.operator("mmd_tools.set_shadeless_glsl_shading",text="Shadeless")
        pie.operator("mmd_tools.reset_shading",text="Reset")

classes=(
    VIEW3D_MMD_PIE,
)

addon_keymaps=[]

def register():
    wm=bpy.context.window_manager
    km=wm.keyconfigs.addon.keymaps.new(name='Mesh')
    kmi=km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS')
    kmi.properties.name = "VIEW3D_MMD_PIE"
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