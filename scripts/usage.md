# Dev quick start

```bash
rm -rf venv && virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
rm -v ../tf-modules-azure.md ; python gen_github_repo_md_list.py >  ../tf-modules-azure.md   
```
