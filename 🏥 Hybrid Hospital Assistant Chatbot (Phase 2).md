# **🏥 Hybrid Hospital Assistant Chatbot (Phase 2\)**

## **📌 Project Overview**

This project implements a **Hybrid Generative AI–Based Hospital Assistant Chatbot** designed to provide real-time assistance to patients and visitors in a hospital environment.

The chatbot combines:

* **Rule-Based Logic** for deterministic and safety-critical operations  
* **Conversational AI (LLM concepts)** for natural language interaction

The application is deployed as a **live web application using Streamlit Cloud** and supports real-time interaction through a browser.

---

## **🎯 Objectives**

* Provide instant hospital-related assistance  
* Reduce dependency on manual reception/helpdesk  
* Demonstrate a real-world **hybrid AI architecture**  
* Build and deploy a **real-time AI application**

---

## **🧠 System Architecture**

The chatbot follows a **Hybrid Architecture**:

### **1️⃣ Rule-Based Engine**

Handles structured and safety-critical tasks:

* Appointment information  
* Doctor lookup  
* Medical condition → department mapping  
* Billing and payment guidance  
* Emergency assistance  
* Hospital floor navigation

### **2️⃣ Conversational Layer (LLM-based concept)**

Handles:

* Natural language queries  
* Hospital FAQs  
* Process explanations  
* Human-like conversational responses

### **3️⃣ Hybrid Router**

* Routes user queries to the rule-based engine first  
* Falls back to the conversational layer if no deterministic rule applies

---

## **✨ Features**

* 💬 Real-time chat interface  
* 🧠 Medical condition inference (e.g., Diabetes → Endocrinology)  
* 📅 Appointment assistance  
* 👨‍⚕️ Doctor recommendation  
* 💳 Billing & payment guidance  
* 🚨 Emergency support  
* 🏥 Hospital floor navigation  
* ⚡ Quick action buttons  
* 📜 Chat history using session state  
* ☁️ Live cloud deployment

---

## **🛠️ Technology Stack**

* **Programming Language:** Python  
* **Frontend & UI:** Streamlit  
* **Backend Logic:** Python Functions  
* **Architecture:** Hybrid Rule-Based \+ Conversational AI  
* **Deployment:** Streamlit Cloud  
* **Version Control:** GitHub

---

##  **Live Demo**

🔗 **Live Streamlit Application:**  
 *[https://ai-medical-diagnosis-hospital-chatbot-nvnimpic2xmxamwur2f3ft.streamlit.app/](https://ai-medical-diagnosis-hospital-chatbot-nvnimpic2xmxamwur2f3ft.streamlit.app/)* 

The application is fully deployed and accessible via a public URL.

---

## **📂 Repository Structure**

hospital-chatbot-phase2/  
│  
├── hospital\_chatbot.py      \# Main Streamlit application  
├── requirements.txt         \# Project dependencies  
└── README.md                \# Project documentation

---

## **▶️ How to Run (Local – Optional)**

⚠️ Local execution is optional. The recommended way is using the **Streamlit Cloud deployment**.

pip install streamlit  
streamlit run hospital\_chatbot.py

---

##  **Ethical & Safety Considerations**

* No real patient data is used  
* No medical diagnosis or prescriptions are provided  
* Clear disclaimers included in the UI  
* Emergency guidance prioritizes human intervention

---

## **⚠️ Limitations**

* Conversational layer uses predefined responses (no live LLM API)  
* No database or EMR integration  
* English language support only

---

## **🔮 Future Enhancements**

* Integration with real LLM APIs (OpenAI / Gemini)  
* Voice-based interaction  
* Multilingual support  
* Hospital database & EMR integration  
* Appointment booking backend  
* Analytics dashboard for hospital staff

## **📌 Conclusion**

This project demonstrates a practical and industry-aligned implementation of a **Hybrid AI system** for healthcare assistance. By combining deterministic rule-based logic with conversational AI principles and deploying the system in real time, the project showcases both **technical depth and real-world applicability**.