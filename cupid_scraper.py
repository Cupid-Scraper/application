import os

from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium import webdriver

import my_config_scraper
# from models import Person, initialize,

WARNING_MESSAGE_ON = True
BROWSER = webdriver.Firefox()


ATTR_XPATH = {
    'username':
    '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[1]',
    'age':
    '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[1]',
    'location':
    '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[3]',
    'percentage':
    '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[5]/a',
    'basics':
    '//*[@id="react-profile-details"]/table[1]/tbody/tr/td[2]',
    'background':
    '//*[@id="react-profile-details"]/table[2]/tbody/tr/td[2]',
    'misc_details':
    '//*[@id="react-profile-details"]/table[3]/tbody/tr/td[2]',
    'looking_for':
    '//*[@id="react-profile-wiw"]/div[2]',
}

config_lists = {
    'activities': my_config_scraper.activities,
    'education': my_config_scraper.education,
    'topics_interest': my_config_scraper.topics_interest,
    'politics': my_config_scraper.politics,
    'adjectives': my_config_scraper.adjectives,
    'no_way': my_config_scraper.no_way,
    'authors': my_config_scraper.authors,
    'books': my_config_scraper.books,
    'comedians': my_config_scraper.comedians,
    'food': my_config_scraper.food,
    'directors': my_config_scraper.directors,
    'movies': my_config_scraper.movies,
    'music': my_config_scraper.music,
    'music_genres': my_config_scraper.music_genres,
    'news_mags': my_config_scraper.news_mags,
    'radio': my_config_scraper.radio,
    'television': my_config_scraper.television,
    'youtube': my_config_scraper.youtube,
    'your_six_things': my_config_scraper.your_six_things,
    'your_thoughts': my_config_scraper.your_thoughts,
    'general_words':
    my_config_scraper.general_words,
}

