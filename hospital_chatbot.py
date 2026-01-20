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
# LOGIN SCREEN
# ===============================
def login_screen():
    st.title("🔐 Patient Login")
    st.caption("Login using your mobile number to access the Hospital Assistant")

    mobile = st.text_input("📱 Enter Mobile Number", max_chars=10)

    if st.button("Send OTP"):
        if len(mobile) == 10 and mobile.isdigit():
            otp = random.randint(100000, 999999)
            st.session_state.otp = otp
            st.session_state.mobile = mobile
            st.success("✅ OTP sent successfully!")
            st.info(f"🔑 OTP (Simulation): **{otp}**")  # simulation
        else:
            st.error("❌ Please enter a valid 10-digit mobile number")

    if st.session_state.otp:
        entered_otp = st.text_input("🔐 Enter OTP", max_chars=6)

        if st.button("Verify OTP"):
            if entered_otp == str(st.session_state.otp):
                st.session_state.logged_in = True
                st.success("🎉 Login successful!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid OTP")

# ===============================
# CHATBOT DATA
# ===============================
hospital_data = {
    "doctors": {
        "endocrinology": ["Dr. Ramesh Kumar", "Dr. Anita Sharma"],
        "cardiology": ["Dr. Suresh Rao"],
        "general": ["Dr. Meena Patel"]
    },
    "opd_timings": "9 AM – 5 PM (Mon–Sat)",
    "billing": ["Cash", "Card", "UPI", "Insurance"],
    "emergency": "🚨 Emergency services are available 24/7 on the Ground Floor."
}

condition_to_department = {
    "diabetes": "endocrinology",
    "sugar": "endocrinology",
    "fever": "general",
    "cold": "general",
    "heart": "cardiology",
    "bp": "cardiology"
}

# ===============================
# CHATBOT LOGIC
# ===============================
def chatbot_response(query):
    q = query.lower()

    if "emergency" in q:
        return hospital_data["emergency"]

    for condition, dept in condition_to_department.items():
        if condition in q:
            docs = hospital_data["doctors"][dept]
            return f"👨‍⚕️ For **{condition}**, consult **{dept.title()}**:\n" + "\n".join(docs)

    if "appointment" in q:
        return f"🗓️ OPD Timings: {hospital_data['opd_timings']}"

    if "bill" in q or "payment" in q:
        return "💳 Payment modes: " + ", ".join(hospital_data["billing"])

    return "🤖 I can help with doctors, appointments, billing, and emergencies."

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
""")

    st.title("🏥 Hospital Assistant Chatbot")
    st.caption("Secure Access Enabled via OTP Login")

    user_input = st.text_input("Ask your question:")

    if user_input:
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", chatbot_response(user_input)))

    for speaker, msg in st.session_state.chat:
        if speaker == "You":
            st.markdown(f"🧑 **You:** {msg}")
        else:
            st.success(f"🤖 {msg}")

    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.chat = []
        st.session_state.otp = None
        st.experimental_rerun()
