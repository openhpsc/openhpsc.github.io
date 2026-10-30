<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Documentation help

## Change appearance

Use **Light**, **Dark**, or **System** in the page header. The active option is
highlighted. System follows your device's appearance; Light and Dark stay fixed.
Your choice is saved in this browser and applies when you visit another page.

If styling appears stale after a deployment, reload the page with `Ctrl+Shift+R`
(on macOS, `Cmd+Shift+R`). Browser privacy settings that block local storage may
prevent the preference from being saved between visits.

## Search and navigation

Use the sidebar to move between sections. Click the project logo or **OpenHPSC**
in the navigation to return home. On narrow screens, use the sidebar button
beside the page header. The Contents panel links to headings within a page.

Select Search or press `Ctrl+K` (`Cmd+K` on macOS). Type a term and press Enter
for full results. To copy a command, use the copy button at the top right of its
code block; command flags remain part of the copied text.

## Pages deployment reports Not Found

If `actions/configure-pages` reports that the Pages site cannot be found:

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Rerun the failed workflow from the Actions tab.

The public organization-site repository should be named `openhpsc.github.io`.
Organization policy must also allow GitHub Actions and Pages for the repository.

## A change does not appear

Check that the edit was committed and pushed to `main`. Then confirm the latest
workflow's build and deployment jobs both succeeded. A successful local build
alone does not publish a change.

```bash
git status
git add .
git commit -m "Update documentation"
git push
```

If the workflow failed, read the first relevant error before rerunning it.

## A documentation build fails

Run the strict build locally using the pinned environment:

```bash
python -m pip install -r requirements.txt
python -m sphinx -E -a -n -W --keep-going -b html docs _build/html
```

Check missing pages in the navigation, broken internal references, or errors in
MyST directives. Do not suppress warnings globally to hide an unresolved problem.

## Browser tab title contains an old separator

This project supplies title overrides in `docs/_templates/layout.html` and
`docs/_templates/search.html`. Keep both files and the `templates_path` setting
in `docs/conf.py` when updating the repository. Rebuild and redeploy after changes.
