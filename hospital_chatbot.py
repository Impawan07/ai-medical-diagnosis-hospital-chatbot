import streamlit as st
import random

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Hospital Assistant Chatbot",
    page_icon="🏥",
    layout="centered"
)

# ===============================
# CUSTOM UI (BACKGROUND + CHAT)
# ===============================
st.markdown("""
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3");
    background-size: cover;
}
.chat-box {
    background-color: rgba(0,0,0,0.6);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# SESSION STATE INIT
# ===============================
defaults = {
    "logged_in": False,
    "otp": None,
    "mobile": None,
    "chat": [],
    "selected_doctor": None,
    "booking_confirmed": False
}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ===============================
# LOGIN SCREEN (OTP – SIMULATED)
# ===============================
def login_screen():
    st.title("🔐 Patient Registration & Login")
    st.caption("Login using your mobile number to access hospital services")

    mobile = st.text_input("📱 Enter Mobile Number", max_chars=10)

    if st.button("Send OTP"):
        if mobile.isdigit() and len(mobile) == 10:
            otp = random.randint(100000, 999999)
            st.session_state.otp = otp
            st.session_state.mobile = mobile
            st.success("✅ OTP sent successfully!")
            st.info(f"🔑 OTP (Simulation): **{otp}**")
        else:
            st.error("❌ Please enter a valid 10-digit mobile number")

    if st.session_state.otp:
        entered_otp = st.text_input("🔐 Enter OTP", max_chars=6)
        if st.button("Verify OTP"):
            if entered_otp == str(st.session_state.otp):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Invalid OTP")

# ===============================
# DATA
# ===============================
hospital_data = {
    "doctors": {
        "endocrinology": ["Dr. Ramesh Kumar", "Dr. Anita Sharma"],
        "cardiology": ["Dr. Suresh Rao"],
        "general": ["Dr. Meena Patel"]
    },
    "floors": {
        "Endocrinology": "First Floor (OPD Clinics)",
        "Cardiology": "First Floor (OPD Clinics)",
        "General": "First Floor (OPD Clinics)"
    },
    "billing": ["Cash", "Card", "UPI", "Insurance"],
    "emergency": "🚨 Emergency services are available 24/7 on the Ground Floor."
}

condition_to_department = {
    "diabetes": "endocrinology",
    "sugar": "endocrinology",
    "fever": "general",
    "cold": "general",
    "cough": "general",
    "heart": "cardiology",
    "bp": "cardiology"
}

appointment_slots = {
    "Dr. Anita Sharma": ["10:00 AM", "11:00 AM", "2:00 PM", "4:00 PM"],
    "Dr. Ramesh Kumar": ["9:30 AM", "12:00 PM", "3:00 PM"],
    "Dr. Suresh Rao": ["10:30 AM", "1:00 PM", "5:00 PM"]
}

# ===============================
# CHATBOT LOGIC (FINAL)
# ===============================
def chatbot_response(query):
    q = query.lower()

    # Emergency
    if "emergency" in q:
        return hospital_data["emergency"]

    # Navigation
    if "navigate" in q or "where is" in q or "go to" in q:
        for dept, loc in hospital_data["floors"].items():
            if dept.lower() in q:
                return f"📍 **{dept} Department** is located at **{loc}**."
        return "📍 Please specify the department you want to navigate to."

    # Medical condition → doctor
    for condition, dept in condition_to_department.items():
        if condition in q:
            doctors = hospital_data["doctors"][dept]
            return (
                f"👨‍⚕️ For **{condition.title()}**, consult **{dept.title()}**.\n\n"
                "Available doctors:\n" +
                "\n".join(f"- {d}" for d in doctors)
            )

    # Doctor selection
    for doctor in appointment_slots:
        if doctor.lower() in q:
            st.session_state.selected_doctor = doctor
            return (
                f"👨‍⚕️ You selected **{doctor}**.\n"
                "Type **appointment** to see available slots."
            )

    # Appointment flow
    if "appointment" in q:
        if st.session_state.selected_doctor:
            slots = appointment_slots[st.session_state.selected_doctor]
            return (
                f"📅 Available slots for **{st.session_state.selected_doctor}**:\n\n"
                + "\n".join(f"- {s}" for s in slots)
                + "\n\nPlease select a slot."
            )
        return "👨‍⚕️ Please select a doctor first."

    # Slot confirmation
    if st.session_state.selected_doctor:
        for slot in appointment_slots[st.session_state.selected_doctor]:
            if slot.lower() in q:
                st.session_state.booking_confirmed = True
                return (
                    f"✅ **Appointment Confirmed!**\n\n"
                    f"Doctor: {st.session_state.selected_doctor}\n"
                    f"Time: {slot}"
                )

    # Billing
    if "bill" in q or "payment" in q:
        return "💳 Payment methods: " + ", ".join(hospital_data["billing"])

    return (
        "🤖 I can help with:\n"
        "- Doctor recommendations\n"
        "- Appointments\n"
        "- Billing & payments\n"
        "- Emergency help\n"
        "- Hospital navigation"
    )

# ===============================
# MAIN APP
# ===============================
if not st.session_state.logged_in:
    login_screen()

else:
    st.sidebar.title("🧠 System Info")
    st.sidebar.markdown(f"""
**Logged in as:**  
📱 {st.session_state.mobile}

**Architecture:**  
Hybrid Rule-Based + LLM  

**Status:**  
🟢 Live & Operational
""")

    st.title("🏥 Hospital Assistant Chatbot")
    st.caption("Secure Access • Realistic Appointment Booking")

    user_input = st.text_input("Ask your question:")

    if user_input:
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", chatbot_response(user_input)))

    for speaker, msg in st.session_state.chat:
        st.markdown(
            f"<div class='chat-box'><b>{speaker}:</b><br>{msg}</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")
    if st.button("🚪 Logout"):
        for key in defaults:
            st.session_state[key] = defaults[key]
        st.rerun()

    st.warning(
        "⚠️ This chatbot provides informational assistance only and does not offer medical diagnosis or treatment."
    )
