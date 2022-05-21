import bpy
from mathutils import Vector
from collections import defaultdict


def get_vertex_normals(obj: bpy.types.Object) -> defaultdict[int, Vector]:
    """
    Calculates vertex normals from connected faces and returns them as a dict.
    
     * Raises TypeError if the passed object is not MESH type.
    """
    if obj.type != "MESH":
        raise TypeError
    
    vertex_data: defaultdict[int, Vector] = defaultdict(Vector)
    
    for face in obj.data.polygons:
        for vert in face.vertices:
            vertex_data[vert] += face.normal
    
    for vector in vertex_data.values():
        vector.normalize()
    
    return vertex_data
