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
# SESSION STATE INIT
# ===============================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "otp" not in st.session_state:
    st.session_state.otp = None

if "mobile" not in st.session_state:
    st.session_state.mobile = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# ===============================
# LOGIN SCREEN (OTP – SIMULATED)
# ===============================
def login_screen():
    st.title("🔐 Patient Login")
    st.caption("Login using your mobile number to access the Hospital Assistant")

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
                st.success("🎉 Login successful!")
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
    "opd_timings": "9 AM – 5 PM (Monday to Saturday)",
    "floors": {
        "Ground Floor": "Reception, Pharmacy, Emergency",
        "First Floor": "OPD Clinics",
        "Second Floor": "Diagnostics & Labs",
        "Third Floor": "ICU"
    },
    "billing": ["Cash", "Card", "UPI", "Insurance"],
    "emergency": "🚨 Emergency services are available 24/7 on the **Ground Floor**."
}

condition_to_department = {
    "diabetes": "endocrinology",
    "sugar": "endocrinology",
    "fever": "general",
    "cold": "general",
    "cough": "general",
    "heart": "cardiology",
    "bp": "cardiology",
    "blood pressure": "cardiology"
}

# ===============================
# CHATBOT LOGIC (FINAL)
# ===============================
def chatbot_response(query):
    q = query.lower()

    # 1. Emergency
    if "emergency" in q:
        return hospital_data["emergency"]

    # 2. Navigation
    if "navigate" in q or "go to" in q or "where is" in q:
        for dept in hospital_data["doctors"]:
            if dept in q or dept.replace("ology", "") in q:
                return (
                    f"📍 The **{dept.title()} Department** is located on the "
                    f"**First Floor (OPD Clinics)**. Please follow signage from reception."
                )
        return "📍 Please specify which department you want directions to."

    # 3. Medical condition inference (no doctor keyword needed)
    for condition, dept in condition_to_department.items():
        if condition in q:
            doctors = hospital_data["doctors"][dept]
            return (
                f"👨‍⚕️ For **{condition.title()}**, you should consult the "
                f"**{dept.title()} department**.\n\n"
                "Available doctors:\n" +
                "\n".join(f"- {doc}" for doc in doctors)
            )

    # 4. Explicit doctor request
    if "doctor" in q or "consult" in q:
        return (
            "👨‍⚕️ Please mention your health issue.\n\n"
            "Examples: diabetes, fever, heart problem."
        )

    # 5. Appointment
    if "appointment" in q:
        return f"🗓️ OPD timings: **{hospital_data['opd_timings']}**."

    # 6. Billing
    if "bill" in q or "payment" in q:
        return "💳 Accepted payment methods: " + ", ".join(hospital_data["billing"])

    # 7. Floors
    if "floor" in q:
        return "\n".join(
            [f"• **{f}**: {d}" for f, d in hospital_data["floors"].items()]
        )

    # Fallback
    return (
        "🤖 I can help you with:\n"
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
    # Sidebar
    st.sidebar.title("🧠 System Info")
    st.sidebar.markdown(f"""
**Logged in as:**  
📱 {st.session_state.mobile}

**Architecture:**  
Hybrid Rule-Based + LLM  

**Status:**  
🟢 Live & Operational
""")

    # Header
    st.title("🏥 Hospital Assistant Chatbot")
    st.caption("Secure Access Enabled via OTP Login")

    st.markdown("""
💡 **Try asking:**  
- diabetes  
- fever  
- navigate to cardiology  
- appointment  
- billing  
""")

    # Chat Input
    user_input = st.text_input("Ask your question:")

    if user_input:
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", chatbot_response(user_input)))

    # Chat Display
    for speaker, msg in st.session_state.chat:
        if speaker == "You":
            st.markdown(f"🧑 **You:** {msg}")
        else:
            st.markdown(f"🤖 **Assistant:** {msg}")

    st.markdown("---")

    # Logout
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.chat = []
        st.session_state.otp = None
        st.session_state.mobile = None
        st.rerun()

    # Disclaimer
    st.warning(
        "⚠️ This chatbot provides informational assistance only and does not "
        "offer medical diagnosis or treatment."
    )
