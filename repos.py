#!/usr/bin/env python3
"""列出 GitHub 用户的公开仓库（公开 API，无需登录）。

用法：python3 repos.py <username>
"""

import json
import sys
import urllib.request


def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    req = urllib.request.Request(url, headers={"User-Agent": "github-age-checker"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def main(username):
    try:
        repos = fetch_repos(username)
    except Exception as exc:  # noqa: BLE001 - 直接报告错误即可
        print(f"{username}: 查询失败：{exc}")
        return
    if not repos:
        print(f"{username}: 没有公开仓库")
        return
    for repo in repos:
        print(
            f"{repo['name']} | ★{repo['stargazers_count']} | "
            f"{repo['language'] or '-'} | {repo['description'] or ''}"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python3 repos.py <username>")
        raise SystemExit(1)
    main(sys.argv[1])
