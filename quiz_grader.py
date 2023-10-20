# Import required dependencies to use Google's API
import os.path
import pandas as pd
from assets import classcode, quizcode, max_score, quiz_range

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

creds = None

# Define the accesses to be granted
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', # View your Google Classroom classes.
        'https://www.googleapis.com/auth/classroom.rosters', # Manage your Google Classroom class rosters.
        'https://www.googleapis.com/auth/classroom.profile.emails', # View the email addresses of people in your classes.
        'https://www.googleapis.com/auth/classroom.topics', #See, create, and edit topics in Google Classroom.
        'https://www.googleapis.com/auth/classroom.coursework.students', # Manage coursework and grades for students
        'https://www.googleapis.com/auth/classroom.courseworkmaterials', # See, edit, and create classwork materials in Google Classroom.
        'https://www.googleapis.com/auth/spreadsheets'] # See all your Google Sheets spreadsheets.

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

def QuizGrader(filepath, link, sheet_name, course_name, quiz_name, credentials):  

    QUIZ_DF = pd.read_csv(filepath) # Quiz CSV Path
    SCORE_ACADEMY_LINK = link # Score Academy Link
    NAMA_SHEET = sheet_name # Sheet Name (Wizard) 

    creds = credentials

    # In the section, the user is going to access the scores that have been entered on the spreadsheet `Score Academy`  
    # Input the link to the Score Academy spreadsheet and retrieve the Spreadsheet ID

    SCORE_ACADEMY_ID = SCORE_ACADEMY_LINK.split(sep='/')[-2]

    # Specify the sheet and the cell ranges that is going to be accessed

    GRADE_RANGE = [f'{NAMA_SHEET}!D:E', f'{NAMA_SHEET}!F:H', f'{NAMA_SHEET}!M:R']

    # Call the Google Spreadsheet API and retrieve the values of the ranges that have been specified

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets().values().batchGet(spreadsheetId=SCORE_ACADEMY_ID,
                                                         ranges=GRADE_RANGE).execute()
        values = sheet.get('valueRanges', [])
            
    except HttpError as error:
        print(error)

    # Concat the retrieved values as a dataframe

    email = pd.DataFrame(values[0].get('values'))
    grade_dv = pd.DataFrame(values[1].get('values'))
    grade_ml = pd.DataFrame(values[2].get('values'))

    df = pd.concat([email, grade_dv, grade_ml], axis=1)
    df.columns = df.iloc[0]
    df.drop(index=0, inplace=True)
    df['Email'] = df['Email'].str.lower() 

    # In this section, the user is going to choose which Google Classroom Course that is going to be accessed
    # Call the Google Classroom API to access various methods with user's access from the credential that has been authenticated

    service = build('classroom', 'v1', credentials=creds)

    # Use the `courses().list()` method to show a list of the user's courses

    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')

    course_input = course_name
    course_lowercase = course_input.lower()
    course_id = None

    for course in courses:
        if course_lowercase == course['name'].lower():
            course_id = course['id']
            break

    if course_id == None:
        raise Exception(f"{course_input} course not found")

    else:
        print(f'{course_input} found with ID {course_id}')

    
    # Input the quiz code (**case-insensitive**) that is going to be accessed. If the quiz was found, the quiz's `id` will be retrieved. **Quiz Input :**
    # 
    #  - `P4DS` : 1. Q: Programming for Data Science (P4DS) & Practical Statistic (PS)
    #  - `DV` : 2. Q: Data Visualization (DV)
    #  - `IP` : 3. Q: Interactive Plotting (IP)
    #  - `RM`
    #  - `C1`
    #  - `C2`
    #  - `UL`
    #  - `TS`
    #  - `NN`

    service = build('classroom', 'v1', credentials=creds)
    response = service.courses().courseWork().list(courseId=course_id).execute()
    classworks = response.get('courseWork')

    while response.get('nextPageToken'):
        response = service.courses().students().list(courseId=course_id, pageToken = response['nextPageToken']).execute()
        classworks.extend(response.get('courseWork'))

    quiz_input = quiz_name
    quiz_id = None

    for classwork in classworks:
        if classwork['title'] == classcode(quiz_input):
            quiz_id = classwork['id']
            break

    if quiz_id == None:
        raise Exception(f"Quiz not found")
    else:
        print(f"{classwork['title']} Quiz was found")

    # In this section, the received grade is going to be written in Score Academy

    QUIZ_DF['USER EMAIL'] = QUIZ_DF['USER EMAIL'].str.strip().str.lower()
    QUIZ_DF['PASSED STATUS'] = QUIZ_DF['PASSED STATUS'].str.strip().str.lower()
    QUIZ_DF = QUIZ_DF[QUIZ_DF['PASSED STATUS'] == "yes"]
    QUIZ_DF = QUIZ_DF.drop_duplicates("USER EMAIL")
    passed_email = QUIZ_DF["USER EMAIL"]

    df.loc[df["Email"].isin(passed_email.values), quizcode(quiz_input)] = max_score(quiz_input)
    df.loc[~df["Email"].isin(passed_email.values), quizcode(quiz_input)] = 0

    try:
        service = build('sheets', 'v4', credentials=creds)
        
        values = [[x] for x in df[quizcode(quiz_input)].values.tolist()]

        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SCORE_ACADEMY_ID, range=f'{NAMA_SHEET}!{quiz_range(quiz_input)}',
            valueInputOption="USER_ENTERED", body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        print(f"An error occurred: {error}")

    # Use the `courses().courseWork().studentSubmissions().list()` method to store a list of the quiz's submissions

    submissions = []

    service = build('classroom', 'v1', credentials=creds)
    response = service.courses().courseWork().studentSubmissions().list(
        courseId=course_id,
        courseWorkId=quiz_id).execute()
    submissions.extend(response.get('studentSubmissions', []))

    while response.get('nextPageToken'):
        response = service.courses().courseWork().studentSubmissions().list(
            courseId=course_id,
            courseWorkId=quiz_id,
            pageToken = response['nextPageToken']).execute()
        submissions.extend(response.get('studentSubmissions'))

    
    # All the stored submission are graded as draft in accordance with the student's e-mail in the Google Classroom using `courses().courseWork().studentSubmissions().patch()` method

    grade = []
    warn = []
    quiz_code = quizcode(quiz_input)

    for submission in submissions:
        # Retrieve student's email
        submission_profile = service.courses().students().get(courseId=course_id, userId=submission['userId']).execute()
        student_df = df.loc[df['Email Classroom'] == submission_profile['profile']['emailAddress']]
        
        # Retrieve student's grade
        if not student_df.empty:
            if isinstance(student_df[quiz_code].values[0], int) or student_df[quiz_code].values[0].isnumeric():
                submission_grade = student_df[quiz_code].values[0]
            else:
                warn.append(f"{submission_profile['profile']['name']['fullName']} ({submission_profile['profile']['emailAddress']}) has no grade")
                grade.append([submission_profile['profile']['name']['fullName'], submission_profile['profile']['emailAddress'], None, "NO GRADE"])
                continue      
        else:
            warn.append(f"{submission_profile['profile']['name']['fullName']} ({submission_profile['profile']['emailAddress']}) was not found")
            grade.append([submission_profile['profile']['name']['fullName'], submission_profile['profile']['emailAddress'], None, "NOT FOUND"])
            continue

        # Grade the submission as draftGrade
        studentSubmission = {
            'draftGrade': str(submission_grade),
            'assignedGrade': str(submission_grade)
        }

        response = service.courses().courseWork().studentSubmissions().patch(
            courseId=course_id,
            courseWorkId=classwork['id'],
            id=submission['id'],
            updateMask='assignedGrade,draftGrade',
            body = studentSubmission).execute()
        
        if submission['state'] == 'TURNED_IN':
            response = service.courses().courseWork().studentSubmissions().return_(
                courseId=course_id,
                courseWorkId=classwork['id'],
                id=submission['id']).execute()
        
        grade.append([submission_profile['profile']['name']['fullName'], submission_profile['profile']['emailAddress'], submission_grade, "GRADED"])

    grade_df = pd.DataFrame(grade, columns=['Name', 'Email Classroom', 'Grade', 'Status'])
    grade_df.sort_values('Status')
    
    return grade_df, warn


