<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Getting started

## What you can build today

This repository builds the OpenHPSC documentation. It does not yet contain
processor RTL, an FPGA bitstream, or an RTEMS BSP.

## Build locally

Use Python 3.12 and Git. On systems that package virtual-environment support
separately, install that support first.

```bash
git clone https://github.com/openhpsc/openhpsc.github.io.git
cd openhpsc.github.io
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m sphinx -n -W --keep-going -b html docs _build/html
```

The build treats documentation warnings as errors. Open the generated
`_build/html/index.html`, or serve the output locally:

```bash
python -m http.server 8000 --directory _build/html
```

Visit `http://localhost:8000`. Stop the server with `Ctrl+C`.

## Edit a page

Pages live in `docs/` and use MyST Markdown. Add a new page to a `toctree` in
`docs/index.md` so it appears in the navigation. Rebuild after changes.

Configuration is in `docs/conf.py`; shared styling is in
`docs/_static/custom.css`. The default theme supplies search, a page outline,
light/dark modes, and responsive navigation.

## Publish with GitHub Pages

1. Create a public repository named `openhpsc.github.io` under `openhpsc`.
2. Add the contents of this starter at the repository root, including `.github/`.
3. Use `main` as the default branch.
4. Open **Settings → Pages → Build and deployment → Source** and choose
   **GitHub Actions**.
5. Push to `main`, or run **Build and deploy documentation** from the Actions tab.

The included workflow checks pull requests and deploys successful builds from
`main`. The expected site address is `https://openhpsc.github.io/`.

## Useful checks

```bash
# Rebuild every page and fail on warnings.
python -m sphinx -E -a -n -W --keep-going -b html docs _build/html

# Optional: check external links. Network restrictions can cause false failures.
python -m sphinx -b linkcheck docs _build/linkcheck
```
