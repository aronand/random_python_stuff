import bpy
from mathutils import Vector


def get_vertex_normals(obj: bpy.types.Object) -> dict[int, Vector]:
    """
    Calculates vertex normals from connected faces and returns them as a dict.
    
     * Raises TypeError if the passed object is not MESH type.
    """
    if obj.type != "MESH":
        raise TypeError
    
    vertex_data: dict[int, Vector] = {}
    
    for face in obj.data.polygons:
        for vert in face.vertices:
            if vert not in vertex_data:
                vertex_data[vert] = Vector((0.0, 0.0, 0.0))
            vertex_data[vert] += face.normal
    
    for vector in vertex_data.values():
        vector.normalize()
    
    return vertex_data
