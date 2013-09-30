from util import hook, http, web
import re
import random


base_url = "http://reddit.com/r/{}/.json"
imgur_re = re.compile(r'http://(?:i\.)?imgur\.com/(a/)?(\w+\b(?!/))\.?\w?')

album_api = "https://api.imgur.com/3/album/{}/images.json"


def is_valid(data):
    if data["domain"] in ["i.imgur.com", "imgur.com"]:
        return True
    else:
        return False


@hook.command
def imgur(inp):
    "imgur <subreddit> -- Gets the first page of imgur images from <subreddit> and returns a link to them."
    try:
        data = http.get_json(base_url.format(inp.strip()),
                             user_agent=http.ua_chrome)
    except Exception as e:
        return "Error: " + str(e)

    data = data["data"]["children"]
    random.shuffle(data)

    # filter list to only have 10 imgur links
    filtered_posts = [i["data"] for i in data if is_valid(i["data"])]

    if not filtered_posts:
        return "No images found."

    items = []

    headers = {
    "Authorization": "Client-ID b5d127e6941b07a"
    }

    # loop over the list of posts
    for post in filtered_posts:
        match = imgur_re.search(post["url"])
        if match.group(1) == 'a/':
            # post is an album
            url = album_api.format(match.group(2))
            images = http.get_json(url, headers=headers)["data"]

            # loop over the images in the gallery and add to the list
            for image in images:
                items.append(image["id"])

        elif match.group(2) is not None:
            # post is an image
            items.append(match.group(2))

    #post_data = {
    #    "ids": items,
    #    "title": "images from /r/{}/".format(inp)
    #}

    #album = http.get("https://api.imgur.com/3/album/",  post_data=post_data, get_method="post", headers=headers)
    #pprint(album)


    return web.isgd("http://imgur.com/" + ','.join(items))