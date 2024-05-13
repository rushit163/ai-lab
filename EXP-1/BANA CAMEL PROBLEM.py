def camel_banana_problem(total_bananas, distance, capacity):
    bananas_remaining = total_bananas
    for _ in range(distance):
        bananas_remaining -= capacity
        if bananas_remaining <= 0:
            return "The camel cannot complete the journey."
        bananas_remaining += 1  # Eat a banana
    return f"The camel completed the journey with {bananas_remaining} bananas remaining."

# Example usage:
total_bananas = int(input("Enter total number of bananas: "))
distance = int(input("Enter total distance: "))
capacity = int(input("Enter camel's capacity: "))

result = camel_banana_problem(total_bananas, distance, capacity)
print(result)