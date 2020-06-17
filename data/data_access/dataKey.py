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

def retrun_month_df(user_df,month,year): 
    df_data_month = user_df[(user_df['years'] == year) & (user_df['months'] == month)]
    df_data_month['datetime'] = pd.to_datetime(df_data_month.datetime)
    df_data_month = df_data_month.sort_values(by='datetime',ascending =True).reset_index()
    return df_data_month

def return_user_activity_status(user_df):
    minEventCount = 100
    lastDateForFull = 20
    year = 2020
    months_to_check = [1,2,3,4,5]
    userDic = {}
    goodUsers = []
    for file in files:
        for month in range(1,12):
            if retrun_month_df(user_df,month,year).shape[0] > minEventCount and max(retrun_month_df(user_df,month,year)['datetime']).day > lastDateForFull:
                goodMonths.append(month)
        userDic[file] = goodMonths
    for i in list(userDic.keys()):
        if len([j for j in months_to_check if j in userDic[i]]) == len(months_to_check):
            goodUsers.append(i)
    if len(goodUsers) == 0:
        return False
    else:
        return True

def retrive_user_responses(column_name):
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


retrive_user_responses("num_people_living_with")