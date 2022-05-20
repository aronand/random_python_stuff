from mathutils import Vector


def __normal_to_uint8(axis: float) -> int:
    """
    Converts a float value of -1.0...1.0 into int 0...255.

     * Raises TypeError if argument is not of type float
     * Raises ValueError if value is not normalized
    """
    if type(axis) is not float:
        raise TypeError
    
    if axis < -1.0 or axis > 1.0:
        raise ValueError
    
    return round(((axis + 1) / 2) * 255)


def normal_to_rgb(normal: Vector) -> tuple[int, int, int]:
    """Maps normal vector into RGB values and returns them as a tuple."""
    rgb: list = [__normal_to_uint8(axis) for axis in normal]
    return tuple(rgb)
