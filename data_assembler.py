from definitions import *


class InputFiles:

    """ A single class to store all of the input data
        """

    def __init__(self, s__folder):
        """ Initialise the class based on a folder containing all of the inputs

                Args:
                s__folder: a string showing the location of the folder

                Returns: all of the necessary values to be accessed by the class
                """

        self.s__folder = s__folder

        # all of the csvs are read into dataframes
        self.df__tc_defs = pd.read_csv(self.s__folder + 'CustomerTestCellDefinition.csv')
        self.df__res1hh = pd.read_csv(self.s__folder + 'tc1a_power_logica_sorted.csv')
        # self.df__res2hh = pd.read_csv(self.s__folder)
        # self.df__smehh = pd.read_csv(self.s__folder)
        # self.df__res1id = pd.read_csv(self.s__folder)
        # self.df__res2id = pd.read_csv(self.s__folder)
        # self.df__resmc = pd.read_csv(self.s__folder)
        # self.df__smemc = pd.read_csv(self.s__folder)

        self.df__res1hh['datetime'] = pd.to_datetime(
            self.df__res1hh['Unnamed: 0'],
            infer_datetime_format=True)  # ensure the date is formatted as a datetime, rather than a string

        self.df__res1hh['Time'] = pd.to_datetime(
            self.df__res1hh['datetime'],
            format='%H:%M').dt.time  # define a column of Times

        self.df__res1hh['Period'] = self.df__res1hh['Time'].map(period_dict)  # map periods 1-48 onto times

        self.df__res1hh['Season'] = self.df__res1hh['datetime']\
            .apply(lambda x: (x.month % 12 + 3) // 3)  # calculate the season

        # ----------------- #
        #    Profile IDs    #
        # ----------------- #

        # -- Domestic ID -- #

        # the IDs are reformatted first
        self.df__tc_defs = self.df__tc_defs[self.df__tc_defs['Test Cell ID'] == '1a']  # only select test cell 1a

        # add a new column "ID" in the same format as the half hourly profile headers
        self.df__tc_defs['ID'] = "TC" + self.df__tc_defs['Test Cell ID'] \
                                 + '_' + self.df__tc_defs['Location ID'].astype(str)
        self.df__dom_id = self.df__tc_defs[['ID', 'Mosaic Class']]  # a new dataframe containing ID and Mosaic Class
        self.df__dom_id = self.df__dom_id.dropna(inplace=False)  # drop rows with Mosaic class
        self.df__dom_id['Type'] = self.df__dom_id['Mosaic Class'].map(dict__dom_map)  # map on types from Mosaic Class
        self.df__dom_id = self.df__dom_id[['ID', 'Type']].copy()  # new dataframe with only ID and type
