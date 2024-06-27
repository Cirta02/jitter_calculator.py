# jitter_calculator.py

import sys

# Fonction pour extraire les événements à partir du fichier de trace
def extract_events(trace_file):
    events = []
    with open(trace_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 4:
                time_stamp = float(parts[1])
                event_type = parts[0]
                events.append({"time": time_stamp, "event_type": event_type})
    return events

# Fonction pour calculer le jitter
def calculate_jitter(events):
    if len(events) < 2:
        return 0.0

    total_jitter = 0.0
    count = 0

    for i in range(1, len(events)):
        if events[i]["event_type"] == "r" and events[i-1]["event_type"] == "r":
            jitter = abs(events[i]["time"] - events[i-1]["time"])
            total_jitter += jitter
            count += 1

    if count > 0:
        average_jitter = total_jitter / count
    else:
        average_jitter = 0.0

    return average_jitter

# Fonction principale pour exécuter le calcul du jitter
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 jitter_calculator.py <trace_file>")
        return
    
    trace_file = sys.argv[1]
    
    try:
        events = extract_events(trace_file)
        print(f"Extracted {len(events)} events from trace file.")

        jitter = calculate_jitter(events)
        print(f"Average Jitter: {jitter:.4f} seconds")
    
    except FileNotFoundError:
        print(f"Error: Trace file '{trace_file}' not found.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

