import pandas as pd
import datetime as dt

half_hour_list = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30",
                  "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30",
                  "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                  "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
                  "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30",
                  "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]

half_hour_list = [dt.datetime.strptime(time, '%H:%M').time() for time in half_hour_list]

period_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
               17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
               33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

period_dict = dict(zip(half_hour_list, period_list))

draws_per_scenario = 200

dict__dom_map = {'A Alpha Territory': 'Dom_1',
                 'B Professional Rewards': 'Dom_1',
                 'C Rural Solitude': 'Dom_1',
                 'D Small Town Diversity': 'Dom_1',
                 'E Active Retirement': 'Dom_1',
                 'F Suburban Mindsets': 'Dom_1',
                 'G Careers AND Kids': 'Dom_1',
                 'H NEW Homemakers': 'Dom_1',
                 'I Ex-Council Community': 'Dom_1',
                 'J Claimant Cultures': 'Dom_1',
                 'K UPPER FLOOR Living': 'Dom_1',
                 'L Elderly Needs': 'Dom_1',
                 'M Industrial Heritage': 'Dom_1',
                 'N Terraced Melting Pot': 'Dom_1',
                 'O Liberal Opinions': 'Dom_1'}

dict__scenarios = pd.DataFrame({"Scenario": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                                             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                                             41, 42, 43, 44, 45],
                                "Dom_1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                          25, 30, 35, 40, 45, 50, 60, 70, 80, 90,
                                          100, 120, 140, 160, 180, 200, 250, 300, 350, 400,
                                          500, 600, 700, 800, 1000]}).set_index('Scenario')
