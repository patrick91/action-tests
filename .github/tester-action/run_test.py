import json
import os
import pathlib
import re
import subprocess

import httpx

GITHUB_SHA = os.environ["GITHUB_SHA"]
GITHUB_EVENT_PATH = os.environ["GITHUB_EVENT_PATH"]
GITHUB_WORKSPACE = os.environ["GITHUB_WORKSPACE"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

print("running tests 🍓")

with open(GITHUB_EVENT_PATH) as f:
    event_data = json.load(f)

body = event_data["issue"]["body"]


print("asd")


def extract(markdown: str, filter_language: str = None):
    regex = r"```[a-z]*\n[\s\S]*?\n```"

    print(markdown)
    print("aaaaaaaaaaaaaaaaaaa", re.findall(regex, markdown, re.MULTILINE))

    for match in re.finditer(regex, markdown, re.MULTILINE):
        language = match.group(1)

        print(match)

        if filter_language and language != filter_language:
            continue

        yield match.group(2)


def get_comments_link(github_event_data: dict) -> str:
    return github_event_data["issue"]["comments_url"]


url = get_comments_link(event_data)

print("getting blocks")


for block in extract(body):
    print(block)

# test_path = pathlib.Path(GITHUB_WORKSPACE) / "test_issue.py"

# with open(test_path, "w") as f:
#     f.write(code)


# try:
#     output = subprocess.check_output(
#         ["pytest", "-vv", test_path], shell=True, cwd=GITHUB_WORKSPACE
#     )

# except subprocess.CalledProcessError as exc:
#     output = exc.output.decode()


# body = f"```{output}```"

# request = httpx.post(
#     url, headers={"Authorization": f"token {GITHUB_TOKEN}"}, json={"body": body}
# )

# if request.status_code >= 400:
#     print(request.status_code)
#     print(request.text)
