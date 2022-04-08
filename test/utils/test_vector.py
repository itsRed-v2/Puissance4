from p4.utils.vector import Vector

def test_constructor():
	vec = Vector(2, 4)
	assert vec.c == 2
	assert vec.r == 4

def test_add():
	vec = Vector(2, 4)
	vec2 = Vector(2, 1)

	vec.add(vec2)
	assert vec.c == 4
	assert vec.r == 5

def test_subtract():
	vec = Vector(2, 4)
	vec2 = Vector(2, 1)

	vec.subtract(vec2)
	assert vec.c == 0
	assert vec.r == 3

def test_multiply():
	vec = Vector(2, 4)

	vec.multiply(3)
	assert vec.c == 6
	assert vec.r == 12

	vec.multiply(-1)
	assert vec.c == -6
	assert vec.r == -12

def test_equal():
	vec1 = Vector(2, 2)
	vec2 = Vector(2, 2)
	vec3 = Vector(2, 3)

	assert vec1 == vec2
	assert vec2 != vec3