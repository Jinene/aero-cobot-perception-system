def avoid_obstacle(distance):
    if distance < 0.5:
        return "STOP"
    elif distance < 1.0:
        return "SLOW"
    else:
        return "MOVE"


if __name__ == "__main__":
    test_distances = [0.3, 0.7, 1.5]

    for d in test_distances:
        action = avoid_obstacle(d)
        print(f"Distance: {d} → Action: {action}")
