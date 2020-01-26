# The Plane in 3d

## Plane representation

The plane can be defined as a point and two directions like following:

$plane = \left(\array{p_x \\ p_y \\ p_z}\right) + a \cdot \left(\array{v1_x \\ v1_y \\ v1_z}\right) + b \cdot \left(\array{v2_x \\ v2_y \\ v2_z}\right)$

Following factor rules apply:

 - For $a = 0$ and $b = 0$ we have just the point $p$.
 - For $a = 1$ and $b = 0$ we the $p1 + \vec{v1}$.
 - For $a = 0$ and $b = 1$ we the $p1 + \vec{v2}$.
 - For $a = 1$ and $b = 1$ we the $p1 + \vec{v1} + \vec{v2}$.
 - For $a = 0.5$ and $b = 0.5$ we have the center point. 

## Intersection point of a line with a plane
Calculation works in follwing steps:

 - We define a line L to be equal to plane P as following:<br>
   $p1 + a \cdot \vec{v1} = p2 + b \cdot \vec{v2} + c \cdot \vec{v3}$<br>
   When there is a solution we should have values for the three factors.
   So we should get rid of two factors to be able to calculate one.
   We start with it subtracting the point $p1$ on both sides.
 - $a \cdot \vec{v1} = (p2 - p1) + b \cdot \vec{v2} + c \cdot \vec{v3}$<br>
   Now we do a cross product with $v3$ on both sides; that does eliminate last term because
   a $\vec{v3} \times \vec{v3}$ is the null vector.
 - $a \cdot \vec{v1} \times \vec{v3} = (p2 - p1) \times \vec{v3} + b \cdot \vec{v2} \times \vec{v3}$<br>
   Again we use the same *trick* to elimate last term by applying a cross product
   of $\vec{v2} \times \vec{v3}$ on both sides.
 - $a \cdot (\vec{v1} \times \vec{v3}) \times (\vec{v2} \times \vec{v3}) = ((p2 - p1) \times \vec{v3}) \times (\vec{v2} \times \vec{v3})$<br>
   Before we can run the final logic we should have two vectors:
     - $\vec{v4} = (\vec{v1} \times \vec{v3}) \times (\vec{v2} \times \vec{v3})$
     - $\vec{v5} = ((p2 - p1) \times \vec{v3}) \times (\vec{v2} \times \vec{v3})$
 - As a result you have three ways how to calculate the factor $a$:
      - Solution 1: $a = v5_x / v4_x$ (when $v4_x$ is not 0)
      - Solution 2: $a = v5_y / v4_y$ (when $v4_y$ is not 0)
      - Solution 3: $a = v5_z / v4_z$ (when $v4_z$ is not 0)
      - If no solution does match then there is no intersection point otherwise you now can
        use first line $p1 + a \cdot \vec{v1}$ to calculate the intersection point.

You are able to see whether the point is between start and end point of line (for $0.0 <= a <= 1.0$) 
but you would have to calculate $b$ and $c$ to know same for plane.
