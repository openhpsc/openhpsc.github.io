<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# OpenHPSC Documentation

Open High-Performance Spaceflight Computing: an independent community initiative
working toward open-source, high-performance, fault-tolerant space computing.
The documentation connects architecture, real-time software, and reproducible verification.

**Status:** definition phase. This repository contains documentation, not a
released or qualified processor. It is not affiliated with NASA, JPL, Microchip,
or SiFive.

Built with **Sphinx + MyST Markdown + Sphinx Book Theme**. The manual-oriented
structure is inspired by the RTEMS Documentation Project; the text is original.

## First deployment

1. Create `openhpsc/openhpsc.github.io` as a public repository on GitHub.
2. Put this project's contents at its root. Include the hidden `.github` folder.
3. Commit and push to `main`.
4. In **Settings → Pages**, select **GitHub Actions** as the source.
5. Run or rerun **Build and deploy documentation** from the Actions tab.
6. After deployment succeeds, visit <https://openhpsc.github.io/>.

The workflow also validates documentation pull requests without deploying them.
GitHub Actions must be enabled for this repository and allowed by organization policy.

If you have an empty repository already, these commands publish the source:

```bash
git init -b main
git add .
git commit -m "Add initial OpenHPSC documentation"
git remote add origin https://github.com/openhpsc/openhpsc.github.io.git
git push -u origin main
```

If the remote already contains commits, clone it first and copy this starter's
files into that clone. Do not overwrite existing work or force-push.

## Local build

Use Python 3.12:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m sphinx -n -W --keep-going -b html docs _build/html
python -m http.server 8000 --directory _build/html
```

Open <http://localhost:8000>. Edit Markdown in `docs/` and rebuild.

## Repository guide

| Path | Purpose |
| --- | --- |
| `docs/index.md` | Home and navigation |
| `docs/conf.py` | Sphinx, theme, and repository configuration |
| `docs/_static/` | Original visual assets and shared CSS |
| `.github/workflows/pages.yml` | Pull-request checks and Pages deployment |
| `CONTRIBUTING.md` | Contribution workflow |
| `org-profile/README.md` | Optional organization profile starter |

## Optional organization profile

Create a separate public repository named `openhpsc/.github`. Copy
`org-profile/README.md` there as `profile/README.md`. GitHub displays it on the
organization's Overview page. This profile repository is separate from the
`.github/` directory holding this website's workflow.

## Licensing

- Original Markdown documentation: **CC BY 4.0**, see `LICENSE`.
- Original build configuration, CSS, workflow, and scripts: **MIT**, see `LICENSE-CODE`.
- Third-party tools and future imported IP retain their own licenses.

## Documentation release 0.2

This release uses the supplied OpenHPSC logo and expands the project foundation:
mission, draft requirements, reference architecture, first-demonstrator acceptance
criteria, verification methods, research priorities, governance, and a gated roadmap.
The supplied logo is excluded from the documentation/code licenses; see
`docs/_static/LOGO-NOTICE.txt`. No hardware results are fabricated or implied.
