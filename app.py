import streamlit as st

st.set_page_config(
    page_title="AI Stack for Healthcare",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Stack for Healthcare")
st.write("AI-powered Healthcare Information Assistant")

st.divider()

st.header("🤖 Healthcare AI Assistant")

question = st.text_input(
    "Enter your health concern:",
    placeholder="Example: I have fever"
)

if st.button("Get AI Suggestion"):

    if not question.strip():
        st.warning("Please enter your health concern.")

    else:
        text = question.lower()

        # FEVER
        if "fever" in text or "temperature" in text:

            st.subheader("🌡️ Fever - General Guidance")

            st.write("Here are some general precautions:")

            st.markdown("""
            ### ✅ What you can do

            - 💧 Drink plenty of water and fluids.
            - 🛌 Get enough rest and sleep.
            - 👕 Wear comfortable clothing.
            - 🌬️ Stay in a comfortable room.
            - 🍲 Eat light and nutritious food if you can.
            - 🌡️ Monitor your temperature.

            ### ⚠️ When to contact a doctor

            Seek medical advice if:

            - Fever is persistent or getting worse.
            - You have difficulty breathing.
            - You feel unusually weak or confused.
            - You have a severe headache or stiff neck.
            - You have repeated vomiting.
            - You show signs of dehydration.
            - You are worried about your symptoms.

            ### 🚨 Important

            This application provides general healthcare information.
            It does not diagnose diseases or replace a doctor.
            """)

        # COUGH / COLD
        elif "cough" in text or "cold" in text:

            st.subheader("🤧 Cold / Cough - General Guidance")

            st.markdown("""
            ### ✅ General precautions

            - 💧 Drink enough fluids.
            - 🛌 Get adequate rest.
            - 🍵 Warm fluids may feel soothing.
            - 🚭 Avoid smoke and other irritants.
            - 🌡️ Monitor your symptoms.

            If symptoms are severe, persistent, or getting worse,
            consult a healthcare professional.
            """)

        # HEADACHE
        elif "headache" in text or "head pain" in text:

            st.subheader("🤕 Headache - General Guidance")

            st.markdown("""
            ### ✅ General precautions

            - 🛌 Rest in a quiet environment.
            - 💧 Drink enough water.
            - 🍲 Eat regular meals.
            - 📱 Reduce excessive screen time.
            - 😴 Get adequate sleep.

            If the headache is sudden, severe, or accompanied by
            concerning symptoms, seek medical attention promptly.
            """)

        # STOMACH PAIN
        elif "stomach pain" in text or "stomach ache" in text:

            st.subheader("🤢 Stomach Pain - General Guidance")

            st.markdown("""
            ### ✅ General precautions

            - 💧 Stay hydrated.
            - 🍲 Eat light meals if comfortable.
            - 🛌 Get adequate rest.
            - Avoid foods that make your symptoms worse.

            If pain is severe, persistent, or getting worse,
            consult a healthcare professional.
            """)

        # GENERAL HEALTH QUESTION
        else:

            st.subheader("🩺 General Health Guidance")

            st.write(
                "I can provide basic healthcare information "
                "based on common symptoms."
            )

            st.markdown("""
            ### General precautions

            - 💧 Stay hydrated.
            - 🛌 Get enough rest.
            - 🍎 Eat balanced meals.
            - 🧘 Manage stress.
            - 📝 Monitor your symptoms.

            For persistent or concerning symptoms,
            consult a qualified healthcare professional.
            """)

st.divider()

st.caption(
    "⚕️ For educational purposes only. "
    "This application does not replace professional medical advice."
)