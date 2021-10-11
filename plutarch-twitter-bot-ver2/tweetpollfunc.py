from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def tweet_poll(chrome_fill_path, contestant_list, contestant_dict):
    """ chrome_file_path: file path to chromedriver
        wikipedia_url:  a url for a wikipedia article with a table
        contestant_lists: a list of elements scrapped from a wikipedia table
        contestant_dict: a dictionary with each element in contestant_list as key and a summary of the corresponding
        article for each contestant name as the value

        Tweets out a twitter poll using the dictionary for tweet inputs, pairing elements in the poll using the
        contestant list """
    driver = webdriver.Chrome(chrome_fill_path)
    driver.get("https://twitter.com/i/flow/login")
    sleep(5)

    username_input = driver.find_element_by_tag_name("input")
    username_input.send_keys("@pollingplutarch")
    username_input.send_keys(Keys.ENTER)
    sleep(2)

    password_input = driver.find_element_by_tag_name("input")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)
    sleep(2)

    for pair in contestant_list:
        poll_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[3]/div')
        poll_button.click()
        sleep(2)
        tweet_input = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        first_choice = driver.find_element_by_name("Choice1")
        second_choice = driver.find_element_by_name("Choice2")

        tweet_input.send_keys(f"{pair[0]}: {contestant_dict[pair[0]]}\nVS\n{pair[1]}: {contestant_dict[pair[1]]}")
        first_choice.send_keys(pair[0])
        second_choice.send_keys(pair[1])
        tweet_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        sleep(4)
