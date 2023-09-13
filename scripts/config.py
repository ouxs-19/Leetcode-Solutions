# generate challenge readme

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

# Stats script

API_URL = "https://leetcode-api-faisalshohag.vercel.app/ouxs-19"

CATEGORIES = {
    "Easy": {"curr": ["easySolved"], "max": ["totalEasy"], "color": "00b8a3"},
    "Medium": {"curr": ["mediumSolved"], "max": ["totalMedium"], "color": "ffc01e"},
    "Hard": {"curr": ["hardSolved"], "max": ["totalHard"], "color": "ef4743"},
    "Total": {"curr": ["totalSolved"], "max": ["totalQuestions"], "color": "1c27a3"},
}

PROGRESS_BAR_LINK = "https://us-central1-progress-markdown.cloudfunctions.net/progress/{}?dangerColor={}"

MAIN_README_TEMPLATE = "main_readme.j2"
