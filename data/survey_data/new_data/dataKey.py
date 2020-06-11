import pandas as pd

def retrive_question_data(column_name):
    answers = {}
    input_file_name = "data_dict.csv"
    df = pd.read_csv(input_file_name)
    question_row = df.loc[df['Variable / Field Name'] == column_name].iloc[0]
    question = question_row['Field Label']
    answers_raw = question_row['Choices, Calculations, OR Slider Labels']
    for raw_answer in answers_raw.split(" | "):
        split_answer = raw_answer.split(", ")
        answers[split_answer[0]] = split_answer[1]
    return question,answers

