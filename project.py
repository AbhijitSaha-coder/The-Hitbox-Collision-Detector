enemy = [20, 20, 40, 40] 

print(f"Enemy is at {enemy[0]},{enemy[1]} with size {enemy[2]}x{enemy[3]}")
bullet_x = int(input("Fire at X: "))
bullet_y = int(input("Fire at Y: "))

if (enemy[0] + enemy[2] >= bullet_x > enemy[0]) and (enemy[1] + enemy[3] >= bullet_y > enemy[1]):
    print("HIT")
else:
    print("MISS")