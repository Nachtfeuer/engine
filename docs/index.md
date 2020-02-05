# Welcome

It's an overview of the classes and its relationships:

```plantuml
@startuml
Line ..> Point
Line ..> Vector
Triangle ..> Point
Plane ..> Point
Plane ..> Vector

class Vector {
    + float x
    + float y
    + float z
    --
    + float length()
    + float angle(Vector vector)
    + float dot_product(Vector vector)
    + Vector cross_product(Vector vector)
    + Vector normalized()
    + Vector scaled(float factor)
    + Vector projection(Vector vector)
    .. operators ..
    + Vector add(Vector vector)
    + Vector sub(Vector vector)
    + Vector neg(Vector vector)
    + Vector mul(float factor)
    .. tool functions ..
    + float[3] toList()
    + float(3) toTuple()
    ..
    {static} + Vector from_sequence(List|Tuple sequence)
}

class Point {
    + float x
    + float y
    + float z
    --
    + Vector sub(Point point)
}

class Line {
    + Point position
    + Vector direction
    --
    + float length()
    + float angle(Line line)
    + float distance(Point point)
    + Point point(float factor)
    + boolean has_point(Point point)
    + Point intersection(Line line)
    ..
    {static} + Line from_point(Point point_a, Point point_b)
}

class Plane {
    + Point position
    + Vector direction_a
    + Vector direction_b

    + Point intersection(Line line)
    + Point point(float factor_a, float factor_b)
    + boolean has_point(Point point, boolean exact_match=True)
}

class Triangle {
    + Point[3] points
    + Point intersection(Line line)
    + bool has_point(Point point)
}
@enduml
```
