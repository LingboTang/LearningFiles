import math

def normalize_vector(vec):
	norm = math.sqrt(float(vec[0]) ** 2 + float(vec[1]) ** 2 + float(vec[2]) ** 2)
	vec = (float(vec[0])/norm, float(vec[1])/norm, float(vec[2])/norm)
	return vec

vec1 = (-20, 10, -24)
vec2 = (17, -12, 26)

norm_vec1 = normalize_vector(vec1)
norm_vec2 = normalize_vector(vec2)


print(float(vec1[0]) ** 2 + float(vec1[1]) ** 2 + float(vec1[2]) ** 2)
print(float(vec2[0]) ** 2 + float(vec2[1]) ** 2 + float(vec2[2]) ** 2)
print(norm_vec1)
print(norm_vec2)