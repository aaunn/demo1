import streamlit as st
st.title("EXERCISE")

tab1, tab2, tab3, tab4 = st.tabs (["1. Time left before retire", "2. BMI and Health analysis", "3. Blood pressure and Health anlysis", "4. Emergency patient"])

with tab1:
    st.header("Time left before retire")
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("**Enter your first name:**")
    with col2:
        lname = st.text_input("**Enter your last name:**")
    col3, col4 = st.columns([1,3])
    with col3:
        age = st.number_input("**Enter your age**", min_value=0, step=1)
    with col4:
        career = st.text_input("**Enter your career**")

    if st.button("Show Retirement Result", key="btn_retire"):
        st.subheader("YOUR INFORMATION")
        st.write(f"**Name** {fname} {lname} | **age** {age} years | **Career** is {career}")

        retire = 60 - age
        if retire > 0:
            st.info(f"Your time left before retirement: **{retire} years**")
        elif retire == 0:
            st.success("You are retiring this year! Congratulations!")
        else:
            st.success(f"You have already retired or passed retirement age by {abs(retire)} years!")

with tab2:
    st.header("BMI and Health Analysis")
    
    col_w, col_h = st.columns(2)
    with col_w:
        weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=300.0, value=60.0, step=0.1)
    with col_h:
        height_cm = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
        
    if weight > 0 and height_cm > 0:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

    if st.button("Calculate BMI", key="btn_bmi"):
        st.subheader("Results")
        st.write(f"Your BMI is: **{bmi:.2f}**")

        if bmi <= 18.5:
            st.warning("**underweight**")
        elif bmi > 18.5 and bmi <= 24.9:
            st.success("**normal**")
        elif bmi > 25 and bmi <= 29.9:
            st.warning("**overweight**")
        elif bmi > 30 and bmi <= 34.9:
            st.warning("**obese**")
        elif bmi > 35 and bmi <= 39.9:
            st.error("**severely obese**")
        elif bmi > 40:
            st.error("**morbidly obese**") 


with tab3:
    st.header("Blood Pressure and Health Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        systolic = st.number_input("Systolic (Upper number - mmHg):", min_value=50, max_value=250, value=120, step=1)
    with col2:
        diastolic = st.number_input("Diastolic (Lower number - mmHg):", min_value=30, max_value=150, value=80, step=1)

    if st.button("Analyze Blood Pressure", key="btn_bp"):
        st.subheader("Results")
    
    # Blood pressure classification based on AHA guidelines
        if systolic < 90 and diastolic < 70:
            st.warning("Blood Pressure: Low Blood Pressure (Hypotension)")
        elif systolic < 120 and diastolic < 80:
            st.success("Blood Pressure: Normal")
        elif 120 <= systolic < 130 and diastolic < 80:
            st.warning("Blood Pressure: Elevated")
        elif (130 <= systolic < 140) or (80 <= diastolic < 90):
            st.warning("Blood Pressure: High Blood Pressure (Hypertension Stage 1)")
        elif systolic >= 140 or diastolic >= 90:
            st.error("Blood Pressure: High Blood Pressure (Hypertension Stage 2)")
            
        if systolic > 180 or diastolic > 120:
            st.error("🚨 HYPERTENSIVE CRISIS: Consult your doctor immediately!")

with tab4:
    st.header("Emergency Patient Vitals & Triage")
    
    patient_id = st.text_input("Patient Name:")
    
    st.markdown("### 📋 Input Vitals")
    
    # 2-column layout for vitals inputs
    v_col1, v_col2 = st.columns(2)
    
    with v_col1:
        # 1. Respiratory Rate
        resp_rate = st.number_input("1. Respiratory Rate (breaths/min):", min_value=0, max_value=80, value=16, step=1)
        
        # 2. Oxygen Saturation
        spo2 = st.number_input("2. Oxygen Saturation (SpO2 %):", min_value=0, max_value=100, value=98, step=1)
        
        # 3. Blood Pressure (Using systolic as the primary triage filter)
        sys_bp = st.number_input("3. Systolic Blood Pressure (mmHg):", min_value=0, max_value=300, value=120, step=1)

    with v_col2:
        # 4. Body Temperature
        temp_c = st.number_input("4. Body Temperature (°C):", min_value=25.0, max_value=45.0, value=37.0, step=0.1)
        
        # 5. Glasgow Coma Scale (GCS ranges from 3 to 15)
        gcs = st.number_input("5. Glasgow Coma Scale (GCS 3-15):", min_value=3, max_value=15, value=15, step=1)

    # --- TRIAGE EVALUATION LOGIC ---
    if st.button("Run Triage Evaluation", key="btn_triage"):
        st.markdown("---")
        st.markdown("### 🚨 Triage Assessment Summary")
        
        if patient_id:
            st.write(f"**Patient:** {patient_id}")
            
            # Simple Clinical Alert Threshold Rules
            is_critical = gcs <= 8 or spo2 < 90 or resp_rate < 8 or resp_rate > 30 or sys_bp < 90
            is_urgent = (90 <= spo2 <= 94) or (21 <= resp_rate <= 30) or (temp_c >= 39.0 or temp_c <= 35.0) or (9 <= gcs <= 14)
            
            # Output color-coded recommendation based on inputs
            if is_critical:
                st.error("🟥 **LEVEL 1: IMMEDIATE RESUSCITATION REQUIRED**")
                st.markdown("""
                * **Triggers detected:** Critical neurological depression (GCS ≤ 8), severe hypoxia, or extreme respiratory failure.
                * **Action:** Move to Trauma/Resuscitation room instantly. Alert attending physician.
                """)
            elif is_urgent:
                st.warning("🟨 **LEVEL 2 / 3: URGENT / EMERGENT**")
                st.markdown("""
                * **Triggers detected:** Abnormal vitals present (mild hypoxia, tachypnea, high fever, or altered consciousness).
                * **Action:** Assign to monitored bed. Re-evaluate within 15 minutes.
                """)
            else:
                st.success("🟩 **LEVEL 4 / 5: STABLE / NON-URGENT**")
                st.markdown("""
                * **Triggers detected:** All 5 core vital signs fall within acceptable, safe boundaries.
                * **Action:** Patient safe for standard waiting zone or fast-track assessment.
                """)
                
            # Display a clean dashboard summary of the data
            st.markdown("**Vitals Logged:**")
            st.caption(f"Resp: {resp_rate} bpm | SpO2: {spo2}% | SBP: {sys_bp} mmHg | Temp: {temp_c}°C | GCS: {gcs}/15")
        else:
            st.info("Please enter a Patient Name or ID above to view the live vitals triage evaluation.")