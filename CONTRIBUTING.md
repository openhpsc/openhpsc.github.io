<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Contributing to OpenHPSC

Help develop open, high-performance, fault-tolerant computing for space through
clear requirements, reusable implementations, and reproducible evidence.

Read `docs/contributing.md` for contribution areas and the workflow. Use the issue
templates for documentation improvements, requirements, and experiment proposals.
Discuss significant architecture or interface changes before implementation.

Run the documentation check before opening a pull request:

```bash
python -m sphinx -n -W --keep-going -b html docs _build/html
```

Link affected requirements or roadmap milestones. Distinguish proposed features
from measured results, preserve attribution, and include reproduction details.
