if "bpy" in locals():
    if bpy.app.version < (2, 71, 0):
        import imp as importlib
    else:
        import importlib
    importlib.reload(pie_mesh)
    importlib.reload(pie_object)
else:
    import bpy
    from . import (
        pie_mesh,
        pie_object
        )

sub_modules_names=(
    "pie_mesh",
    "pie_object",
)

sub_modules=[__import__(__package__ + "." + submod, {}, {}, submod) for submod in sub_modules_names]

def register_submodule(mod):
    mod.register()

def unregister_submodule(mod):
    mod.unregister()


def register():
    for mod in sub_modules:
        register_submodule(mod)

def unregister():
    for mod in sub_modules:
        unregister_submodule(mod)

if __name__ == "__main__":
    register()