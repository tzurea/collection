import sqlite3


sql_create_questions_table = """CREATE TABLE IF NOT EXISTS questions
                    ( id integer primary key ,
                     marks integer,
                     subject_id integer,
                     chapter_id integer,
                     unit_id integer,
                     quest_title text,
                     ans1_txt text,
                     ans2_txt text,
                     ans3_txt text,
                     ans4_txt text,
                     right_answer text,
                     is_passage text)"""


sql_create_pea_mock_table = """CREATE TABLE IF NOT EXISTS pea_question_ids
                    ( id integer primary key autoincrement,
                     date_added text,
                     question_lists text)"""

sql_create_csit_mock_table = """CREATE TABLE IF NOT EXISTS csit_question_ids
                    ( id integer primary key autoincrement,
                     date_added text,
                     question_lists text)"""


sql_create_be_mock_table = """CREATE TABLE IF NOT EXISTS be_question_ids
                    ( id integer primary key autoincrement,
                     date_added text,
                     question_lists text)"""

sql_create_qbank_mock_table = """CREATE TABLE IF NOT EXISTS qbank_question_ids
                    ( id integer primary key autoincrement,
                     date_added text,
                     question_lists text)"""


sql_create_daily_mock_table = """CREATE TABLE IF NOT EXISTS daily_question_ids
                    ( id integer primary key autoincrement,
                     date_added text,
                     question_lists text)"""

create_tables_list = [
    sql_create_be_mock_table,
    sql_create_csit_mock_table,
    sql_create_pea_mock_table,
    sql_create_qbank_mock_table,
    sql_create_daily_mock_table,
    sql_create_questions_table,
]


sql_insert_question = "INSERT OR IGNORE INTO questions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
sql_insert_pea = "INSERT OR IGNORE INTO pea_question_ids VALUES (?,?,?)"
sql_insert_csit = "INSERT OR IGNORE INTO csit_question_ids VALUES (?,?,?)"
sql_insert_be = "INSERT OR IGNORE INTO be_question_ids VALUES (?,?,?)"
sql_insert_qbank = "INSERT OR IGNORE INTO qbank_question_ids VALUES (?,?,?)"
sql_insert_daily = "INSERT OR IGNORE INTO daily_question_ids VALUES (?,?,?)"


def create_connection(db_path):
    connection = sqlite3.connect(db_path)
    return connection


def execute_sql(connection, sql_execute_statement, sql_entries=None):
    cursor = connection.cursor()
    if sql_entries:
        cursor.execute(sql_execute_statement, sql_entries)
    else:
        cursor.execute(sql_execute_statement)
    connection.commit()
