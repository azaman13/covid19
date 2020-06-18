Last Updated: 06/18/2020

How to Use:

-- Your file must be in the main directory
-- Use the following import statement: from data_access.key import retrieve_question_data,retrieve_user_groups
-- Reference "survey_data_dict.csv" to find the column names for the questions you would like to group the users by. The "column_name" is found in "Variable / Field Name"

Functions:

retrieve_question_data(column_name)
-- description: Given the column name assosiated to a question, return the question and answers assosited to that question

-- arguments: 
++ column_name = Name of question column 

-- returns:
++ question = string containing the actual question asked on survey
++ answers = a dictonary in which the key is the raw survet response, and the value is the actual answer assosiated to the raw response


retrieve_user_groups(column_name)
-- description: Given the column name assosiated to a question, return a dictonary with users aggregated by their question response

-- arguments: 
++ column_name = Name of question column 

-- returns:
++ user_responses = A dictonary in which the keys are the raw question responses, and the value is another dictonary of users. 
                   The keys in the user dictonary are the users new survey ID, and the corresponding value is a pandas datafram containing all of the users browsing data

-- Edge cases: When attempting to retrive users aggregated by their depression, anxiety, etc, use the following as your column_name:
++ depression 
++ anxiety (gad7 > 9: anxious, gad7 <= 9: not anxious)
++ self_esteem (self-esteem score > 15: moderate to high self-esteem, gad7 <= 9: low self-esteem)


