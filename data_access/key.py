import glob
import pandas as pd


def retrieve_question_data(column_name):
    answers = {}
    input_file_name = "survey_data_dict.csv"
    df = pd.read_csv(input_file_name)
    question_row = df.loc[df['Variable / Field Name'] == column_name].iloc[0]
    question = question_row['Field Label']
    answers_raw = question_row['Choices, Calculations, OR Slider Labels']
    for raw_answer in answers_raw.split(" | "):
        split_answer = raw_answer.split(", ")
        answers[split_answer[0]] = split_answer[1]
    return question,answers


def retrieve_all_questions():
    question_key = {}
    input_file_name = "data_dict.csv"
    df = pd.read_csv(input_file_name)
    for column in df['Variable / Field Name']:
        question_row = df.loc[df['Variable / Field Name'] == str(column)].iloc[0]
        question = question_row['Field Label']
        question_key[column] = question
    return question_key

def retrive_custom_user_groups(group_name,group_params):
    user_responses = {}
    for i in group_params['categories']:
        user_responses[i] = {}
    userCount = 0
    files = glob.glob('user_search_data/*.csv')
    input_file_name = "processed_survey_data.csv"
    df = pd.read_csv(input_file_name)
    for i,row in df.iterrows():
        file = [file for file in files if str(row["record_id"])+"_" in file]
        df_temp = pd.read_csv(file[0])
        if row[group_params["score_field"]] <= group_params["threshold"]:
            user_responses[group_params["categories"][0]][row["record_id"]] = df_temp
            userCount += 1 
        else:
            user_responses[group_params["categories"][1]][row["record_id"]] = df_temp
            userCount += 1
    for i in user_responses.keys():
        print(i+" | Percentage of Sample: "+str("{0:.0%}".format(len(user_responses[i].keys())/userCount)))
    return user_responses   


def retrieve_user_groups(column_name):
    custom_groups = {"anxiety":{"threshold":9,"categories":["not_anxious","anxious"],"score_field":"gad7_score"},"self_esteem":{"threshold":15,"categories":["low_self_esteem","not_low_self_esteem"],"score_field":"selfesteem_score"}}        
    if column_name.lower() in custom_groups.keys():
        return retrive_custom_user_groups(column_name.lower(),custom_groups[column_name.lower()])
    userCount = 0
    files = glob.glob('user_search_data/*.csv')
    question,answers = retrieve_question_data(column_name)
    user_responses = {}
    input_file_name = "processed_survey_data.csv"
    df = pd.read_csv(input_file_name)
    for i,row in df.iterrows():
        if row[column_name] in user_responses.keys():
            file = [file for file in files if str(row["record_id"])+"_" in file]
            df_temp = pd.read_csv(file[0])
            user_responses[row[column_name]][row["record_id"]] = df_temp
            userCount += 1 
        else:
            file = [file for file in files if str(row["record_id"])+"_" in file]
            df_temp = pd.read_csv(file[0])
            user_responses[row[column_name]] = {row["record_id"]:df_temp}
            userCount += 1
    print("Question:",question)
    print("Key:")
    for i in answers.keys():
        print(i,"=",answers[i]+" | Percentage of Sample: "+str("{0:.0%}".format(len(user_responses[int(i)].keys())/userCount)))
    return user_responses
