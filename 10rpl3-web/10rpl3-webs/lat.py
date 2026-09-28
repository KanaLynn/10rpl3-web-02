s = int(input("masukan nilai sisi : "))

v_cth1 = s * s * s
v_cth2 = s**3

print("hasil rumus pertama : ", v_cth1)
print("hasil rumus kedua : ", v_cth2)

p = int(input("masukan nilai panjang : "))
l = int(input("masukan nilai lebar : "))
t = int(input("masukan nilai tinggi : "))

v = p * l * t
L = 2 * (p * l + p * t + l * t)
print("hasil volume : ", v)
print("hasil luas permukaan : ", L)
