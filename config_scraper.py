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

# AGE Range Perference (Must use integers)
# You may specify either value, both values, or neither.
greater_than_or_equal_to = 26
less_than_or_equal_to = None
age_range = [
    greater_than_or_equal_to,
    less_than_or_equal_to
]

# LOCATIONS where you'd like to find a match ()
locations = [
    'San Francisco, CA', 'Berkeley, CA', 'Oakland, CA', 'Albany, CA',
    'Emeryville, CA', 'Piedmont, CA', 'El Cerrito, CA', 'Alameda, CA',
]

# FLAGS ALL MATCHES AT OR ABOVE THE GIVEN %
percentage = 80

# Details
basics_wanted = [
    'Woman', 'Single', 'Thin', 'Fit', 'Jacked'
]

# Details Not Wanted
basics_not_wanted = [
    'Overweight', 'Trans Woman', 'Open relationship', 'Seeing Someone',

]

# Background
background_wanted = [
    'Atheist', 'Agnostic', 'Working on Post grad', 'Attended Post grad',
    'Attended University', 'Christian (and laughing about it)',
    'Catholic (and laughing about it)', 'Muslim (and laughing about it)',
    'Buddhist (and laughing about it)', 'Hindu (and laughing about it)',
    'Jewish (and laughing about it)', 'Sikh (and laughing about it)',
    'Other religion (and laughing about it)',
    "Christian (but it's not important)", "Catholic (but it's not important)",
    "Muslim (but it's not important)", "Buddhist (but it's not important)",
    "Hindu (but it's not important)", "Jewish (but it's not important)",
    "Sikh (but it's not important)",
    "Other religion (but it's not important)", 'Attended Two-year college',
    'Attended Space camp', 'Atheist (and laughing about it)',
    'Agnostic (and laughing about it)', "Atheist (but it's not important)",
    "Agnostic (but it's not important)", 'Working on Space camp',
]

# Details Not Wanted (Just flags you that the word/s exist in the details
# section)
background_not_wanted = [
    'Christian', 'Catholic', 'Muslim', 'Buddhist', 'Hindu', 'Jewish', 'Sikh',
    'Other', 'Christian (and it’s important)', 'Catholic (and it’s important)',
    'Muslim (and it’s important)', 'Buddhist (and it’s important)',
    'Hindu (and it’s important)', 'Jewish (and it’s important)',
    'Sikh (and it’s important)',
    'Other religion (and it’s important)', 'Dropped out of University',
]


# Mics Details
misc_details_wanted = [
    'Has dogs', 'Has cats'
]

# Misc Details Not Wanted (Just flags you that the word/s exist in the misc
# details section)
misc_details_not_wanted = [
    'Vegan', 'Vegetarian', 'Has kids', 'Kosher', 'Halal',
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
    'rock climbing', 'gigging', 'ultimate frisbee',
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
    'musician', 'pianist', 'hilarious', 'engineer'
]

# Absolutely Not - Matches that have these words in their essays will
# automatically be HIDDEN. Be careful with this one.
no_way = [

]


# FAVORITES SECTION -----------------------------------------------------------

authors = [
    'stephen king',

]

books = [
    'for dummies', "ender's game", "ender's shadow",
]

comedians = [
    'bill burr', 'chad daniels', 'george carlin', 'joe rogan',
    'jim gaffigan', 'lewis black', 'mike birbiglia'
]

food = [
    'pizza', 'steak', 'in n out', 'the habit',
]

directors = [
    'hayao miyazaki', 'quentin tarantino', 'christopher nolan', 'ridley scott', 'martin scorsese', 'coen brothers', 
]

actors = [
    'bill murray', 
]
movies = [
    'spirited away', 'big lebowski', 'carlitos way', 'goodfellas',
    'scarface', 'pulp fiction', 'kill bill', 'holy grail',
    'my neighbor totoro', 'howls moving castle', 'lord of the rings',
    'shawshank redemption', 
]

# This should just be musical artists.
music = [
    'fleetwood mac', 'bob dylan', 'the clash', 'the doors', 'supertramp',
    'john williams', 'grateful dead', 'herbie hancock', 'miles davis',
    'eric clapton', 'devo', 'thin lizzy', 'rush', 'al green', 'black sabbath',
    'bruce springsteen', 'funkadelic', 'black keys', 'the cars', 'the beatles',
    'bach', 'tom petty', 'heartbreakers', 'incredible bongo band', 'kinks',
    'allman brothers band', 'rolling stones', 'led zeppelin', 'foghat',
    'billy joel', 'beach boys', 'boston', 'loggins & messina',
    'tom waits', 'queen', 'cheap trick', 'doobie brothers',
    'ccr', 'creedence clearwater revival', 'willie nelson', 'rjd2', 'u2',
    'david bowie', 'joni mitchell', 'dave brubeck', 'howard shore', 
    'danny elfman',

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
    'west wing', 'game of thrones', 'law and order', 'the wire', 'monty python', 'better call saul', 'sens8', 'the crown', 
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

doin_w_life = [
    'scientist',
]