WARNING_MESSAGE = """
UPON FILLING OUT 'my_config_scraper.py' BE WARY THAT THIS FILE NOW CONTAINS
SENSITIVE INFORMATION ABOUT YOU, AND IT SHOULD BE PROTECTED.

PRECAUTIONS TO TAKE:
- DO NOT LEAVE YOUR COMPUTER OPEN & UNATTEDED (this should be forever & always)
- ALWAYS REQUIRE A LOGIN TO ACCESS YOUR COMPUTER (even for sleep mode)
- USE A UNIQUE & STRONG PASSWORD FOR YOUR COMPUTER (obviously right?)

TO TURN OFF THIS WARNING CHANGE 'WARNING_MESSAGE_ON' TO 'False' INSIDE
'cupid_scraper.py'
PRESS 'enter' TO CONTINUE
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def sign_in(browser):
    browser.get('https://www.okcupid.com/')
    print('[+] Opened browser to OkCupid.com')
    signInElem = browser.find_element_by_class_name(
        'splashIndividual-header-signin-splashButton')
    signInElem.click()
    print('[+] Filling in Sign In form')
    emailElem = browser.find_element_by_id('login_username')
    emailElem.send_keys(my_config_scraper.USERNAME)
    passwordElem = browser.find_element_by_id('login_password')
    passwordElem.send_keys(my_config_scraper.PASSWORD)
    signin_button = browser.find_element_by_id('sign_in_button')
    signin_button.submit()
    print('[+] Signed In')
    browser.get('https://www.okcupid.com/home')
    print('[+] Redirected to Homepage')


def grab_match_cards(browser):
    browser.get('https://www.okcupid.com/match')
    browser.set_page_load_timeout(5)
    print('[+] Grabbing Matches')
    return browser.find_elements_by_class_name(
        'match_card_wrapper')


def grab_match_links(match_cards):
    match_links = []
    for card in match_cards:
        link = card.find_element_by_class_name('name')
        link = link.get_attribute("href")
        match_links.append(link)

    # print('[+] Found {} Matches'.format(len(match_links)))
    # input('\nPress ENTER to begin Searching')
    return match_links


def get_profile_attrs(browser, link):
    try:
        browser.get(link)
    except WebDriverException:
        print("[-] WebDriver Error: 'url' not string")

    try:
        username = browser.find_element_by_xpath(ATTR_XPATH['username']).text
    except NoSuchElementException:
        print('Did not scrape HTML properly.')
        exit

    try:
        age = browser.find_element_by_xpath(ATTR_XPATH['age']).text
    except NoSuchElementException:
        print("[*] {} did not have Age".format(username))
        age = None

    try:
        location = browser.find_element_by_xpath(ATTR_XPATH['location']).text
    except NoSuchElementException:
        print('[*] {} did not have location.'.format(username))
        location = None

    percentage = browser.find_element_by_xpath(ATTR_XPATH['percentage']).text
    basics = browser.find_element_by_xpath(ATTR_XPATH['basics']).text
    background = browser.find_element_by_xpath(ATTR_XPATH['background']).text

    try:
        misc_details = browser.find_element_by_xpath(
            ATTR_XPATH['misc_details']).text
    except NoSuchElementException:
        print("[*] {} did not have Misc Details".format(username))
        misc_details = None

    looking_for = browser.find_element_by_xpath(ATTR_XPATH['looking_for']).text

    essay_titles = browser.find_elements_by_class_name(
        "essays2015-essay-title")
    essays = browser.find_elements_by_class_name("essays2015-essay-content")
    essay_list = zip(essay_titles, essays)

    return (username, age, location, percentage,
            basics, background, misc_details,
            looking_for, essay_list, link)


def parse_profile_attrs(attributes):
    print('\nUSERNAME: {}.'.format(attributes[0]))

    check_age(attributes[1], my_config_scraper.age_range)
    check_location(attributes[2], my_config_scraper.locations)
    check_percentage(attributes[3], my_config_scraper.percentage)
    check_profile_details(
        'Details',
        attributes[4],
        my_config_scraper.basics_wanted,
        my_config_scraper.basics_not_wanted,
    )
    check_profile_details(
        'Background',
        attributes[5],
        my_config_scraper.background_wanted,
        my_config_scraper.background_not_wanted
    )
    check_profile_details(
        'Misc Details',
        attributes[6],
        my_config_scraper.misc_details_wanted,
        my_config_scraper.misc_details_not_wanted
    )
    check_essays(
        attributes[8]
    )


def check_age(age, age_range):
    low, high = age_range
    if not low:
        low = float("inf")
    if not high:
        high = float("inf")
    if int(age) >= low and int(age) <= high:
        print('[+] Matched Age Range: {}'.format(age))


def check_location(location, location_list):
    if location.strip() in location_list:
        print('[+] Matched City: {}'.format(location))


def check_percentage(match_percentage, pref_percent):
    match_percentage = match_percentage.split('%')
    if int(match_percentage[0]) >= pref_percent:
        print(
            "[+] Matched Percentage Range: {}%".format(
                match_percentage[0]))
    else:
        print('    [-] Did Not Match Percentage Range: {}%'.format(
            match_percentage[0]))


def check_profile_details(section_name, section, wanted_list, not_wanted_list):
    section = section.split(', ')
    matched_wanted_list = []
    matched_unwanted_list = []
    for detail in section:
        if detail.strip() in wanted_list:
            matched_wanted_list.append(detail)
        if detail.strip() in not_wanted_list:
            matched_unwanted_list.append(detail)

    if matched_wanted_list:
        print('[+] Matched Wanted {}: {}'.format(section_name, ', '.join(
            matched_wanted_list)))
    if matched_unwanted_list:
        print('    [-] Matched Unwanted {}: {}'.format(section_name, ', '.join(
            matched_unwanted_list)))


def check_essays(essays):
    # ADD THREADING FOR LISTS
    print("\nChecking essays against 'my_config_scraper'...\n")
    for essay_name, essay_paragraph in essays:
        counter = 0
        for lst_name, values in config_lists.items():
            values_present = []
            for item in values:
                if item in essay_paragraph.text:
                    values_present.append(item)
                elif item.upper() in essay_paragraph.text:
                    values_present.append(item)
                elif item.title() in essay_paragraph.text:
                    values_present.append(item)
            if values_present:
                if counter == 0:
                    print('\n> > > {}'.format(essay_name.text))
                print('[+] Matched Items in {} list:'.format(
                                                lst_name.upper()))
                for value in values_present:
                    print('   {}'.format(value))
                counter += 1


def main():
    if WARNING_MESSAGE_ON is True:
        print(WARNING_MESSAGE)
        input()
        clear()
    print('<3'*5, 'CUPID SCRAPER', '<3'*5)
    if WARNING_MESSAGE_ON is False:
        print('[*] WARNING MESSAGE DISABLED')

    sign_in(BROWSER)
    match_cards = grab_match_cards(BROWSER)
    match_links = grab_match_links(match_cards)

    counter = 1
    for link in match_links[:4]:
        clear()
        print('<3'*7, 'CUPID SCRAPER', '<3'*7)
        attributes = get_profile_attrs(BROWSER, link)
        parse_profile_attrs(attributes)
        counter += 1
        if counter != 5:
            input('\n<3<3<3 Press ENTER to search next match <3<3<3 ')

    input('\n<3<3<3 Press ENTER to close browser <3<3<3 ')
    BROWSER.quit()
    print('<3'*21, '\n')


if __name__ == "__main__":
    clear()
    # initialize()
    main()
