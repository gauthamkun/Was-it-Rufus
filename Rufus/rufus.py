import git
from datetime import datetime, timedelta


def func(git_dir):
    repo = git.Repo(git_dir)
    print("active branch:", repo.active_branch)
    if repo.is_dirty():
        print("local changes: False")
    else:
        print("local changes: True")
    commit_head = repo.head.commit
    commit_date = commit_head.authored_datetime
    commit_time = datetime.now()
    time = commit_time.astimezone()
    time2 = time - timedelta(days=7)
    if commit_date.astimezone() > time2:
        print("recent commit: True")
    else:
        print("recent commit: False")
    if commit_head.author.name == "Rufus":
        print("blame Rufus: True")
    else:
        print("blame Rufus: False")


if __name__ == "__main__":
    git_dir = input('Enter local path:')
    func(git_dir)
