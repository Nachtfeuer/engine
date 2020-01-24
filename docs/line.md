# The line in 3d

## Line representation

The line can be defined as a point and a direction like following:

$l = \left(\array{p_x \\ p_y \\ p_z}\right) + k \cdot \left(\array{v_x \\ v_y \\ v_z}\right)$

For $k = 0$ it is the start point of the line and for $k = 1$ it is the end point of the line.

## Angle between lines

The calculation of the angle is related to the direction vectors of
both lines which you find in vector documention.

## Intersection point of two lines
First to say it's more likely in 3d space that two lines do not intersect while
in 2d the only case where to lines do not intersect is when they are parallel.
However the calculation is not too hard considering following approach:

 - First we have two lines as shown in line representation but with two different factors
   which should provide us the same point when there is an intersection so we can say:
   $p1 + a \cdot \vec{v1} = p2 + b \cdot \vec{v2}$<br>
   First we do is we subtract p1 on both sides.
 - $a \cdot \vec{v1} = p2 - p1 + b \cdot \vec{v2}$<br>
   Now we apply cross product $\vec{v2}$ on both sides.
 - $a \cdot \vec{v1} \times \vec{v2} = (p2 - p1) \times \vec{v2}$<br>
   The $b \cdot \vec{v2}$ did go away because the cross product with same vector
   is the null vector.
 - From programming perspective you now have to consider that two lines
   can refer - as special cases - to a plane where one dimension might go away.
   As a result you have three ways how to calculate the factor $a$:
      - First: we define $\vec{v3} = \vec{v1} \times \vec{v2}$ and $\vec{v4} = (p2 - p1) \times \vec{v2}$
      - Solution 1: $a = v4_x / v3_x$ (when $v3_x$ is not 0)
      - Solution 2: $a = v4_y / v3_y$ (when $v3_y$ is not 0)
      - Solution 3: $a = v4_z / v3_z$ (when $v3_z$ is not 0)
      - If no solution does match then there is no intersection point otherwise you now can
        use first line $p1 + a \cdot \vec{v1}$ to calculate the intersection point.

For the basic idea thank you very much to the great guys here:
    [http://mathforum.org/library/drmath/view/62814.html](http://mathforum.org/library/drmath/view/62814.html)
