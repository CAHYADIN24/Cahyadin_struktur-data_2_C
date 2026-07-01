# teknik duplikasi pada list

x = ["prabowo", "Jokowi", "Gibran"]
print(f"X : {x}")

y = x
print(f"Y : {y}")

x[0] = "Tedy"
print(f"X dirubah: {x}")
print(f"Y berubah? : {y}")

z = x.copy()

print(f"alamat x {hex(id(x))}")
print(f"alamat y {hex(id(y))}")
print(f"alamat z {hex(id(z))}")

x[1] = "habibie"

print(f"X dirubah: {x}")
print(f"Z berubah? : {z}")
print(f"Y berubah? : {y}")