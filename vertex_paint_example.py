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

if not mesh.vertex_colors:
    mesh.vertex_colors.new()

v_col = mesh.vertex_colors['Col']  # We presume the default name

for vert, data in vertex_data.items():
    normal = data[0]
    loop_indices = data[1]
    if not loop_indices:
        continue
    # Convert color to 0.0...1.0 range and fourth argument (doesn't seem to be alpha, no idea what it is)
    color = [float(col)/255 for col in normal_to_rgb(normal)]
    color.append(1.0)
    for li in loop_indices:
        v_col.data[li].color = color
