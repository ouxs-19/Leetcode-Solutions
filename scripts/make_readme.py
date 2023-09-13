from config import *
from functools import reduce
import requests
from bs4 import BeautifulSoup
import jinja2
import json
import sys
import markdownify
from os import path
import re

nested_get = lambda arr, obj: reduce(lambda dict, key: dict[key], arr, obj)

SCRIPT_ROOT = path.dirname(__file__)
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path.join(SCRIPT_ROOT, TEMPLATES_DIR)),
    trim_blocks=True,
    lstrip_blocks=True,
)


class Leetcode_Problem:
    def __init__(self, name):
        self.raw_name = name
        self.url = self.construct_url(name)
        self.set_info()
        self.desc_to_md()
        self.prepare_topics()

    def fetch_info(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, PARSER)
        res = soup.find_all("script", attrs=ATTRS)
        data = json.loads(res[0].contents[0])

        return data

    def set_info(self):
        data = self.fetch_info()

        self.name = nested_get(NAME_PATH, data)
        self.difficulty = nested_get(DIFFICULTY_PATH, data)
        self.acc = json.loads(nested_get(ACC_PATH, data))[ACC_KEY]
        self.description = nested_get(DESCRIPTION_PATH, data)
        self.topics = nested_get(TOPICS_PATH, data)

    def construct_url(self, url):
        name = re.sub('\s{2,}', ' ', re.sub('-{2,}', '', re.sub('[^a-z0-9- ]+', '',url.split(" ",1)[1].lower()))).replace(" ","-")
        return LEETCODE_URL + name

    def desc_to_md(self):
        self.description = markdownify.markdownify(
            self.description, heading_style=MD_STYLE
        )

    def prepare_topics(self):
        self.topics = [topic[TOPICS_KEY] for topic in self.topics]

    def get_attrs(self):
        return dict(
            challenge_name=self.name,
            challenge_link=self.url,
            challenge_difficulty=self.difficulty,
            challenge_topics=challenge.topics,
            challenge_acc=self.acc,
            challenge_description=self.description,
        )

    def add_to_counter(self):
        challenges_counter = self.load_challs_counter()

        for topic in self.topics:
            if topic not in challenges_counter:
                challenges_counter[topic] = [self.raw_name]
            else :
                if self.raw_name not in challenges_counter[topic] : 
                    challenges_counter[topic].append(self.raw_name)

        self.save_counter(challenges_counter)

    def load_challs_counter(self):
        with open(COUNTER_FILE, "r") as stream:
            try:
                return json.load(stream)
            except Exception as exc:
                print(exc)
                exit()

    def save_counter(self, data):
        with open(COUNTER_FILE, "w") as f:
            try:
                return json.dump(data, f,   indent=4)
            except Exception as exc:
                print(exc)
                exit()

def generate_README(JINJA_ENV, challenge, challenge_path):
    template = JINJA_ENV.get_template(README_TEMPLATE)
    content = template.render(challenge.get_attrs())
    file_path = path.join(challenge_path, README_PATH)
    with open(file_path, "w") as f:
        f.write(content)


if len(sys.argv) != 2:
    print("Usage: ./make_readme.py '1. challenge'")
    exit()

challenge_path = sys.argv[1]
challenge = Leetcode_Problem(challenge_path)
generate_README(JINJA_ENV, challenge, challenge_path)
challenge.add_to_counter()