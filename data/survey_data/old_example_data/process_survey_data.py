import csv, pandas as pd, numpy as np, math
from datetime import datetime

def compute_phq9_score(row,phq9_1_index, phq9_final_index):
    if row:
        zero = []#"Not At all",
        one = []#"Several Days",
        two = []#"More Than Half the Days",
        three = []#"Nearly Every Day"
        
        phq1 = row[1].phq9_1
        phq2 = row[1].phq9_2
        phq3 = row[1].phq9_3
        phq4 = row[1].phq9_4
        phq5 = row[1].phq9_5
        phq6 = row[1].phq9_6
        phq7 = row[1].phq9_7
        phq8 = row[1].phq9_8
        phq9 = row[1].phq9_9
        phq_final = row[1].phq9_final
        suicide = row[1].suicide
        
        for phq in row[1].tolist()[phq9_1_index : phq9_final_index + 1]:
            if phq == 0:
            	zero.append(phq)
            elif phq == 1:
            	one.append(phq)
            elif phq == 2:
            	two.append(phq)
            elif phq == 3:
            	three.append(phq)
        #print(zero)
        #print(one)
        #print(two)
        #print(three)
        zero = np.array(zero, dtype='float')
        one = np.array(one, dtype='float')
        two = np.array(two, dtype='float')
        three = np.array(three, dtype='float')
        
        score = np.sum(zero) + np.sum(one) + np.sum(two) + np.sum(three)
        
        return score,phq_final,suicide


def compute_gad_7(row, gad7_start_index, gad7_end_index):
    if row:
        zero = []#"Not At all",
        one = []#"Several Days",
        two = []#"More Than Half the Days",
        three = []#"Nearly Every Day"
        for value in row[1].tolist()[gad7_start_index : gad7_end_index + 1]:
            if value == 0:
            	zero.append(value)
            elif value == 1:
            	one.append(value)
            elif value == 2:
            	two.append(value)
            elif value == 3:
            	three.append(value)
             
        zero = np.array(zero, dtype='float')
        one = np.array(one, dtype='float')
        two = np.array(two, dtype='float')
        three = np.array(three, dtype='float')
        score = np.sum(zero) + np.sum(one) + np.sum(two) + np.sum(three)
        return score
    

def compute_selfesteem(row):
    if row:
        #1, Strongly Agree
        #2, Agree
        #3, Disagree
        #4, Strongly Disagree
        #For questions 1, 3, 4, 7, and 10 score SA=3, A=2, D=1, and SD=0:
        mappingA = {1:3, 2:2, 3:1, 4:0, 0:0}
        ros1 = row[1].ros_satisfied_self
        ros3 = row[1].ros_good_qualities
        ros4 = row[1].ros_well_as_othres
        ros7 = row[1].ros_worth        
        ros10 = row[1].ros_positive_attitude
        # Sanitize the values        
        if math.isnan(ros1):
            ros1 = 0
        if math.isnan(ros3):
            ros3 = 0
        if math.isnan(ros4):
            ros4 = 0
        if math.isnan(ros7):
            ros7 = 0
        if math.isnan(ros10):
            ros10 = 0
        
        
        mappingB = {1:0, 2:1, 3:2, 4:3, 0:0}
        #For questions 2, 5, 6, 8, and 9 score SA=0, A=1, D=2, and SD=3:
        ros2 = row[1].ros_good
        ros5 = row[1].ros_proud
        ros6 = row[1].ros_useless
        ros8 = row[1].ros_respect
        ros9 = row[1].ros_failure
        #sanitize the values
        if math.isnan(ros2):
            ros2 = 0
        if math.isnan(ros5):
            ros5 = 0
        if math.isnan(ros6):
            ros6 = 0
        if math.isnan(ros8):
            ros8 = 0
        if math.isnan(ros9):
            ros9 = 0
                  
        A = mappingA[ros1] + mappingA[ros3] + mappingA[ros4] + mappingA[ros7] + mappingA[ros10]
        
        B = mappingB[ros2] + mappingB[ros5] + mappingB[ros6] + mappingB[ros8] + mappingB[ros9]
        
        
        return A + B


