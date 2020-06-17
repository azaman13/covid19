import pandas as pd

def condence_df(df_raw_data):
    df_new = pd.DataFrame()
    temp_store = []
    column_title = ""
    for col in df_raw_data.columns:
        if len(col.split('___')) != 1:
            if len(temp_store) == 0 or int(col.split('___')[-1]) > temp_store[-1]:
                temp_store.append(int(col.split('___')[-1])) 
                column_title = col.split('___')[0]
            else:
                df_new[column_title] = df_raw_data.apply(lambda r: " ".join([str(i) for i in temp_store if r[column_title+"___"+str(i)] == 1]), axis=1)
                temp_store = [int(col.split('___')[-1])]
                column_title = col.split('___')[0]
        else:
            if len(temp_store) > 0:
                df_new[column_title] = df_raw_data.apply(lambda r: " ".join([str(i) for i in temp_store if r[column_title+"___"+str(i)] == 1]), axis=1)
                temp_store = []
                column_title = ""
            df_new[col] = df_raw_data[col]
    return df_new

def compute_phq9_score(df):
    columns = ["phq9_"+str(i) for i in range(1,10)]
    df['phq9_score'] = df[columns].sum(axis=1)-9
    df = df.drop(columns=columns)
    return df

def compute_gad_7(df):
    start_index = df.columns.get_loc('feeling_nervous_anxious_or')
    end_index = df.columns.get_loc('feeling_afraid_as_if_somet')
    columns = df.columns[start_index:end_index+1]
    df['gad7_score'] = (df[columns].sum(axis=1))-7
    df = df.drop(columns=columns)
    return df   

def compute_selfesteem(df):
    mappingA = {1:3, 2:2, 3:1, 4:0, 0:0}
    mappingB = {1:0, 2:1, 3:2, 4:3, 0:0}
    columnsA = ['ros_satisfied_self','ros_good_qualities','ros_well_as_othres','ros_worth','ros_positive_attitude']
    columnsB = ['ros_good','ros_proud','ros_useless','ros_respect','ros_failure']
    for column in columnsA + columnsB:
        if column in columnsA:
            df[column] = df[column].apply(lambda x: mappingA[x])
        else:
            df[column] = df[column].apply(lambda x: mappingB[x])
    df['selfesteem_score'] = df[columnsA+columnsB].sum(axis=1)
    df = df.drop(columns=columnsA + columnsB) 
    return df

def compute_scores(df):
    df1 = compute_phq9_score(df)
    df2 = compute_gad_7(df1)
    df_w_scores = compute_selfesteem(df2)
    return df_w_scores

def drop_excess(df):
    print(df.columns[0])
    excess_columns = ['redcap_survey_identifier','redcap_event_name','ph_id2_2bf']
    df = df.drop(columns=excess_columns)
    df.set_index('record_id', inplace=True)
    return df
      
def main():
    input_file_name = "raw_data.csv"
    output_file_name = "processed_data.csv"
    print("Processing",input_file_name)
    df_raw_data = pd.read_csv(input_file_name)
    condenced_df = condence_df(df_raw_data)
    print("File condenced")
    print("Computing scores...")
    df_w_scores = compute_scores(condenced_df)
    print("Cleaning df...")
    final_df = drop_excess(df_w_scores)
    print("New File Created:",output_file_name)
    final_df.to_csv(output_file_name)

main()

