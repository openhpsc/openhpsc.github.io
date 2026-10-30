# Apply this documentation update

Copy the contents of this ZIP's `openhpsc.github.io` folder into your existing
repository checkout. Include hidden folders such as `.github`. Preserve your
checkout's `.git` directory and review local changes before replacing files.

This update connects the documentation to Community Discussions, community
issues, and the R&D project. The community roadmap holds milestone status;
website bug reports remain in this documentation repository. No GitHub settings,
issues, project items, or automation are created by copying these files.

Validate and publish:

```bash
. .venv/bin/activate
python -m sphinx -n -W --keep-going -b html docs _build/html
python scripts/check_site.py _build/html
git diff --stat
git add .
git commit -m "Connect documentation to community discussions and R&D tracking"
git push
```

Check that GitHub Actions completes successfully, then refresh the website.
The organization profile starter is updated too. To change the live organization
Overview, copy `org-profile/README.md` into `profile/README.md` in `openhpsc/.github`
and commit there separately.
