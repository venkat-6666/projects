import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_filename = 'random_forest_model.joblib'
rf_model = joblib.load(model_filename)

# Define the symptoms list (assuming the same order as in your dataset)
symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
            'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
            'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
            'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
            'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
            'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
            'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
            'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
            'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
            'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
            'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
            'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
            'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
            'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
            'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
            'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
            'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression',
            'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
            'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
            'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
            'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
            'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1',
            'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
            'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails',
            'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

def predict_disease(symptoms_list):
    # Create a DataFrame from user input
    user_input = pd.DataFrame([symptoms_list], columns=symptoms)
    # Make predictions
    prediction = rf_model.predict(user_input)
    return prediction[0]

# Streamlit UI
st.title("Disease Prediction ")



# User input checkboxes
st.header("User Input")
user_input = []
for symptom in symptoms:
    user_input.append(st.checkbox(symptom, False, key=symptom))

# Make prediction on button click
if st.button("Predict"):
    result = predict_disease(user_input)
# Hospital Names For Diseases
    data_list = ["Fungal infection", "Allergy", "GERD", "Chronic cholestasis", "Drug Reaction", "Peptic ulcer diseae", "AIDS",
                "Diabetes", "Gastroenteritis", "Bronchial Asthma", "Hypertension", "Migraine", "Cervical spondylosis",
                "Paralysis (brain hemorrhage)", "Jaundice", "Malaria", "Chicken pox", "Dengue", "Typhoid", "hepatitis A",
                 "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "Alcoholic hepatitis", "Tuberculosis", "Common Cold",
                "Pneumonia", "Dimorphic hemmorhoids(piles)", "Heart attack", "Varicose veins", "Hypothyroidism", "Hyperthyroidism",
                 "Hypoglycemia", "Osteoarthristis", "Arthritis", "(vertigo) Paroymsal  Positional Vertigo", "Acne", "Urinary tract infection", "Psoriasis", "Impetigo"]
    hospital_names = ["Sri Konaseema Specialities Hospital in Amalapuram","Sri Surya Skin and Cosmetology Hospital in Amalapuram","Trinity Hospital in Amalapuram",
                    "Trinity Hospital in Amalapuram","Sri nidhi hospitals in Amalapuram","Sai Viswas hospital in Amalapuram","A.P Vaidya Vidhana Parishad area hospital in amalapuram",
                    "Mathrusri Nursing Home in Amalapuram","Sri nidhi hospitals in Amalapuram","Mathrusri Nursing Home in Amalapuram","Mathrusri Nursing Home in Amalapuram",
                    "Sri Hari hospital in amalapuram","KIMS hospital in Amalapuram","Mathrusri Nursing Home in Amalapuram","Mathrusri Nursing Home in Amalapuram",
                    "Mathrusri Nursing Home in Amalapuram","Sri Konaseema Specialities Hospital in Amalapuram","Sri Konaseema Specialities Hospital in Amalapuram",
                    "Sri Konaseema Specialities Hospital in Amalapuram","Trinity Hospital in Amalapuram","Trinity Hospital in Amalapuram","Trinity Hospital in Amalapuram",
                    "Trinity Hospital in Amalapuram","Trinity Hospital in Amalapuram","SriNidhi hospitals in Amalapuram","MathruSri Nursing Home in Amalapuram",
                    "United Hospital in Amalapuram","Trinity Hospital in Amalapuram","Adharsh Hospital in Amalapuram","Bolero hospital in RajamahendraVaram",
                    "Yashoda hospitals in Amalapuram","Sri nidhi hospitals in Amalapuram","Sri Surya Homoeo Stores and Clinic in Amalapuram","Sri nidhi hospitals in Amalapuram",
                    "Raja Orthopaedic Hospital in amalapuram","Raja Orthopaedic Hospital in amalapuram","United multi speaciality Hospital in Amalapuram","Trinity skin clinic in Amalapuram",
                    "United multispeciality hospital in Amalapuram","Trinity Skin Clinic in Amalapuram","Trinity Skin Clinic in Amalapuram"]
    h_N = hospital_names[data_list.index(result)]
    #printing the output
    st.success(f"The predicted disease is: {result} and \n Suggesting to go --{h_N}..")