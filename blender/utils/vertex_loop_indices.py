import bpy
from collections import defaultdict


def get_vertex_loop_indices(obj: bpy.types.Object) -> dict[int, list[int]]:
    """
    Maps face loop indices to vertices and returns them as a dict.
    
     * Raises TypeError if the passed object is not MESH type.
    """
    if obj.type != "MESH":
        raise TypeError
    
    vertex_data: dict[int, list[int]] = defaultdict(list)

    for face in obj.data.polygons:
        for vert, loop_index in zip(face.vertices, face.loop_indices):
            vertex_data[vert].append(loop_index)
    
    return vertex_data
