import os
import pandas as pd
import streamlit as st
from quiz_grader import QuizGrader
import time


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the accesses to be granted
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', # View your Google Classroom classes.
        'https://www.googleapis.com/auth/classroom.rosters', # Manage your Google Classroom class rosters.
        'https://www.googleapis.com/auth/classroom.profile.emails', # View the email addresses of people in your classes.
        'https://www.googleapis.com/auth/classroom.topics', #See, create, and edit topics in Google Classroom.
        'https://www.googleapis.com/auth/classroom.coursework.students', # Manage coursework and grades for students
        'https://www.googleapis.com/auth/classroom.courseworkmaterials', # See, edit, and create classwork materials in Google Classroom.
        'https://www.googleapis.com/auth/spreadsheets'] # See all your Google Sheets spreadsheets.

creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('classroom', 'v1', credentials=creds)

# Use the `courses().list()` method to show a list of the user's courses

results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])

st.title("Algoritma Online Quiz Grader")
st.write("#")

course_name = None
specialization = None
filepath = None
grade_table = pd.DataFrame()
warning_text = ""

course_name = st.selectbox("Select Course", [course['name'] for course in courses], index=None)

if course_name != None:
    specialization = st.selectbox("Select Specialization", ['Data Analytics', 'Data Visualization', 'Machine Learning'], index=None)

if specialization != None:
    col1, col2 = st.columns(2)
    with col1:
        if specialization == 'Data Visualization':
            quiz_name = st.selectbox("Select Class", ['P4DS', 'DV', 'IP'])
        elif specialization == 'Machine Learning':
            quiz_name = st.selectbox("Select Class", ['RM', 'C1', 'C2', 'UL', 'TS', 'NN'])
        elif specialization == 'Data Analytics':
            quiz_name = st.selectbox("Select Class", ['P4DA', 'EDA', 'DWV', 'SQL', 'IML1', 'IML2'])

    with col2:
        sheet_name = st.text_input("Input Score Academy Sheet Name", value="Academy: Batch 23")

    filepath = st.file_uploader("Upload Algoritma Online CSV", type="csv")

if filepath != None:
    _, _, col3, col4, _ = st.columns(5)

    with col3:
        button = st.button('Grade Quiz')
    with col4:
        if button:
            with st.spinner('Grading...'):
                grade_table, warnings = QuizGrader(filepath=filepath,
                                                  link='https://docs.google.com/spreadsheets/d/1cGJ0pn9k9gKCBnceWVwaL9D7BBDMNjLh8uPYlaBlJi8/edit#gid=455932940', 
                                                  sheet_name=sheet_name, 
                                                  course_name=course_name, 
                                                  quiz_name=quiz_name, 
                                                  credentials=creds)
    if button:
        success = st.success('Grading Successful!')
        my_bar = st.progress(0, text="Loading result. Please wait...")

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text="Loading result. Please wait...")
        time.sleep(1)
        
        my_bar.empty()
        success.empty()

        percent_complete = True
        
        if percent_complete:
            for warning in warnings:
                warning_text += f'  {warning}  \n'

            st.info(warning_text, icon='⚠️')
            st.dataframe(grade_table, use_container_width=True)