def main ():
    file = '../../data/campus-survey-data/CampusStudysept2019_DATA_2020-05-11_1711.csv'
    data = pd.read_csv(file)
    
    record_ids = []
    time_stamps = []
    ages = []
    months = []
    # gender
    #1 is male
    #2 is female 
    #3 is other    
    gender = []
    
    # this is string
    nationality = []
    
    # race 1: while, 2: black/african american, 3:others
    race = []
    
    permanent_home = []
    #    1, Grater Rochester area
    #    2, Elsewhere in NY state
    #    3, Elsewhere in the USA
    #    4, Outside of the USA
    
    first_gen = []
    # 1 yes
    # 0 No

    financial_support_from_parents = []
    financial_support_from_loans = []
    financial_support_from_self = []
    #0, Parents or guardians
    #1, Loans
    #2, My own savings and earnings
    living_w_parents = data.housing___0.tolist()
    living_dorm_single = data.housing___1.tolist()
    living_dorm_shared = data.housing___2.tolist()
    living_greek_single = data.housing___3.tolist()
    living_greek_shared = data.housing___4.tolist()
    living_off_campus_single = data.housing___5.tolist()
    living_off_campus_shared = data.housing___6.tolist()
    
    college_year = []
    #0, With parents or guardians
    #1, University dorm (single)
    #2, University dorm (shared room)
    #3, Fraternity or sorority (single room)
    #4, Fraternity or sorority (shared room)
    #5, University or off-campus house or apartment (single)
    #6, University or off-campus house or apartment (with housemates)    
    

    majors = [str(i).lower() for i in data.college_major.tolist()]    
    
    
    gpa_current = data.gpa_current.tolist()
    gpa_last_sem_end = data.gpa_last_sem_end.tolist()
    gpa_last_sem_start = data.gpa_last_sem_start.tolist()
    
    change_major = data.change_major.tolist()
    #1, Yes
    #0, No
    change_major_year = data.change_major_year.tolist()
    # here is the year mapping, for future use and reference
    year_mapping = {    
        0: 2019,
        1: 2018,
        2: 2017,
        3: 2016,
        4: 2015,
        5: 2014,
        6: 2013,
        7: 2012,
        8: 2011,
        9: 2010,
        10: 2020,
    }
    # 0 : Jan and 11 : Dec
    change_major_months = data.change_major_month.tolist()
    
    
    weekly_academic_work_hrs = data.weekly_work_hr.tolist()
    #0, Less than 10 hours ( < 1.4hr/day)
    #1, Between 10 - 15 hours (< 2.14 hr/day)
    #2, Between 15 - 20 hours (< 2.9hr/day)
    #3, Between 20 - 25 hours (< 3.5hr/day)
    #4, More than 25 hours ( > 3.5 hr/day)    
    
    
    weekly_research_work = data.wrk_outside_class.tolist()    
    # binary var: 1: yes, 0: No
    
    sleep_weekendnights_hrs = data.sleep_weekends.tolist()    
    sleep_weeknights_hrs = data.sleep_weeknights.tolist()
    #0, 5hr or less
    #1, 6 hr
    #2, 7 hr
    #3, 8 hr
    #4, 9 hr
    #5, 10 hr
    #6, 11 hr or more
    
    
    
    # Weekly work hours. Employment    
    # binary variables: 1: yes, 0: no
    less_2hr_work = data.employment_status___1.tolist()
    betw_2_5_hr_work = data.employment_status___2.tolist()
    betw_5_11_hr_work = data.employment_status___3.tolist()
    grt_11_hr_work = data.employment_status___4.tolist()
    betw_11_20_hr_work = data.employment_status___5.tolist()
    grt_20_hr_work = data.employment_status___6.tolist()
    do_not_work = data.employment_status___7.tolist()
    
    # these are dates!
    current_job_start_date = data.job.tolist()
    seeing_family_recent_date = data.saw_family.tolist()
    
    family_seeing_freq = data.saw_family_freq.tolist()
    #1, Most days
    #2, About once/week
    #3, About once/month
    #4, During school breaks only
    #5, Rarely or never while I am at college
    
    talk_to_family_freq = data.talk_family.tolist()
    #1, Most days
    #2, About once a week
    #3, About once a month
    #4, During school breaks
    #5, Rarely or never while I am at college
    
    trying_to_be_healthy = data.physical_act.tolist()
    #0, strongly disagree
    #1, disagree
    #2, agree
    #3, strongly agree

    
    eat_healthy_diet = data.eating.tolist()
    #0, strongly disagree
    #1, disagree
    #2, agree
    #3, strongly agree
    
    spiritual_wellbeing = data.spiritual.tolist()
    #0, strongly disagree
    #1, disagree
    #2, agree
    #3, strongly agree
    
    sleep_weeknights_hrs = data.prod_rel.tolist()
    #0, strongly disagree
    #1, disagree
    #4, agree
    #3, strongly agree
    
    enjoy_being_at_school = data.being_at_school.tolist()
    #0, strongly disagree
    #1, disagree
    #4, agree
    #3, strongly agree
    
    overwhelmed_at_school = data.overwhelmed.tolist()
    #0, strongly disagree
    #1, disagree
    #2, agree
    #3, strongly agree
    
    
    ############## Health questions Matrix ##################
    #1, Yes
    #0, No
    smoke = data.cigarettes.tolist()
    rec_drugs = data.rec_drugs.tolist()
    #########################################################
    
    # PHQ9
    phq_scores = []
    phq_final_get_along_with_people = []
    suicide_ideation = []

    phq9_1_index = data.columns.get_loc("phq9_1")
    phq9_final_index = data.columns.get_loc("phq9_final")
    
    
    
    #suicide ideation timeline
    #1, Less than a month ago
    #2, Within the last 3 months
    #3, Within the last 6 months
    #4, More than 6 months ago
    #5, Not applicable
    si_less_month_ago = data.si_timeline___1.tolist()
    si_within_3_months = data.si_timeline___2.tolist()
    si_within_6_months = data.si_timeline___3.tolist()
    si_grt_6_months_ago = data.si_timeline___4.tolist()
    si_not_application = data.si_timeline___5.tolist()
    
    # anxiety/GAD-7    
    gad7_start_index = data.columns.get_loc('feeling_nervous_anxious_or')
    gad7_end_index = data.columns.get_loc('feeling_afraid_as_if_somet')
    anxiety_scores = []


    # Rosenburgh self-esteem score
    self_esteem_scores = []
    
    # binary, 1: yes, 0: no
    someone_to_talk_to = data.someone_to_talk_to.tolist()
    emergency_living_place = data.emergency_living.tolist()
    money_for_needs = data.money_for_needs.tolist()
    eat_less = data.eat_less.tolist()
    borrow_money = data.borrow_money.tolist()
    lose_housing = data.lose_housing.tolist()
    divorce = data.divorce.tolist()

    # string
    divorce_time = data.dovirce_time.tolist()
    
    death_close_family = data.ds_fam.tolist()
    death_close_family_time = data.ds_fam_time.tolist()
    
    death_close_friend = data.ds_frnd.tolist()
    death_close_friend_time = data.ds_frnd_time.tolist()

    argument_with_family = data.arg_fam.tolist()
    argument_with_family_time = data.arg_fam_time.tolist()

    conflict_with_friend = data.con_frnd.tolist()
    conflict_with_friend_time = data.con_frnd_time.tolist()

    conflict_with_student = data.con_std.tolist()
    conflict_with_student_time = data.con_std_time.tolist()
    
    conflict_with_faculty = data.con_fac.tolist()
    conflict_with_faculty_time = data.con_fac_time.tolist()
    
    conflict_with_roommate = data.con_room.tolist()
    conflict_with_roommate_time = data.con_room_time.tolist()

    family_health_change = data.family_health.tolist()
    family_health_time = data.family_health_time.tolist()

    change_in_personal_health = data.personal_health.tolist()
    change_in_personal_health_time = data.personal_health_time.tolist()
    
    started_dating_time = data.dating_time.tolist()
    any_breakup = data.breakup.tolist()
    breakup_date = data.breakup_time.tolist()

    dropped_class = data.dropping.tolist()
    dropped_class_time = data.dropping_time.tolist()
    
    received_c_grade = data.low_grade.tolist()
    received_c_grade_time = data.low_grade_time.tolist()

    on_probation = data.probation.tolist()
    on_probation_time = data.probation_time.tolist()
    
    member_of_sports = data.sport.tolist()
    member_of_sports_time = data.sports_act_time.tolist()

    member_of_oncampus_clubs = data.clubs.tolist()
    member_of_oncampus_clubs_time = data.clubs_act_time.tolist()

    member_of_performing_arts = data.arts.tolist()
    member_of_performing_arts_time = data.arts_act_time.tolist()

    member_of_academic_clubs = data.academic_clubs.tolist()
    member_of_academic_clubs_time = data.academic_clubs_time.tolist()

    member_of_religious_club = data.religious.tolist()
    member_of_religious_club_time = data.religious_time.tolist()
    
    participate_in_social_good = data.social_good.tolist()
    participate_in_social_good_time = data.social_good_time.tolist()
    
    laid_off = data.laid_off.tolist()
    laid_off_time = data.fired_frm_work.tolist()

    
    
    for row in data.iterrows():
        id = row[1].ph_id2_2bf
        print('PHID:===>',id)
        record_ids.append(row[1].ph_id2_2bf)
        tstr = row[1].promotehealth_timestamp
        
        if tstr != '[not completed]':
            t_obj = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
            time_stamps.append(t_obj)
        
        else:
            time_stamps.append(None)
        
        
        ages.append(row[1].age)
        months.append(row[1].months)
        
        if row[1].gender != 1 and row[1].gender != 2:
            gender.append(3)
        else:
            gender.append(row[1].gender)
        
            
        nationality.append(row[1].nationality)
        #print(id, '--->',row[1].race___1)
        
        
        if row[1].race___1 == 1 or row[1].race___2 == 1 or row[1].race___4 == 1 or row[1].race___6 == 1:
            race.append(3)
        
        elif row[1].race___5 == 1:
            race.append(1)
        
        else:# row[1].race___3 == 1:
            race.append(2)

        permanent_home.append(row[1].perm_home)
        
        first_gen.append(row[1].first_gen)
        
        if row[1].sig_src___0 == 1:
            financial_support_from_parents.append(1)
        else:
            financial_support_from_parents.append(0)

        if row[1].sig_src___1 == 1:
            financial_support_from_loans.append(1)
        else:
            financial_support_from_loans.append(0)
        
        
        if row[1].sig_src___2 == 1:
            financial_support_from_self.append(1)
        else:
            financial_support_from_self.append(0)        
        
        if row[1].year_college___1 == 1:
            college_year.append(1)

        elif row[1].year_college___2 == 1:
            college_year.append(2)
        
        elif row[1].year_college___3 == 1:
            college_year.append(3)

        elif row[1].year_college___4 == 1:
            college_year.append(4)


        elif row[1].year_college___5 == 1:
            college_year.append(5)


        elif row[1].year_college___6 == 1:
            college_year.append(6)

        elif row[1].year_college___7 == 1:
            college_year.append(7)
        # if missing, then put it to other group with 7
        else:
            college_year.append(7)
        
        
        
        ####################### compute PHQ9 ##############################
        score, phq_final, suicide = compute_phq9_score(row, phq9_1_index, phq9_final_index)
        phq_scores.append(score)
        phq_final_get_along_with_people.append(phq_final)
        suicide_ideation.append(suicide)
        ###################################################################
        
        ###################### compute anxiety score ######################
        anxiety_score = compute_gad_7(row, gad7_start_index,gad7_end_index)
        #5-9 mild anxiety
        #10-14 moderate anxiety (1)
        #15-21 severe anxiety         
        anxiety_scores.append(anxiety_score)
        ###################################################################

        ###################### rosenburgh self-esteem score ####################
        ros_score = compute_selfesteem(row)
        self_esteem_scores.append(ros_score)
        


    #print(phq_scores, len(phq_scores))
    #
    #print(anxiety_scores, len(anxiety_scores))
    #print(self_esteem_scores, len(self_esteem_scores))
    #
    #print(suicide_ideation, len(suicide_ideation))


    #'',len(),'\n'
    print('============================')
    #print(
    #    'ids',len(record_ids),'\n'
    #    'tstamps',len(time_stamps),'\n'
    #    'ages',len(ages),'\n'
    #    'months',len(months),'\n'
    #    'gender',len(gender),'\n'
    #    'nationality', len(nationality), '\n'
    #    'race',len(race),'\n'
    #    'permanent_home', len(permanent_home), '\n'
    #    'first_gen', len(first_gen), '\n'
    #    'financial_support_from_parents', len(financial_support_from_parents), '\n'
    #    'financial_support_from_loans', len(financial_support_from_loans), '\n'
    #    'financial_support_from_self', len(financial_support_from_self), '\n'
    #    'living_dorm_single', len(living_dorm_single), '\n'
    #    'living_greek_shared', len(living_greek_shared), '\n'
    #    'living_off_campus_shared', len(living_off_campus_shared), '\n'
    #    'college_year', len(college_year), '\n'
    #    'majors', len(majors), '\n'
    #    'change_major', len(change_major), '\n'
    #    'change_major_year', len(change_major_year), '\n'
    #    'change_major_months', len(change_major_months), '\n'
    #    'weekly_research_work', len(weekly_research_work), '\n'\
    #    'self_esteem_scores',len(self_esteem_scores), '\n'
    #)
    #    
        
    header = [
        'record_ids', 
        'time_stamps', 
        'ages', 
        'months', 
        'gender', 
        'nationality', 
        'race', 
        'permanent_home', 
        'first_gen', 
        'financial_support_from_parents', 
        'financial_support_from_loans', 
        'financial_support_from_self', 
        'living_w_parents', 
        'living_dorm_single', 
        'living_dorm_shared', 
        'living_greek_single', 
        'living_greek_shared', 
        'living_off_campus_single', 
        'living_off_campus_shared', 
        'college_year', 
        'majors', 
        'gpa_current', 
        'gpa_last_sem_end', 
        'gpa_last_sem_start', 
        'change_major', 
        'change_major_year', 
        'change_major_months', 
        'weekly_academic_work_hrs', 
        'weekly_research_work', 
        'sleep_weekendnights_hrs', 
        'sleep_weeknights_hrs', 
        'less_2hr_work', 
        'betw_2_5_hr_work', 
        'betw_5_11_hr_work', 
        'grt_11_hr_work', 
        'betw_11_20_hr_work', 
        'grt_20_hr_work', 
        'do_not_work', 
        'current_job_start_date', 
        'seeing_family_recent_date', 
        'family_seeing_freq', 
        'talk_to_family_freq', 
        'trying_to_be_healthy', 
        'eat_healthy_diet', 
        'spiritual_wellbeing', 
        'sleep_weeknights_hrs', 
        'enjoy_being_at_school', 
        'overwhelmed_at_school', 
        'smoke', 
        'rec_drugs', 
        'phq_scores', 
        'phq_final_get_along_with_people', 
        'suicide_ideation', 
        'si_less_month_ago', 
        'si_within_3_months', 
        'si_within_6_months', 
        'si_grt_6_months_ago', 
        'si_not_application', 
        'anxiety_scores', 
        'self_esteem_scores', 
        'someone_to_talk_to', 
        'emergency_living_place', 
        'money_for_needs', 
        'eat_less', 
        'borrow_money', 
        'lose_housing', 
        'divorce', 
        'divorce_time', 
        'death_close_family', 
        'death_close_family_time', 
        'death_close_friend', 
        'death_close_friend_time', 
        'argument_with_family', 
        'argument_with_family_time', 
        'conflict_with_friend', 
        'conflict_with_friend_time', 
        'conflict_with_student', 
        'conflict_with_student_time', 
        'conflict_with_faculty', 
        'conflict_with_faculty_time', 
        'conflict_with_roommate', 
        'conflict_with_roommate_time', 
        'family_health_change', 
        'family_health_time', 
        'change_in_personal_health', 
        'change_in_personal_health_time', 
        'started_dating_time', 
        'any_breakup', 
        'breakup_date', 
        'dropped_class', 
        'dropped_class_time', 
        'received_c_grade', 
        'received_c_grade_time', 
        'on_probation', 
        'on_probation_time', 
        'member_of_sports', 
        'member_of_sports_time', 
        'member_of_oncampus_clubs', 
        'member_of_oncampus_clubs_time', 
        'member_of_performing_arts', 
        'member_of_performing_arts_time', 
        'member_of_academic_clubs', 
        'member_of_academic_clubs_time', 
        'member_of_religious_club', 
        'member_of_religious_club_time', 
        'participate_in_social_good', 
        'participate_in_social_good_time', 
        'laid_off', 
        'laid_off_time'
    ]
    
    data_dict = {}
    #header = ['record_ids','time_stamps','ages','months','gender','nationality','race','permanent_home','first_gen','financial_support_from_parents','financial_support_from_loans','financial_support_from_self','living_w_parents','living_dorm_single','living_dorm_shared','living_greek_single','living_greek_shared','living_off_campus_single','living_off_campus_shared','college_year','majors','gpa_current','gpa_last_sem_end','gpa_last_sem_start','change_major','change_major_year','change_major_months','weekly_academic_work_hrs    ','weekly_research_work    ','sleep_weekendnights_hrs    ','sleep_weeknights_hrs','less_2hr_work','betw_2_5_hr_work','betw_5_11_hr_work','grt_11_hr_work','betw_11_20_hr_work','grt_20_hr_work','do_not_work','current_job_start_date','seeing_family_recent_date','family_seeing_freq','talk_to_family_freq','trying_to_be_healthy','eat_healthy_diet    ','spiritual_wellbeing','sleep_weeknights_hrs','enjoy_being_at_school','overwhelmed_at_school','smoke','rec_drugs','phq_scores','phq_final_get_along_with_people','suicide_ideation','si_less_month_ago','si_within_3_months','si_within_6_months','si_grt_6_months_ago','si_not_application','anxiety_scores','self_esteem_scores','someone_to_talk_to','emergency_living_place','money_for_needs','eat_less','borrow_money','lose_housing','divorce','divorce_time','death_close_family','death_close_family_time','death_close_friend','death_close_friend_time','argument_with_family','argument_with_family_time','conflict_with_friend','conflict_with_friend_time','conflict_with_student','conflict_with_student_time','conflict_with_faculty','conflict_with_faculty_time','conflict_with_roommate','conflict_with_roommate_time','family_health_change','family_health_time','change_in_personal_health','change_in_personal_health_time ','started_dating_time','any_breakup','breakup_date','dropped_class','dropped_class_time','received_c_grade','received_c_grade_time','on_probation','on_probation_time','member_of_sports','member_of_sports_time','member_of_oncampus_clubs','member_of_oncampus_clubs_time','member_of_performing_arts','member_of_performing_arts_time','member_of_academic_clubs','member_of_academic_clubs_time','member_of_religious_club','member_of_religious_club_time','participate_in_social_good','participate_in_social_good_time','laid_off','laid_off_time']
    # lst_of_lsts = [record_ids, time_stamps, ages, months, gender, nationality, race, permanent_home, first_gen, financial_support_from_parents, financial_support_from_loans, financial_support_from_self, living_w_parents , living_dorm_single , living_dorm_shared , living_greek_single , living_greek_shared , living_off_campus_single , living_off_campus_shared , college_year, majors , gpa_current , gpa_last_sem_end , gpa_last_sem_start , change_major , change_major_year , change_major_months , weekly_academic_work_hrs     , weekly_research_work     , sleep_weekendnights_hrs     , sleep_weeknights_hrs , less_2hr_work , betw_2_5_hr_work , betw_5_11_hr_work , grt_11_hr_work , betw_11_20_hr_work , grt_20_hr_work , do_not_work , current_job_start_date , seeing_family_recent_date , family_seeing_freq , talk_to_family_freq , trying_to_be_healthy , eat_healthy_diet     , spiritual_wellbeing , sleep_weeknights_hrs , enjoy_being_at_school , overwhelmed_at_school , smoke , rec_drugs , phq_scores, phq_final_get_along_with_people , suicide_ideation, si_less_month_ago , si_within_3_months , si_within_6_months , si_grt_6_months_ago , si_not_application , anxiety_scores, self_esteem_scores, someone_to_talk_to , emergency_living_place , money_for_needs , eat_less , borrow_money , lose_housing, divorce, divorce_time, death_close_family, death_close_family_time, death_close_friend, death_close_friend_time, argument_with_family, argument_with_family_time, conflict_with_friend, conflict_with_friend_time, conflict_with_student, conflict_with_student_time, conflict_with_faculty, conflict_with_faculty_time, conflict_with_roommate, conflict_with_roommate_time, family_health_change, family_health_time , change_in_personal_health , change_in_personal_health_time  , started_dating_time, any_breakup , breakup_date , dropped_class, dropped_class_time , received_c_grade, received_c_grade_time , on_probation , on_probation_time , member_of_sports , member_of_sports_time , member_of_oncampus_clubs , member_of_oncampus_clubs_time , member_of_performing_arts , member_of_performing_arts_time , member_of_academic_clubs, member_of_academic_clubs_time , member_of_religious_club, member_of_religious_club_time, participate_in_social_good , participate_in_social_good_time , laid_off , laid_off_time,feeling_during_2019_christmas,feeling_during_newyears,feeling_during_thanksgiving,corona_effects,corona_fear,current_credits,last_credits,spring_pressure ]
    # first round
    lst_of_lsts = [record_ids, time_stamps, ages, months, gender, nationality, race, permanent_home, first_gen, financial_support_from_parents, financial_support_from_loans, financial_support_from_self, living_w_parents , living_dorm_single , living_dorm_shared , living_greek_single , living_greek_shared , living_off_campus_single , living_off_campus_shared , college_year, majors , gpa_current , gpa_last_sem_end , gpa_last_sem_start , change_major , change_major_year , change_major_months , weekly_academic_work_hrs     , weekly_research_work     , sleep_weekendnights_hrs     , sleep_weeknights_hrs , less_2hr_work , betw_2_5_hr_work , betw_5_11_hr_work , grt_11_hr_work , betw_11_20_hr_work , grt_20_hr_work , do_not_work , current_job_start_date , seeing_family_recent_date , family_seeing_freq , talk_to_family_freq , trying_to_be_healthy , eat_healthy_diet     , spiritual_wellbeing , sleep_weeknights_hrs , enjoy_being_at_school , overwhelmed_at_school , smoke , rec_drugs , phq_scores, phq_final_get_along_with_people , suicide_ideation, si_less_month_ago , si_within_3_months , si_within_6_months , si_grt_6_months_ago , si_not_application , anxiety_scores, self_esteem_scores, someone_to_talk_to , emergency_living_place , money_for_needs , eat_less , borrow_money , lose_housing, divorce, divorce_time, death_close_family, death_close_family_time, death_close_friend, death_close_friend_time, argument_with_family, argument_with_family_time, conflict_with_friend, conflict_with_friend_time, conflict_with_student, conflict_with_student_time, conflict_with_faculty, conflict_with_faculty_time, conflict_with_roommate, conflict_with_roommate_time, family_health_change, family_health_time , change_in_personal_health , change_in_personal_health_time  , started_dating_time, any_breakup , breakup_date , dropped_class, dropped_class_time , received_c_grade, received_c_grade_time , on_probation , on_probation_time , member_of_sports , member_of_sports_time , member_of_oncampus_clubs , member_of_oncampus_clubs_time , member_of_performing_arts , member_of_performing_arts_time , member_of_academic_clubs, member_of_academic_clubs_time , member_of_religious_club, member_of_religious_club_time, participate_in_social_good , participate_in_social_good_time , laid_off , laid_off_time]
    for index, lst in enumerate(lst_of_lsts):
        data_dict[header[index]] = lst
    
    
    df = pd.DataFrame(data_dict)
    df.to_csv('../../data/campus-survey-data/processed_survey_data_mar_11.csv',index=False)
            
        
        
        
        
        
        
        
main()
