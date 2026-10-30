# Apply this documentation update

Copy the contents of this ZIP's `openhpsc.github.io` folder into your existing
repository checkout. Include hidden folders such as `.github`. Do not replace
or remove your checkout's `.git` directory.

Keep the new `docs/_templates/`, `docs/_static/`, `requirements.txt`, and
`docs/conf.py` together; these implement the appearance and browser-title fixes.

Review and publish:

```bash
git diff --stat
git add .
git commit -m "Improve documentation appearance and navigation"
git push
```

Check that GitHub Actions completes successfully, then refresh the website.
For appearance, use the visible Light, Dark, or System control.
