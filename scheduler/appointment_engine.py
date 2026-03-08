import json
import os

FILE = "database/appointments.json"

def get_slots():
    return ["10AM", "11AM", "2PM"]

def book_slot(doctor, slot):

    booked_slots = []

    if os.path.exists(FILE):

        with open(FILE) as f:
            for line in f:
                data = json.loads(line)
                if data["doctor"] == doctor:
                    booked_slots.append(data["slot"])

    # conflict check
    if slot in booked_slots:

        available = [s for s in get_slots() if s not in booked_slots]

        if available:
            return f"Slot {slot} already booked. Try {available[0]} instead."
        else:
            return "No slots available today."

    appointment = {
        "doctor": doctor,
        "slot": slot
    }

    with open(FILE,"a") as f:
        f.write(json.dumps(appointment)+"\n")

    return f"Appointment booked with {doctor} at {slot}"