from config import *
import requests
import jinja2
from os import path
from functools import reduce


nested_get = lambda arr, obj: reduce(lambda dict, key: dict[key], arr, obj)

SCRIPT_ROOT = path.dirname(__file__)

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path.join(SCRIPT_ROOT, TEMPLATES_DIR)),
    trim_blocks=True,
    lstrip_blocks=True,
)


from dataclasses import dataclass


@dataclass
class statCategory:
    current: int
    maximum: int
    image: str


def construct_img(cog, curr_sols, max_sols):
    ratio = round((curr_sols / max_sols) * 100)
    img_link = PROGRESS_BAR_LINK.format(ratio, CATEGORIES[cog]["color"])

    return img_link


def construct_stats(cog, data):
    curr_sols = nested_get(CATEGORIES[cog]["curr"], data)
    max_sols = nested_get(CATEGORIES[cog]["max"], data)
    img_url = construct_img(cog, curr_sols, max_sols)

    statCog = statCategory(curr_sols, max_sols, img_url)

    return statCog


if __name__ == "__main__":
    data = requests.get(API_URL).json()
    stats = {}

    for category in CATEGORIES:
        stats[category] = construct_stats(category, data)

    template = JINJA_ENV.get_template(MAIN_README_TEMPLATE)
    content = template.render(dict(stats=stats))

    with open(README_PATH, "w") as f:
        f.write(content)
