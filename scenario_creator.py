import pandas as pd


def scenario_id_draw_gen(dict__scenarios_var, df__dom_id_var, draw_var):
    """ Create a list of profile IDs for a specified scenario and draw number

        Args:
        dict__scenarios_var: a scenario dictionary, with different customer types as keys and the number of that type in
                             the scenario as values
        df__dom_id_var: a dataframe of all of the customer IDs, with their re-mapped types
        draw_var: the number of the current draw for this scenario

        Returns: a single dictionary entry, with the number of the draw as the key and a list of the profile IDs as the
                 value
        """

    # create an empty list
    temp_id_list = []

    # iterate through all of the columns (profile types) in the scenario
    for key in dict__scenarios_var:
            number = dict__scenarios_var[key]  # store the number of profiles of that type
            if number > 0:
                df__temp_id = df__dom_id_var[df__dom_id_var['Type'] == key]  # filter to only profile IDs of that type
                temp_id_list += df__temp_id.sample(number)['ID'].tolist()  # randomly sample the correct number of IDs
            else:
                pass
    return {"Draw %d" % draw_var: temp_id_list}  # save in a dictionary format


def scenario_id_gen(dict__scenarios_var, df__dom_id_var, n__draws_var):
    """ Create a dataframe of profile IDs for a specific scenario across multiple draws

        Args:
        dict__scenarios_var: a scenario dictionary, with different customer types as keys and the number of that type in
                             the scenario as values
        df__dom_id_var: a dataframe of all of the customer IDs, with their re-mapped types
        n__draws_var: the number of times to draw samples

        Returns: a dataframe of lists of IDs for each draw
        """
    
    dict__id_samples = {}  # create a blank dictionary
    for draw in range(n__draws_var):  # repeat for as many draws as are required

        #  run the scenario_id_gen function for this draw, and add the output to the dictionary
        dict__id_samples.update(scenario_id_draw_gen(dict__scenarios_var, df__dom_id_var, draw))
    df__id_samples = pd.DataFrame(dict__id_samples)  # convert the dictionary to a dataframe

    return df__id_samples


def scenario_selector(df__scenarios_var, n_scenario_var):
    """ Select the number of required profiles for a single scenario from the dataframe of scenarios

        Args:
        dict__scenarios_var: a dataframe of the number of profiles of each type in each scenario
        n_scenario_var: the number of scenario to look at, which selects a specific row

        Returns: a dictionary of numbers of IDs required by each profile type
        """

    # select a specific row from the dataframe (a single scenario) and then convert to a dictionary
    return df__scenarios_var.iloc[[n_scenario_var-1]].to_dict('records')[0]


def scenario_iterator(df__scenarios_var, df__dom_id_var, n__draws_var):
    """ Generate a dictionary of scenarios IDs, with scenario numbers as keys and dataframes of IDs across draws as
    values

            Args:
            df__scenarios_var: a dataframe of the number of profiles of each type in each scenario
            df__dom_id_var: a dataframe of all of the customer IDs, with their re-mapped types
            n__draws_var: the number of times to draw samples

            Returns: a dictionary, with scenario IDs as keys, with the value of the dictionary a dataframe of IDs across
                     each draws
            """

    dict__of_scenarios = {}  # create a blank dictionary
    for n_scenario in df__scenarios_var.index:  # iterate through all of the scenarios (rows)
        dict__scenario = scenario_selector(df__scenarios_var, n_scenario)  # for each scenario/row, select the scenario
        dict__scenario_samples = scenario_id_gen(dict__scenario, df__dom_id_var, n__draws_var)  # generate the IDs
        dict__scenario_ids = {"Scenario %d" % n_scenario: dict__scenario_samples}  # store this in a dictionary
        dict__of_scenarios.update(dict__scenario_ids)  # add this to the master dictionary
    return dict__of_scenarios
