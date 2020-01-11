# The vector in 3d

## Vector representation

The vector coordinates are representated by three
floats: x, y and z:

$\vec{v} = \left(\array{v_x \\ v_y \\ v_z}\right)$

## Length of a vector

The length of a vector is calculated with:

$\left|\vec{v}\right| = \sqrt{v_x^2 + v_y^2 + v_z^2}$


## Summation

It's a summation per coordinate:<br/>

$\vec{a} + \vec{b} = \left(\array{a_x + b_x \\ a_y + b_y \\ a_z + b_y}\right)$

The implementation is done by overwriting the **\_\_add\_\_** operator which
allows you to write in code $a + b$ same way as in the formular.

## Subtraction

It's a subtraction per coordinate:<br/>

$\vec{a} - \vec{b} = \left(\array{a_x - b_x \\ a_y - b_y \\ a_z - b_y}\right)$

The implementation is done by overwriting the **\_\_sub\_\_** operator which
allows you to write in code $a - b$ same way as in the formular.

## Dot product

The dot product (also called **scalar product**) is calculated this way:

 $\vec{a} \cdot \vec{b} = a_x \cdot b_x + a_y \cdot b_y + a_z \cdot b_z$

The *\_\_mul\_\_* operater has **not** been overwritten for it because there
is also a further multiplication: cross product. The method for the dot product
is **dot_product**.

There following special properties:

 - When $\vec{a} \cdot \vec{b} = 0$ then the angle between those two vectors is $90^\circ$
 - When the value is negative (> $90^\circ$) the direction of the one is opposite to the other.
   That is useful if you consider rendering of an object; the camera does see the object frontside
   but one or more triangles of the backside are not visible. That can be detected by calculating
   the dot product of the camera vector and the triangle plane vector; the backside vector has same
   direction while the frontside vectors should opposite.

## Cross Product

The cross product is calculated this way (result is again a vector):

 $\vec{a} \times \vec{b} = \left(\array{a_y \cdot b_z - a_z \cdot b_y \\ a_z \cdot b_x - a_x \cdot b_z \\ a_x \cdot b_y - a_y \cdot b_x}\right)$

The most simple answer for the meaning: The result vector has $90^\circ$ to both vectors and therefor 
$90^\circ$ to the plan defined by both vectors.

## Multiplication with a factor

$k \cdot \vec{v} = \left(\array{k \cdot b_x \\ k \cdot b_y \\ k \cdot b_y}\right)$

