import time
from cloudbot import hook


@hook.command
def piglatin(text):
    """piglatin - returns word in pig latin format"""
    word = text.lower()
    vowels = 'aeiou'

    pig = 'ay'

    first = word[0]

    if first in vowels:
        newword = word + pig
    else:
        newword = word[1:] + first + pig

    return "{} becomes {}".format(word, newword)


@hook.command
def palindrome(text):
    """palindrome - checks if textut is a palindrome"""
    string = text.lower()
    if string == string[::-1]:
        return "{} is a palindrome".format(string)
    else:
        return "{} is not a palindrome".format(string)


@hook.regex(r'\#(SWAG|swag|Swag)')
@hook.regex(r'\#(YOLO|yolo|Yolo)')
def refrainyoself(match, nick=None, message=None):
    if nick == "Mu5tank05" or "Mu5tank05-mc":
        return
    else:
        matchword = match.group().encode('utf-8')
        message("{} please refrain from saying {}".format(nick, matchword))


@hook.regex(r'\#(fourtwenty|420)')
def fourtwenty(match, nick=None, message=None):
    if nick == "Mu5tank05" or nick == "Sam" or nick == "Mu5tank05-mc":
        message("{} loves to blaze".format(nick))


@hook.command
def says(text, action=None, nick=None, conn=None, chan=None):
    """says - says (text) in current channel"""
    action("is saying something for " + nick)
    time.sleep(1)
    text = text.split(" ")
    if text[0][0] == "#":
        message = " ".join(text[1:])
        out = "PRIVMSG {} :{}".format(text[0], message)
    else:
        message = " ".join(text[0:])
        out = "PRIVMSG {} :{}".format(chan, message)
    conn.send(out)


@hook.regex(r'(?i)(Hello|Hi) (w|W)alter(!| |\\.|\?)*')
def helloregex(match, nick=None, message=None):
    if match.group(3) == "?":
        message("Hi {}, what's your question?".format(nick))
    else:
        message("Hello {}!".format(nick))

@hook.command
def poke(text, action=None):
    action("pokes " + text);