import os

from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium import webdriver

import config_scraper
# from models import Person, initialize,

WARNING_MESSAGE_ON = False
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
    'activities': config_scraper.activities,
    'education': config_scraper.education,
    'topics_interest': config_scraper.topics_interest,
    'politics': config_scraper.politics,
    'adjectives': config_scraper.adjectives,
    'no_way': config_scraper.no_way,
    'authors': config_scraper.authors,
    'books': config_scraper.books,
    'comedians': config_scraper.comedians,
    'food': config_scraper.food,
    'directors': config_scraper.directors,
    'movies': config_scraper.movies,
    'music': config_scraper.music,
    'music_genres': config_scraper.music_genres,
    'news_mags': config_scraper.news_mags,
    'radio': config_scraper.radio,
    'television': config_scraper.television,
    'youtube': config_scraper.youtube,
    'your_six_things': config_scraper.your_six_things,
    'your_thoughts': config_scraper.your_thoughts,
    'general_words':
    config_scraper.general_words,
}

WARNING_MESSAGE = """
UPON FILLING OUT 'config_scraper.py' BE WARY THAT THIS FILE NOW CONTAINS
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
    emailElem.send_keys(config_scraper.USERNAME)
    passwordElem = browser.find_element_by_id('login_password')
    passwordElem.send_keys(config_scraper.PASSWORD)
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

    print('[+] Found {} Matches'.format(len(match_links)))
    return match_links


def get_profile_attrs(browser, link):
    try:
        browser.get(link)
    except WebDriverException:
        print("[-] WebDriver Error: 'url' not string")
    username = browser.find_element_by_xpath(ATTR_XPATH['username']).text

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
    print('\n')
    print('USERNAME: {}.'.format(attributes[0]))
    print('WEB ADDRESS: {}'.format(attributes[-1]))

    check_age(attributes[1], config_scraper.age_range)
    check_location(attributes[2], config_scraper.locations)
    check_percentage(attributes[3], config_scraper.percentage)
    check_basics(
        attributes[4],
        config_scraper.basics_wanted,
        config_scraper.basics_not_wanted,
    )
    check_background(
        attributes[5],
        config_scraper.background_wanted,
        config_scraper.background_not_wanted
    )
    check_misc_details(
        attributes[6],
        config_scraper.misc_details_wanted,
        config_scraper.misc_details_not_wanted
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


def check_basics(basics, basics_wanted, basics_not_wanted):
    basics = basics.split(', ')
    matched_wanted_basics = []
    matched_unwanted_basics = []
    for detail in basics:
        if detail.strip() in basics_wanted:
            matched_wanted_basics.append(detail)
        if detail.strip() in basics_not_wanted:
            matched_unwanted_basics.append(detail)

    if matched_wanted_basics:
        print('[+] Matched Wanted basics: {}'.format(', '.join(
            matched_wanted_basics)))
    if matched_unwanted_basics:
        print('    [-] Matched Unwanted basics: {}'.format(', '.join(
            matched_unwanted_basics)))


def check_background(bkground, bkground_wanted, bkground_not_wanted):
    bkground = bkground.split(', ')
    matched_wanted_bkground = []
    matched_unwanted_bkground = []
    for detail in bkground:
        if detail.strip() in bkground_wanted:
            matched_wanted_bkground.append(detail)
        if detail.strip() in bkground_not_wanted:
            matched_unwanted_bkground.append(detail)

    if matched_wanted_bkground:
        print('[+] Matched Wanted background: {}'.format(', '.join(
            matched_wanted_bkground)))
    if matched_unwanted_bkground:
        print('    [-] Matched Unwanted background: {}'.format(', '.join(
            matched_unwanted_bkground)))


def check_misc_details(misc_details, misc_details_wanted,
                       misc_details_not_wanted):
    misc_details = misc_details.split(', ')
    matched_wanted_misc_details = []
    matched_unwanted_misc_details = []
    for detail in misc_details:
        if detail.strip() in misc_details_wanted:
            matched_wanted_misc_details.append(detail)
        if detail.strip() in misc_details_not_wanted:
            matched_unwanted_misc_details.append(detail)

    if matched_wanted_misc_details:
        print('[+] Matched Wanted Misc Details: {}'.format(', '.join(
            matched_wanted_misc_details)))
    if matched_unwanted_misc_details:
        print('    [-] Matched Unwanted Misc Details: {}'.format(', '.join(
            matched_unwanted_misc_details)))


def check_essays(essays):
    print("\nChecking essays against 'config_scraper'...\n")
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

    counter = 0
    for link in match_links[:4]:
        if counter > 0:
            input('\n***** Press ENTER to search next match *****\n\n')
        attributes = get_profile_attrs(BROWSER, link)
        parse_profile_attrs(attributes)
        counter += 1
    
    # BROWSER.quit()
    print('\n[+] Closed Browser')
    print('<3'*17, '\n')


if __name__ == "__main__":
    clear()
    # initialize()
    main()
