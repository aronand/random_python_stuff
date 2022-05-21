from blender.utils import get_vertex_loop_indices
from blender.utils import get_vertex_normals
from blender.utils import normal_to_rgb
from utils import combine_dictionaries

import bpy


obj = bpy.context.object
mesh = obj.data
vert_normals = get_vertex_normals(obj)
vert_li = get_vertex_loop_indices(obj)
vertex_data = combine_dictionaries(vert_normals, vert_li)

# TODO: Finish the script
# TODO: Try if setting the loop index color works this time without crashing Blender
