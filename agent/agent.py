from agent.tools import book_appointment, check_slots
from memory.session_memory import set_state, get_state
from agent.language import detect_language
from utils.latency_logger import measure_latency

@measure_latency
def process(text: str):

    text_lower = text.lower()
    lang = detect_language(text)

    # greeting
    greetings = ["hello","hi","hey","namaste","vanakkam"]
    if any(word in text_lower for word in greetings):
        return f"Hello! Language detected: {lang}. I can help you book a doctor appointment."

    # appointment booking
    booking_words = ["book","appointment","doctor","consult","visit"]
    if any(word in text_lower for word in booking_words):
        return book_appointment()

    # slot check
    slot_words = ["slot","time","available","schedule"]
    if any(word in text_lower for word in slot_words):
        return check_slots()

    # name memory
    if "my name is" in text_lower:
        name = text_lower.replace("my name is","").strip()
        set_state("name", name)
        return f"Nice to meet you {name}"

    if "who am i" in text_lower:
        name = get_state("name")
        if name:
            return f"You are {name}"
        else:
            return "I don't know your name yet"

    # health queries
    health_words = ["fever","cold","pain","sick","medicine"]
    if any(word in text_lower for word in health_words):
        return "You may need a consultation. I can help book a doctor appointment."

    # fallback
    return "I can help you book appointments, check doctor slots, or schedule a visit."