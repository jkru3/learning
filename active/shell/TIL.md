## 2025/05/12
how to remove DS_Store files tracked by git: `git ls-files -z | grep -z '.DS_Store' | xargs -0 git rm --cached`