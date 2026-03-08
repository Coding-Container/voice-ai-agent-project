from scheduler.appointment_engine import book_slot, get_slots

def book_appointment():
    return book_slot("Dr.Rao", "10AM")

def check_slots():
    slots = get_slots()
    return f"Available slots are: {', '.join(slots)}"