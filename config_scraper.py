#!/usr/bin/python3
"""Includes the various lists and dictionaries need to configure your
personal OkCupid Scraper.

PLEASE KEEP THIS FILE SAFE AND GRANT ONLY YOUR SELF READ/WRITE PRIVLEDGES.
"""


# OkCupid Credentials
USERNAME = 'EdwardLucifitz'
PASSWORD = 'r2V-TZK-dX6-Dfc'

# ****************************************************************************
# ALL STRINGS BELOW THIS TEXT SHOULD MATCH OKCUPID'S SPELLING (INCLUDING CAPS)
# ****************************************************************************

# LOCATIONS where you'd like to find a match ()
locations = [
    'San Francisco', 'Berkeley', 'Oakland', 'Albany', 'Emeryville', 'Piedmont',
    'El Cerrito', 'Alameda',
]

# FLAGS ALL MATCHES AT OR ABOVE THE GIVEN %
percentage = 80

# Details
background_wanted = [
    'Atheist', 'Agnostic'
]

# Details Not Wanted (Just flags you that the word/s exist in the details
# section)
background_not_wanted = [
    'Christian', 'Catholic', 'Muslim', 'Buddhist', 'Hindu', 'Jewish', 'Sikh',
    'Other',
]

# Mics Details
misc_details_wanted = [

]

# Misc Details Not Wanted (Just flags you that the word/s exist in the misc
# details section)
misc_details_not_wanted = [
    'Vegan', 'Vegetarian',
]


# ****************************************************************************
# ************ ALL STRINGS BELOW THIS TEXT SHOULD BE LOWER CASE. *************
# ****************************************************************************

# SEARCHES ALL ESSAYS ---------------------------------------------------

# Flag 420 Friendly matches.
pot_mention = True

activities = [
    'watching netflix', 'telescope viewing', 'hiking', 'camping',
    'filmmaking', 'climbing', 'coding', 'hacking', 'playing pool',
    'playing billiards', 'playing guitar', 'playing songs', 'backpacking',
    'writing music', 'photography', 'taking photographs', 'photowalks',
    'rock climbing', 'gigging',
]

# Education - Place your schools here
education = [
    'uc berkeley', 'ucb'
]

# topics of interest to you
topics_interest = [
    'astronomy', 'guitar', 'python', 'linux',
    'black and white photography', 'black & white photography',
]

politics = [
    'democrat', 'liberal', 'independent', 'progressive',
]

# Searches for specific words you'd like to be in your
# match's essay sections.
adjectives = [
    'artsy', 'punctual', 'responsible', 'reliable', 'dependable',
    'learner', 'humble', 'low maintenance', 'environmentalist',
    'musician', 'pianist', 'hilarious',
]

# Absolutely Not - Matches that have these words in their essays will
# automatically be HIDDEN. Be careful with this one.
no_way = [

]


# FAVORITES SECTION -----------------------------------------------------------

authors = [
    'stephen king', "ender's game", "ender's shadow",

]

books = [
    'for dummies',
]

comedians = [
    'bill burr', 'chad daniels', 'george carlin', 'joe rogan',
    'jim gaffigan', 'lewis black',
]

food = [
    'pizza', 'steak', 'in n out', 'the habit'
]

movies = [
    'spirited away', 'big lebowski', 'carlitos way', 'goodfellas',
    'scarface', 'pulp fiction', 'kill bill', 'holy grail',
]

# This should just be musical artists.
music = [
    'fleetwood mac', 'bob dylan', 'the clash', 'the doors', 'supertramp',
    'john williams', 'grateful dead', 'herbie hancock', 'miles davis',
    'eric clapton', 'devo', 'thin lizzy', 'rush', 'al green', 'black sabbath',
    'bruce springsteen', 'funkadelic', 'black keys', 'the cars', 'the beatles',
    'bach', 'tom petty', 'heartbreakers', 'incredible bongo band', 'kinks',
    'allman brothers band', 'rolling stones', 'led zeppelin',
    'billy joel', 'beach boys', 'boston', 'loggins & messina',
    'tom waits', 'queen', 'cheap trick', 'doobie brothers',
    'ccr', 'creedence clearwater revival',
]

music_genres = [
    'blues'
    'classic rock',
    'rock',
]

news_mags = [
    'washington post',
    'new york times',
]

radio = [
    'npr'
]

television = [
    'x-files', 'westworld', 'stranger things', 'fraiser', 'dick van dyke show',
    'battlestar galactica', 'firefly', 'bill maher', 'real time',
    'john oliver', 'last week tonight', 'seth meyers', 'futurama',
    'west wing', 'game of thrones', 'law and order', 'the wire', 'monty python'
]

youtube = [

]
# --------------------------------------------------------------------


# SIX THINGS YOU COULD NEVER LIVE WITHOUT
your_six_things = [

]

# YOU SPEND A LOT OF TIME THINK ABOUT
your_thoughts = [
    'climate science', 'global warming',
]
