import speech_recognition as sr
import pyttsx3
import time
from langdetect import detect


engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()



doctors = {
    "dr ravi": ["10am", "11am", "12pm"],
    "dr priya": ["2pm", "3pm", "4pm"]
}

appointments = {}

def show_doctors():
    return "Available doctors are Dr Ravi and Dr Priya."


def show_slots(doctor):
    doctor = doctor.lower()

    if doctor not in doctors:
        return "Doctor not found."

    slots = doctors[doctor]

    available = []
    for slot in slots:
        key = doctor + "_" + slot
        if key not in appointments:
            available.append(slot)

    if not available:
        return "No slots available."

    return f"Available slots for {doctor} are {', '.join(available)}"



def book_appointment(doctor, slot):
    doctor = doctor.lower()
    slot = slot.lower()

    if doctor not in doctors:
        return "Doctor not available."

    if slot not in doctors[doctor]:
        return "Invalid slot."

    key = doctor + "_" + slot

    if key in appointments:
        return "This slot is already booked."

    appointments[key] = True

    return f"Appointment booked with {doctor} at {slot}."



def cancel_appointment(doctor, slot):
    doctor = doctor.lower()
    slot = slot.lower()

    key = doctor + "_" + slot

    if key in appointments:
        del appointments[key]
        return f"Appointment with {doctor} at {slot} cancelled."

    return "No appointment found to cancel."


def process_user_input(text):

    text = text.lower()

    if "doctor" in text:
        return show_doctors()

    if "slot" in text or "availability" in text:
        return show_slots("dr ravi")

    if "book" in text:
        return book_appointment("dr ravi", "10am")

    if "cancel" in text:
        return cancel_appointment("dr ravi", "10am")

    if "fever" in text or "cold" in text:
        return "You should consult a doctor. I can help you book an appointment."

    return "I can help with doctor availability, slot availability, booking or cancelling appointments."


recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")
        audio = recognizer.listen(source)

        try:

            text = recognizer.recognize_google(audio)
            print("User:", text)

            language = detect(text)
            print("Detected Language:", language)

            return text

        except:
            return None



def run_voice_agent():

    speak("Hello. I am your healthcare voice assistant.")

    while True:

        user_text = listen()

        if user_text is None:
            speak("Sorry I did not understand.")
            continue

        start = time.time()

        response = process_user_input(user_text)

        end = time.time()

        latency = end - start
        print("Latency:", latency)

        speak(response)



if __name__ == "__main__":

    run_voice_agent()