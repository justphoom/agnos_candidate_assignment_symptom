import streamlit as st
import pickle
# import requests
from collections import Counter

data = pickle.load(open("patient_data.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
suggestion_list = []
def submit():
    patient_profile = {'gender':patient_gender, 'age':patient_age, 'search_term':patient_search_term}
    suggestion_list = recommend(patient_profile)
    print(suggestion_list)
    showSuggestion(suggestion_list)

def recommend(patient_data):
    symptom_list = []
    matching_data = data[data['feature'] == patient_data.get('gender') + ', ' + str(patient_data.get('age')) + ', '+ patient_data.get('search_term')]
    if matching_data.empty:
        pass
        
    else :
        index = matching_data.index[0]

        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
        possible_solution = []
        for i in distance:
            possible_solution.append(data.iloc[i[0]].search_term.strip().split(', '))
            flatted_solutions = [item for sublist in possible_solution for item in sublist]
            solution_counts = Counter(flatted_solutions)
            sorted_solutions_by_frequency = sorted(solution_counts.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_solutions_by_frequency[0:3]:
            symptom_list.append(i[0])
    return symptom_list

def showSuggestion(suggestion_list):
    if len(suggestion_list) == 0:
        st.subheader("Please put a propoer symptom value")
    else:
        for item in suggestion_list:
            st.badge(item)

st.title('Symptom Suggestion App')
with st.form("patient_form"):
    st.write("Please fill in the from")
    patient_gender = st.selectbox("Gender", ("male", "female"))
    patient_age = st.number_input("Age", min_value=0, max_value=99, step=None, placeholder="Type your age...")
    patient_search_term = st.text_input("Symptom", placeholder="Type your symptom...")
    st.form_submit_button('Submit', on_click=submit)
    

    