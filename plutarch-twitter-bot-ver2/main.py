from tablescraper import TableScraper
from contesttext import ContestText
from tweetpollfunc import tweet_poll
from wikipediaapi import ContestTextWikiApi

CHROME_FILE_PATH = "./chromedriver"
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Parallel_Lives"
WIKIPEDIA_PAGE_NAME = "Parallel_Lives"

parallel_lives_table = TableScraper(WIKIPEDIA_URL, ('Greek', 'Life'), ('Roman', 'Life'))

print(parallel_lives_table.table_list)

parallel_lives_list = parallel_lives_table.table_list

parallel_lives_info = ContestTextWikiApi(WIKIPEDIA_PAGE_NAME, parallel_lives_list)
parallel_lives_info.get_contest_dict()
parallel_lives_dict = parallel_lives_info.full_contest_dict

tweet_poll(CHROME_FILE_PATH, parallel_lives_list, parallel_lives_dict)




























