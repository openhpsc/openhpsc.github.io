<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Contributing

Help turn a shared ambition into a system others can understand and reproduce.
OpenHPSC welcomes documentation, architecture reviews, hardware, software, and
experimental work. A small verified improvement is a valuable contribution.

## Choose a starting point

| Your background | A useful first contribution |
| --- | --- |
| Documentation or teaching | Improve an explanation, add a worked example, or clarify a reference |
| Digital design | Reproduce a candidate simulation and document configuration and results |
| Verification | Review a fault model, define outcome rules, or propose an assertion |
| Embedded software / RTEMS | Map a candidate subsystem's startup, interrupt, timer, and console needs |
| FPGA implementation | Evaluate resource requirements and identify a reproducible board flow |
| Radiation effects | Review the evidence ladder or propose device-specific characterization questions |
| Research | Compare approaches using primary sources and identify reproducibility gaps |

## Contribution workflow

1. Find an issue or propose a bounded problem in the
   [issue tracker](https://github.com/openhpsc/openhpsc.github.io/issues).
2. State the intended result and link affected requirements or roadmap milestones.
3. For a small correction, open a pull request directly. Discuss larger technical changes first.
4. Include the source revisions, commands, and results relevant to your change.
5. Run the strict documentation build in [Getting started](getting-started.md).
6. Respond to review and keep the change focused.

The repository includes templates for documentation issues, requirements,
experiments, and pull requests.

## Documentation expectations

Use clear language and define unfamiliar acronyms. Separate proposed features
from delivered capabilities. Prefer original papers, official manuals, source
repositories, and standards. Preserve attribution when adapting material.

Do not claim a partner, supported board, performance figure, or radiation result
without evidence. A planned test belongs in a proposal; a completed test belongs
with its configuration and results.

## Experimental contributions

Follow the [verification guide](verification.md). Include the question, baseline,
fault model, environment, raw records, analysis, and limitations. Explain what
a second contributor should observe and how to reproduce one selected trial.

If an experiment fails, report what you observed. A reproducible limitation can
be more useful than a success claim that cannot be checked.

## Licensing

Original documentation is CC BY 4.0; original build configuration and tooling
are MIT unless identified otherwise. Imported RTL and dependencies retain their
own licenses. The supplied project logo has a separate notice; do not assume
that documentation licensing grants rights to reuse branding.

Only contribute material you are authorized to publish under the applicable
terms. See [Licensing and acknowledgements](license.md).

## Community conduct

Be respectful, constructive, and specific. Critique designs and evidence rather
than people. Help others reproduce findings, acknowledge uncertainty, and keep
private information out of public discussions.
