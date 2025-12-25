def signal_logic(avg_vehicles, emergency_count):

    if emergency_count > 0:
        return "EMERGENCY", 90

    if avg_vehicles < 10:
        return "LOW", 20
    elif avg_vehicles < 30:
        return "MEDIUM", 40
    else:
        return "HIGH", 60
