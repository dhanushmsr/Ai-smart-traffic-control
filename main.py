from emergency_detect import detect_emergency
from signal_control import smart_signal

print("🚦 Real-Time AI Traffic System Started")

emergency, vehicles = detect_emergency()

level, signal, time = smart_signal(vehicles, emergency)

print("\n--- SIGNAL STATUS ---")
print(f"Traffic Level   : {level}")
print(f"Vehicle Count   : {vehicles}")
print(f"Signal State    : {signal}")
print(f"Green Time (s)  : {time}")

if emergency:
    print("🚨 Emergency vehicle detected — Priority given!")
