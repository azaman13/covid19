from data_access.key import retrieve_user_groups


dit = retrieve_user_groups("anxiety")

print(dit['not_anxious'].keys())
