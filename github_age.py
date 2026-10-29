#!/usr/bin/env python3
"""查询 GitHub 用户的注册时间与账号年龄（公开 API，无需登录）。

用法：python3 github_age.py <username> [username ...]
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone


def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url, headers={"User-Agent": "github-age-checker"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def main(usernames):
    now = datetime.now(timezone.utc)
    for username in usernames:
        try:
            data = fetch_user(username)
        except Exception as exc:
            print(f"{username}: 查询失败：{exc}")
            continue
        created = datetime.fromisoformat(data["created_at"].replace("Z", "+00:00"))
        age_days = (now - created).days
        print(
            f"{data['login']}: 注册于 {created.date().isoformat()}，"
            f"已有 {age_days} 天，公开仓库 {data['public_repos']} 个"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python3 github_age.py <username> [username ...]")
        raise SystemExit(1)
    main(sys.argv[1:])
