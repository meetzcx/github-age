# github-age

查询 GitHub 用户的注册时间与账号年龄，使用公开 API，无需登录。

## 用法

```bash
python3 github_age.py <username> [username ...]
```

## 示例

```bash
python3 github_age.py meetzcx
```

输出该账号的注册日期、已有天数与公开仓库数量。

## repos.py

列出该用户的公开仓库（名称、收藏数、语言、简介），同样使用公开 API，无需登录。

```bash
python3 repos.py <username>
```
