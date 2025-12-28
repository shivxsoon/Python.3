Amount = 2750  # <-- Chosen amount

print(f"Amount to withdraw: {Amount}")

limit = 70000

if Amount > limit:
    print("You cannot withdraw more than 70000.")
else:
    note_1 = Amount // 100
    note_2 = (Amount % 100) // 50
    note_3 = ((Amount % 100) % 50) // 10
    remaining = Amount % 10

    print(f"1. Notes of 100 rupee: {note_1} × 100 = {note_1 * 100}")
    print(f"2. Notes of 50 rupee: {note_2} × 50 = {note_2 * 50}")
    print(f"3. Notes of 10 rupee: {note_3} × 10 = {note_3 * 10}")

    total_dispensed = note_1 * 100 + note_2 * 50 + note_3 * 10
    print(f"Total dispensed: {total_dispensed}")

    print(f"Remaining amount that cannot be dispensed: {remaining}")
