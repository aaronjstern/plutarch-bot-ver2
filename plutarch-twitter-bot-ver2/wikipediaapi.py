import wikipedia
from wikipedia.exceptions import DisambiguationError
import re


class ContestTextWikiApi:
     """ wikipedia_page_name: the full name of a wikipedia page with a table,
        contestants_list: a list of elements scrapped from a wikipedia table
        Intiates and populates self.contestants_dict, a dictionary with each element from contestants_list as the key and the 
        full name of the wikipedia article associated with each element as the value. 
        Decreases the possibility of a disambiguation error when using the wikipedia method summary to collect info on each
        element in contestants_list.
        """

    def __init__(self, wikipedia_page_name, contestants_list):
        self.contestants_list = contestants_list
        link_names = wikipedia.WikipediaPage(wikipedia_page_name).links
        print(link_names)
        self.contestants_dict = {}
        for contestants in self.contestants_list:
            for contestant in contestants:
                for link_name in link_names:
                    if contestant in link_name:
                        self.contestants_dict[contestant] = link_name
                    else:
                        if contestant.split(" ")[0] in link_name:
                            self.contestants_dict[contestant] = link_name

        self.full_contest_dict = {}

    def get_contest_dict(self):
        for contestants in self.contestants_list:
            for contestant in contestants:
                try:
                    summary = wikipedia.summary(self.contestants_dict[contestant], auto_suggest=False)
                    info = re.search(r'was(.*?)\.', summary).group(1)
                    if len(info) > 120:
                        info = info[:120] + '...'
                    life_dict = {contestant: info}
                    self.full_contest_dict.update(life_dict)
                    print(life_dict)
                except DisambiguationError as e:
                    print(f"{contestant} may refer to: ")
                    for i, option in enumerate(e.options):
                        print(i, option)
                    choice = int(input("Enter a choice: "))
                    assert choice in range(len(e.options))
                    summary = wikipedia.summary(e.options[choice])
                    info = re.search(r'was(.*?)\.', summary).group(1)
                    if len(info) > 120:
                        info = info[:120] + '...'
                    life_dict = {contestant: info}
                    self.full_contest_dict.update(life_dict)
















