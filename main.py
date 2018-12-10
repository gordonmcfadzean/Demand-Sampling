from data_assembler import InputFiles
from definitions import *
from scenario_creator import *
import numpy as np
import time

class__inputs = InputFiles('C:\\Users\\mcfadzeang\\Desktop\\Ideas\\ADMD Predictor\\CLNR data for sampling approach\\')

class__inputs.df__res1hh.dropna(axis=1,
                                thresh=41500,
                                inplace=True)  # drop any profiles which don't have at least 41,500 timestamps

hh = len(class__inputs.df__res1hh.index)  # count the number of timestamps

# print(class__inputs.df__res1hh.shape)

kept_columns = class__inputs.df__res1hh.columns.tolist()[:-1]  # make a list of the profiles which haven't been dropped

dm_kept_ID = class__inputs.df__dom_id[class__inputs.df__dom_id['ID'].isin(kept_columns[1:])]  # only keep the IDs for
# columns that haven't haven't been dropped

# this needs to be in a function >

for j in range(1, 46):  # iterate through 9 scenarios

    time_start = time.time()

    scenario = scenario_id_gen(scenario_selector(dict__scenarios, j), dm_kept_ID, draws_per_scenario)  # generate
    # ID draws for each scenario

    temp_list = []  # blank list

    for i in scenario.columns:  # iterate through each scenario column

        profiles_list = scenario[i].tolist()  # create a list of the sampled profiles for each scenario

        n_customers = len(profiles_list)  # count the number of profiles

        threshold = max([(1 - (n_customers+1)/20.0)])  # define the threshold for dropping timestamps

        half_hours = class__inputs.df__res1hh[['datetime', 'Period', 'Season']+profiles_list].copy()  # define a new
        # dataframe which only includes the time information, and the profiles for that scenario

        half_hours.dropna(axis=0, thresh=threshold, inplace=True)  # drop timestamps which don't meet the threshold

        for profile in profiles_list:  # iterate through every profile in the scenario
            half_hours[profile].fillna(half_hours.groupby(['Period', 'Season'])[profile].transform(np.mean))  # fill NA
            # with the mean of the same Period and Season

        half_hours['Total'] = half_hours.loc[:, profiles_list].sum(axis=1)  # sum the demand across all of the profiles
        # print(len(half_hours.index), len(half_hours.index)/hh, half_hours['Total'].max())

        temp_list.append(half_hours['Total'].max())  # add the maximum of the total profile to the temporary list

    time_end = time.time()

    duration = time_end - time_start

    print([j, duration] + temp_list)  # print the scenario number, and the list
