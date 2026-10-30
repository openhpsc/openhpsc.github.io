<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Contributing to OpenHPSC

Help develop open, high-performance, fault-tolerant computing for space through
clear requirements, reusable implementations, and reproducible evidence.

Read [the contribution guide](docs/contributing.md) for contribution areas and the workflow.

- [Start a community discussion](https://github.com/openhpsc/community/discussions/new/choose) for questions and early ideas.
- [Open a community issue](https://github.com/openhpsc/community/issues/new) for research, requirements, or experiments.
- [Follow the R&D project](https://github.com/orgs/openhpsc/projects/2) for tracked work.
- [Report a documentation issue](https://github.com/openhpsc/openhpsc.github.io/issues/new/choose)
  for website content or build problems.

Discuss significant architecture or interface changes before implementation.

Run the documentation check before opening a pull request:

```bash
python -m sphinx -n -W --keep-going -b html docs _build/html
python scripts/check_site.py _build/html
```

Link affected requirements or roadmap milestones. Distinguish proposed features
from measured results, preserve attribution, and include reproduction details.
