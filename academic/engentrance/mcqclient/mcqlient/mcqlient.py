import json
import uuid
import time
import sqlite3
import datetime
from pyowm import OWM

OPEN_WEATHER_MAP_CONFIG = {
    'unit': 'celsius',
    'key':  'f45192f86e99294305192beccdb5a3d8',
    'city_id': 1283617
}

chapter_id_list = [140]
no_of_questions_at_a_day = 2
try:
    open_weather_map = OWM(OPEN_WEATHER_MAP_CONFIG['key'])
    weather_manager = open_weather_map.weather_manager()
    weather_observation = weather_manager.weather_at_id(OPEN_WEATHER_MAP_CONFIG['city_id'])
    weather = weather_observation.weather
except:
    pass

current_temperature = weather.temperature(OPEN_WEATHER_MAP_CONFIG['unit'])
current_speed = weather.wnd['speed']
current_direction = weather.wnd['deg']
current_humidity = weather.current_humidity
current_pressure = weather.pressure['press']

user_options = {
    'user_name' : '',
    'registration_details': {
        'date_of_registration': '',
        'registration_start_time' : '',
        'registration_end_time' : '',
    },
    'user_details': {
        'chapter_id_list' : [],
        'no_of_questions_at_a_day' : '',
        'total_time_spent': '',
        'no_of_questions_done' : '',
        'no_of_right_answers' : '',
        'no_of_sessions' : '',
        'seen_questions' : [],
        'user_sessions' : [
            {
                'session_id': '',
                'session_hash' : '',
                'time_taken' : '',
                'no_of_questions' : '',
                'no_of_chapters' : '',
                'no_of_right_answers' : '',
                'session_date' : '',
                'session_start_time' : '',
                'session_end_time' : '',
                'chapter_id_list' : [],
                'question_id_list' : [],
                'no_of_questions_from_each_chapter':'',
                'session_day_temperature' : '',
                'session_day_wind_speed' : '',
                'session_day_wind_direction' : '',
                'session_day_atmospheric_pressure':'',
                'session_day_humidity' : '',
                'question_properties' : {
                    140 : [
                        {
                            'id' :'',
                            'start_time': '',
                            'end_time' : '',
                            'chosen_answer': '',
                            'right_answer' : '',
                            'was_correct' : False                      
                        }

                    ]
                }
            }
        ]
    }
}


db_path = '/tmp/data.db'

sql_create_users_table = """CREATE TABLE IF NOT EXISTS users
                    ( id integer primary key ,
                    user_name text,
                    registration_details text,
                    user_details text
                      )"""



def create_connection(db_path):
    connection = sqlite3.connect(db_path)
    return connection


def execute_sql(connection, sql_execute_statement, sql_entries=None):
    cursor = connection.cursor()
    cursor.execute(sql_execute_statement)
    connection.commit()

connection = create_connection(db_path)
cursor = connection.cursor()

def create_tables():
    execute_sql(connection, sql_create_users_table)


query = "SELECT user_details FROM users WHERE user_name={} ;".format(str(user_name))
cursor.execute(query)
user_details = cursor.fetchone()
user_details = json.loads(user_details)
user_details['chapter_id_list'] = chapter_id_list 
user_details['number_of_questions_at_a_day'] = no_of_questions_at_a_day  
total_time_spent = user_details['total_time_spent']
no_of_questions_done = user_details['no_of_questions_done']
no_of_right_answers = user_details['no_of_right_answers']
no_of_sessions = user_details['no_of_sessions']
seen_questions = user_details['seen_questions']    
user_sessions = user_details['user_sessions']
last_session = user_sessions[-1]
last_session_id = last_session['id']
new_session = {
                'session_id': last_session_id + 1,
                'session_hash' : uuid.uuid4().hex,
                'no_of_questions' : '',
                'no_of_chapters' : '',
                'no_of_right_answers' : '',
                'session_date' : datetime.date.today(),
                'session_start_time' : time.time(),
                'session_end_time' : '',
                'chapter_id_list' : [],
                'question_id_list' : [],
                'no_of_questions_from_each_chapter': no_of_questions_at_a_day,
                'session_day_temperature' : current_temperature,
                'session_day_wind_speed' : current_speed,
                'session_day_wind_direction' : current_direction,
                'session_day_atmospheric_pressure': current_pressure,
                'session_day_humidity' : current_humidity,
                'question_properties' : {}
}

number_of_questions = 0
number_of_chapters = 0
number_of_right_answers_at_session = 0
question_id_list = []
chapter_id_list = []
for chapter in chapter_id_list:
    query = "SELECT id,quest_title,ans1_txt,ans2_txt,ans3_txt,ans4_txt,right_answer from questions where chapter_id={} ;".format(str(chapter))
    cursor.execute(query)
    questions_list = cursor.fetchall()
    questions_list = json.loads(questions_list)
    new_session['question_properties'][chapter] = []
    number_of_questions_in_this_chapter = 0
    for question in questions_list:
        if no_of_questions_in_this_chapter == no_of_questions_at_a_day:
            break
        if question[0] not in seen_questions:
            id = question[0]
            quest_title = question[1]
            ans1_txt = question[2]
            ans2_txt = question[3]
            ans3_txt = question[4]
            ans4_txt = question[5]
            right_answer = question[6]
            start_time = time.time()
            print(quest_title)   
            print()
            print()
            print(ans1_txt)
            print()
            print(ans2_txt)
            print()
            print(ans3_txt)
            print()
            print(ans4_txt)
            print()
            chosen_answer = input()
            end_time = time.time()
            user_details['total_time_spent'] += ( end_time - start_time)
            was_correct = False
            if chosen_answer == right_answer:
                number_of_right_answers_at_session += 1
                was_correct = True
            number_of_questions += 1
            number_of_questions_in_this_chapter += 1
            question_id_list.append(id)             
            seen_questions.append(id)
            new_session['question_properties'][chapter].append(
                {
                    'id':id,
                    'start_time':start_time,
                    'end_time':end_time,
                    'chosen_answer':chosen_answer,
                    'right_answer': right_answer,
                    'was_correct' :was_correct
                }
            )
    number_of_chapters += 1
    chapter_id_list.append(chapter)

user_details['no_of_questions_done'] += no_of_questions 
user_details['no_of_right_answers'] += no_of_right_answers_at_session          
new_session['session_end_time'] = time.time() 
new_session['no_of_questions'] = no_of_questions
new_session['no_of_chapters'] = no_of_chapters
new_session['no_of_right_answers'] = no_of_right_answers
new_session['chapter_id_list'] = chapter_id_list
new_session['question_id_list'] = question_id_list
user_details['user_sessions'].append(new_session)



sql_insert_session = 'UPDATE users SET user_details={} WHERE user_name={}'.format(json.dumps(user_details),user_name)
