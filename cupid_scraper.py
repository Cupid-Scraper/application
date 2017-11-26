import os

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

import config_scraper
from models import Person, initialize, ViewedPerson

WARNING_MESSAGE = True
BROWSER = webdriver.Firefox()


ATTR_XPATH = {
    'username': '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[1]',
    'age': '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[1]',
    'location': '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[3]',
    'percentage': '//*[@id="profile2015"]/div[1]/div/div[1]/div[2]/div[2]/span[5]/a',
    'details': '//*[@id="react-profile-details"]/table[1]/tbody/tr/td[2]',
    'background': '//*[@id="react-profile-details"]/table[2]/tbody/tr/td[2]',
    'misc_details': '//*[@id="react-profile-details"]/table[3]/tbody/tr/td[2]',
    'looking_for': '//*[@id="react-profile-wiw"]/div[2]',
    'self_summary': '//*[@id="react-profile-essays"]/div[1]/div[2]',
    'doin_w_life': '//*[@id="react-profile-essays"]/div[2]/div[2]',
    'good_at': '//*[@id="react-profile-essays"]/div[3]/div[2]',
    'favorites': '//*[@id="react-profile-essays"]/div[4]/div[2]',
}


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
        name = card.find_element_by_class_name('name')
        if not ViewedPerson.select().where(
                                ViewedPerson.name == name.text).exists():
            ViewedPerson.create_viewed_person(name.text)
            link = card.find_element_by_class_name('name')
            link = link.get_attribute("href")
            match_links.append(link)

    print('[+] Found {} Matches'.format(len(match_links)))
    return match_links


def get_profile_attrs(browser, link):
    browser.get(link)
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
    details = browser.find_element_by_xpath(ATTR_XPATH['details']).text
    background = browser.find_element_by_xpath(ATTR_XPATH['background']).text
    try:
        misc_details = browser.find_element_by_xpath(
            ATTR_XPATH['misc_details']).text
    except NoSuchElementException:
        print("[*] {} did not have Misc Details".format(username))
        misc_details = None
    looking_for = browser.find_element_by_xpath(ATTR_XPATH['looking_for']).text

    essays = browser.find_elements_by_id('react-profile-essays')
    all_essays = ''
    for essay in essays:
        all_essays += essay.text

    return (username, age, location, percentage,
            details, background, misc_details,
            looking_for, all_essays)


def check_keywords(attributes):
    print('\n', '\n'.join(attributes[0:4]))
    essays = attributes[-1]
    matched_keywords = []
    with open('keywords.txt') as k_file:
        for word in k_file.readlines():
            if word in essays or word.title() in essays or word.upper() in essays:
                matched_keywords.append(word)
    if not matched_keywords:
        print('[*] Did not find any matching keywords.')
    else:
        print('[+] Found Keyords:')
        print('\n'.join(matched_keywords))


def main():
    print('<3'*5, 'CUPID SCRAPER', '<3'*5)
    sign_in(BROWSER)
    match_cards = grab_match_cards(BROWSER)
    match_links = grab_match_links(match_cards)

    for link in match_links:
        attributes = get_profile_attrs(BROWSER, link)
        check_keywords(attributes)

    BROWSER.quit()
    print('\n[+] Closed Browser')
    print('<3'*17, '\n')


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    initialize()
    main()
