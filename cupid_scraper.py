import os
from selenium import webdriver

from models import Person, initialize, ViewedPerson

BROWSER = webdriver.Firefox()
USERNAME = 'EdwardLucifitz'
PASSWORD = 'r2V-TZK-dX6-Dfc'


def sign_in(browser):
    browser.get('https://www.okcupid.com/')
    print('[+] Opened browser to OkCupid.com')
    signInElem = browser.find_element_by_class_name(
        'splashIndividual-header-signin-splashButton')
    signInElem.click()
    print('[+] Filling in Sign In form')
    emailElem = browser.find_element_by_id('login_username')
    emailElem.send_keys(USERNAME)
    passwordElem = browser.find_element_by_id('login_password')
    passwordElem.send_keys(PASSWORD)
    signin_button = browser.find_element_by_id('sign_in_button')
    signin_button.submit()
    print('[+] Signed In')


def navigate_to_matches(browser):
    browser.get('https://www.okcupid.com/home')
    print('[+] Redirected to homepage')
    browse_matches = browser.find_element_by_partial_link_text(
        'Browse more matches')
    browse_matches.click()
    print('[+] Clicked "Browse more matches"')


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
            link = card.find_element_by_class_name('name').get_attribute("href")
            match_links.append(link)

    print('[+] Found {} Matches'.format(len(match_links)))
    return match_links


def main():
    print('<3'*5, 'CUPID SCRAPER', '<3'*5)
    sign_in(BROWSER)
    navigate_to_matches(BROWSER)
    match_cards = grab_match_cards(BROWSER)
    match_links = grab_match_links(match_cards)
    # print(match_links)
    BROWSER.quit()
    print('[+] Closed Browser')
    print('<3'*17, '\n')

    # name = card.find_element_by_class_name('name')
    # age = card.find_element_by_class_name('age')
    # location = card.find_element_by_class_name('location')
    # print("Name: {} \nAge: {} \nCity: {}\n".format(
    #         name.text, age.text, location.text))
    # try:
    #     Person.create_person(
    #         name=name.text,
    #         age=int(age.text),
    #         location=str(location.text),
    #     )
    # except ValueError:
    #     pass


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    initialize()
    main()
