#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/10/20 10:11
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : t_gist.py
import requests


def upload_gists(auth: str, content: str = "No content") -> str:
    token = ("", auth)
    gists = requests.get("https://api.github.com/gists", auth=token).json()
    all_gists = {list(gist["files"].keys())[0]: gist["id"] for gist in gists}
    filename = "v_bank.json"
    payload = {
        "public": False,
        "description": "v_bank create",
        "files": {
            filename: {
                "type": "text/plain",
                "content": content,
            }
        },
    }
    if filename in all_gists:
        gist_url = "https://api.github.com/gists/" + all_gists[filename]
        file_response = requests.get(gist_url, auth=token).json()["files"][filename]
        old_content = file_response["content"]
        if old_content == content:
            return
        url = requests.patch(
            "https://api.github.com/gists/" + all_gists[filename],
            json=payload,
            auth=token,
        ).json()["id"]
    else:
        url = requests.post(
            "https://api.github.com/gists", json=payload, auth=token
        ).json()["id"]
        print("store in https://gist.github.com/" + url)
    return "https://gist.github.com/" + url


def download_gists(auth: str) -> str:
    token = ("", auth)
    gists = requests.get("https://api.github.com/gists", auth=token).json()
    all_gists = {list(gist["files"].keys())[0]: gist["id"] for gist in gists}
    filename = "v_bank.json"
    if filename not in all_gists:
        return ""
    gist_url = "https://api.github.com/gists/" + all_gists[filename]
    file_response = requests.get(gist_url, auth=token).json()["files"][filename]
    old_content = file_response["content"]
    return old_content


def main():
    auth = "..."
    upload_gists(auth)
    print(download_gists(auth))


if __name__ == "__main__":
    main()
