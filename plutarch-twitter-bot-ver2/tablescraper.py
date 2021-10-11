from bs4 import BeautifulSoup
import requests
import pandas


class TableScraper:

    def __init__(self, wikipedia_url, *column_names):
        """ wikpedia_url: a url for a wikipedia article with a table.
            *column_names: the names of the columns in the wikipedia table to be pulled out
            Enables access to the data from the given wikipedia table as a pandas dataframe and lists """
        result = requests.get(wikipedia_url)
        soup = BeautifulSoup(result.text, "lxml")
        self.table = soup.find('table', {'class': "wikitable"})
        df = pandas.read_html(str(self.table))
        self.data_records = pandas.DataFrame(df[0]).to_dict('records')
        self.columns = []
        for column_name in column_names:
            column = [self.data_records[i][column_name] for i in range(len(self.data_records))]
            self.columns.append(column)
        self.table_zip = list(zip(*self.columns))
        self.table_list = []
        for pair in self.table_zip:
            new_pair = [life.split(" or ")[0] for life in pair]
            self.table_list.append(new_pair)


















