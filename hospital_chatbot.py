import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Hospital Assistant Chatbot",
    page_icon="🏥",
    layout="centered"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🧠 System Info")
st.sidebar.markdown(
    """
**Architecture:**  
Hybrid Rule-Based + LLM  

**Capabilities:**  
• Appointments  
• Doctor Lookup  
• Billing & Payments  
• Emergency Guidance  
• Hospital Navigation  

**Status:**  
🟢 Live & Operational
"""
)

# -------------------------------
# Hospital Static Data
# -------------------------------
hospital_data = {
    "doctors": {
        "endocrinology": ["Dr. Ramesh Kumar", "Dr. Anita Sharma"],
        "cardiology": ["Dr. Suresh Rao"],
        "general": ["Dr. Meena Patel"]
    },
    "opd_timings": "9 AM to 5 PM (Monday to Saturday)",
    "floors": {
        "Ground Floor": "Reception, Pharmacy, Emergency",
        "First Floor": "OPD Clinics",
        "Second Floor": "Diagnostics & Labs",
        "Third Floor": "ICU"
    },
    "billing": {
        "payment_modes": ["Cash", "Card", "UPI", "Insurance"],
        "helpdesk": "Billing counter near reception"
    },
    "emergency": "🚨 Emergency department is open 24/7 on the Ground Floor."
}

# -------------------------------
# Rule-Based Engine
# -------------------------------
def rule_based_response(user_query):
    q = user_query.lower()

    if "emergency" in q:
        return hospital_data["emergency"]

    if "appointment" in q:
        return (
            "🗓️ Sure! You can book appointments during OPD hours: "
            f"**{hospital_data['opd_timings']}**. "
            "Let me know if you'd like help finding a doctor."
        )

    if "doctor" in q:
        for dept, doctors in hospital_data["doctors"].items():
            if dept in q:
                return (
                    f"👨‍⚕️ Doctors available in **{dept.title()}**:\n\n"
                    + "\n".join(f"- {doc}" for doc in doctors)
                )
        return (
            "👨‍⚕️ Please specify the department "
            "(e.g., endocrinology, cardiology, general medicine)."
        )

    if "bill" in q or "payment" in q:
        modes = ", ".join(hospital_data["billing"]["payment_modes"])
        return (
            f"💳 Payment methods accepted: **{modes}**.\n\n"
            f"For assistance, please visit the **{hospital_data['billing']['helpdesk']}**."
        )

    if "floor" in q or "location" in q:
        response = "🏥 **Hospital Floor Directory:**\n\n"
        for floor, details in hospital_data["floors"].items():
            response += f"• **{floor}**: {details}\n"
        return response

    return None

# -------------------------------
# LLM Conversational Layer (Mock)
# -------------------------------
def llm_response(user_query):
    return (
        "🤖 I’m here to help! You can ask me about appointments, "
        "doctors, billing, hospital navigation, or general hospital services. "
        "Please tell me how I can assist you."
    )

# -------------------------------
# Hybrid Router
# -------------------------------
def hybrid_chatbot(user_query):
    rule_response = rule_based_response(user_query)
    if rule_response:
        return rule_response
    return llm_response(user_query)

# -------------------------------
# UI Header
# -------------------------------
st.title("🏥 Hospital Assistant Chatbot")
st.caption("Hybrid Rule-Based + LLM Conversational System")

# -------------------------------
# Architecture Explanation
# -------------------------------
with st.expander("📐 System Architecture & Purpose"):
    st.markdown(
        """
**Rule-Based Engine**  
• Appointments  
• Doctor Lookup  
• Billing Information  
• Emergency Guidance  
• Floor Navigation  

**LLM Conversational Engine**  
• Natural language understanding  
• Process explanations  
• FAQ handling  
• Polite patient guidance  

This hybrid approach ensures **accuracy, safety, and flexibility**.
"""
    )

# -------------------------------
# Quick Action Buttons
# -------------------------------
st.markdown("### ⚡ Quick Actions")
col1, col2, col3, col4 = st.columns(4)

if col1.button("📅 Appointment"):
    st.session_state.chat.append(("Bot", hybrid_chatbot("appointment")))

if col2.button("👨‍⚕️ Find Doctor"):
    st.session_state.chat.append(("Bot", hybrid_chatbot("doctor")))

if col3.button("🚨 Emergency"):
    st.session_state.chat.append(("Bot", hybrid_chatbot("emergency")))

if col4.button("💳 Billing"):
    st.session_state.chat.append(("Bot", hybrid_chatbot("billing")))

# -------------------------------
# Chat History
# -------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

st.markdown("### 💬 Chat")

user_input = st.text_input("Ask your question:")

if user_input:
    response = hybrid_chatbot(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

for speaker, msg in st.session_state.chat:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.success(f"🤖 {msg}")

# -------------------------------
# Disclaimer
# -------------------------------
st.markdown("---")
st.warning(
    "⚠️ **Disclaimer:** This chatbot provides informational assistance only "
    "and does not offer medical diagnosis or treatment."
)
