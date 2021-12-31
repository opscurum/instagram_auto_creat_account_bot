import string
import random


# Generating name functions
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["emelyano", "Farkhada", "ksyunechka", "ndaat", "chiiura", "dsuyrsa", "khure", "esano", "gsayreo", "eesao", "tesaci", "bsutrwa", "bhoiinaz", "choisz", "drsaeu", "esaoin", "tsaeec", "choina", "iresanuz", "choinaes", "roinuenc", "buesaye", "tresaci", "siyres", "bsaont", "foureac", "khyresa", "otvscko", "tredac", "csoiyra", "sounncau", "chooln", "yresab", "chousa", "jsrwayi", "hcsaiu", "chious"]

    surName = ["vakhadi996","fanaseva889", "kalashnikov8869", "rexbnoouf", "ewsaqn",
		"scbmoi", "sachoisa", "inxhiurea", "voinsan",
		"inhsutew", "ussaoima", "coiunz", "tresau",
		"fsatrea", "hdarea", "chresab", "bourenus",
		"hiyrea", "noinea", "ayres", "xsate",
		"sacou", "tzvbou", "ciurds", "ckoura",
		"hkona", "cbsaeon", "grwwav", "nvcoua",
		"scbnkou", "savhoi", "fuyesa", "ryinea",
		"foitea", "bonsai", "utesabi", "sfeckou"]
    return ''.join(random.choice(firstName) + ' '  + random.choice(surName))


# Generating a username
def username(size = 8, chars  = string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))


# Generating a Email
def generatingEmail() :
    return ''.join(username() + '@gmail.com')






