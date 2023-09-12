LEETCODE_URL = "https://leetcode.com/problems/"

BASE_PATH = ["props", "pageProps", "dehydratedState", "queries"]
QUESTION_PATH = ["state", "data", "question"]

NAME_PATH = [*BASE_PATH, 0, *QUESTION_PATH, "title"]
DIFFICULTY_PATH = [*BASE_PATH, 0, *QUESTION_PATH, "difficulty"]
ACC_PATH = [*BASE_PATH, 7, *QUESTION_PATH, "stats"]
DESCRIPTION_PATH = [*BASE_PATH, 6, *QUESTION_PATH, "content"]
TOPICS_PATH = [*BASE_PATH, 8, *QUESTION_PATH, "topicTags"]

ACC_KEY = "acRate"
TOPICS_KEY = "name"

MD_STYLE = "ATX"
PARSER = "html.parser"
ATTRS = {"id": "__NEXT_DATA__"}

TEMPLATES_DIR = "templates"
README_TEMPLATE = "readme.j2"
README_PATH = "README.md"
