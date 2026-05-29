import random
target_units = int(input("Enter target production units: "))
workers_per_shift = int(input("Enter number of workers per shift: "))
defect_rate = float(input("Enter defect rate percentage: "))

total_produced = 0
total_defects = 0

print("\n -Production Counter System Started -\n")
for shift in range(1, 4):
    print(f"\nShift {shift} Started")

    shift_produced = 0
    shift_defects = 0

    for cycle in range(1, 21):
        if total_produced >= target_units:
            print("\nTarget reached! Production stopped.")
            break
        defect_chance = random.randint(1, 100)
        
        if defect_chance <= defect_rate:
            print(f"Cycle {cycle}: Defective item detected - Skipped")
            shift_defects += 1
            total_defects += 1
            continue

        shift_produced += 1
        total_produced += 1

        print(f"Cycle {cycle}: Item Produced Successfully")
    productivity = shift_produced * workers_per_shift

    print("\nShift Summary")
    print("Items Produced :", shift_produced)
    print("Defective Items:", shift_defects)
    print("Worker Productivity:", productivity) 

    if total_produced >= target_units:
        break

print("\n----- Final Production Report -----")
print("Total Items Produced :", total_produced)
print("Total Defective Items:", total_defects)
print("Target Units :", target_units)

if total_produced >= target_units:
    print("Production Target Achieved")
else:
    print("Production Target Not Achieved")