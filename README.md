Hitbox Collision Detector (AABB Logic)

This project simulates a basic hitbox detection system commonly used in 2D shooter games. The objective is to determine whether a bullet fired by the player hits an enemy by checking if the bullet’s coordinates lie within the enemy’s rectangular hitbox. The logic used is Axis-Aligned Bounding Box (AABB) collision detection, one of the simplest and most widely used techniques in game development.

This project is created by Abhijit Saha and is my first PSP (Problem Solving and Programming) project.

⸻

📌 How It Works
	•	The Enemy is represented as a list:
  [x, y, width, height]
  Example: [20, 20, 40, 40]
This means the enemy spans:
	•	X-axis: from 20 → 60
	•	Y-axis: from 20 → 60

	•	The Bullet is a point represented as:
  [x, y]
  	•	The program asks the user for the bullet’s X and Y coordinates.
	•	To determine a collision, it checks:
	•	enemy_left   < bullet_x <= enemy_right
	•	enemy_top    < bullet_y <= enemy_bottom

Where:
	•	enemy_right = x + width
	•	enemy_bottom = y + height

If both X and Y fall inside the hitbox → HIT
Otherwise → MISS

⸻

📌 Stub Code
# [x, y, width, height]
enemy = [20, 20, 40, 40]

print(f"Enemy is at {enemy[0]},{enemy[1]} with size {enemy[2]}x{enemy[3]}")

bullet_x = int(input("Fire at X: "))
bullet_y = int(input("Fire at Y: "))

⸻

📌 Test Cases
Input (X)
Result
Explanation
15
MISS
Outside left boundary
25
HIT (check Y)
Within horizontal range
60
HIT
On right boundary (considered hit)

⸻

🎯 Learning Outcomes
	•	Understanding how AABB collision detection works
	•	Working with coordinate geometry and boundaries
	•	Using conditional logic for decision-making
	•	Introduction to game development concepts
