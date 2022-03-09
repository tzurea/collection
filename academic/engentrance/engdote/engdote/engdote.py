from random import random
from engdote.config import *
from engdote.database.db import *
from datetime import date
from engdote.utils.helpers import *

connection = create_connection(DATABASE)


def create_db_tables(connection=connection):
    for sql_execute_statement in create_tables_list:
        execute_sql(connection, sql_execute_statement)


class EngDoteTypes:
    def pea():
        return MODEL_TEST_URI, MOCK_TEST_DATA

    def daily():
        return DAILY_TEST_URI, MOCK_TEST_DATA

    def csit():
        return MODEL_TEST_URI, MOCK_TEST_DATA

    def be():
        return MOCK_TEST_URI, MOCK_TEST_DATA


def get_questions(url, data={}):
    response_data = post_request(url, HEADERS, data)
    question_list, response_data = get_post_data(response_data)
    response_data = post_request(QUESTION_URI, HEADERS, data=response_data)
    return question_list, response_data


def question_parameters(response_data):
    question_list = []
    for index, question in enumerate(response_data):
        question = question["questionData"]
        id = question["id"]
        marks = question["marks"]
        subject_id = question["subject_id"]
        chapter_id = question["chapter_id"]
        unit_id = question["unit_id"]
        quest_title = get_raw_text(question["quest_title"])
        ans1_txt = get_raw_text(question["ans1_txt"])
        ans2_txt = get_raw_text(question["ans2_txt"])
        ans3_txt = get_raw_text(question["ans3_txt"])
        ans4_txt = get_raw_text(question["ans4_txt"])
        is_passage = question["is_passage"]
        try:
            right_answer = question["right_answer"]
        except:
            right_answer = None
        question_list.append(
            (
                id,
                marks,
                subject_id,
                chapter_id,
                unit_id,
                quest_title,
                ans1_txt,
                ans2_txt,
                ans3_txt,
                ans4_txt,
                right_answer,
                is_passage,
            )
        )
    return question_list


def engdote(test_type=None):
    get_parameters = getattr(EngDoteTypes, test_type)
    url, data = get_parameters()
    question_list, response_data = get_questions(url, data=data)
    question_list = (int(random() * (10 ** 10)), str(date.today()), question_list)
    response_data = question_parameters(response_data)
    sql_statement_id = "sql_insert_{}".format(test_type)
    sql_statement_id = eval(sql_statement_id)
    print(question_list)
    execute_sql(connection, sql_statement_id, sql_entries=question_list)

    for i in response_data:
        execute_sql(connection, sql_insert_question, sql_entries=i)
