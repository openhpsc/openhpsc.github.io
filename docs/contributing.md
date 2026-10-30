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

## Where to participate

| What you want to do | Where to go |
| --- | --- |
| Introduce yourself, ask a question, or explore an idea | [Community Discussions](https://github.com/openhpsc/community/discussions) |
| Propose a scoped research task, requirement, or experiment | [Community issues](https://github.com/openhpsc/community/issues) |
| Follow research and development work | [R&D project](https://github.com/orgs/openhpsc/projects/2) |
| Correct a website page or report a documentation bug | [Documentation issues](https://github.com/openhpsc/openhpsc.github.io/issues) |
| Propose an edit to this manual | [Documentation pull requests](https://github.com/openhpsc/openhpsc.github.io/pulls) |

## Contribution workflow

1. Browse existing discussions and issues before opening a new one.
2. If the idea needs exploration, [start a discussion](https://github.com/openhpsc/community/discussions/new/choose).
3. When there is a concrete task, [open a community issue](https://github.com/openhpsc/community/issues/new).
   Describe the problem, scope, expected output, and acceptance criteria.
   Link the originating discussion and affected requirements, such as `OH-REQ-001`.
4. Link the issue to the relevant roadmap milestone. Maintainers can add it to
   the [R&D project](https://github.com/orgs/openhpsc/projects/2) and update its status as work progresses.
   Opening an issue does not automatically add it to the board.
5. Submit changes to the repository that owns the work, linking the issue and
   relevant source revisions, commands, and results. A small documentation
   correction can go directly to a pull request in this repository.
6. For documentation changes, run the strict build and site check in
   [Getting started](getting-started.md). Respond to review and keep changes focused.
7. Record the outcome and supporting evidence in the issue before closing it.
   Update the board when the work changes status.

Use issues for actionable work and Discussions for conversations. If a discussion
becomes a task, link them in both directions rather than copying the conversation.
The R&D project tracks issues; technical findings belong in linked research notes,
design decisions, or implementation repositories.

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

The [community repository](https://github.com/openhpsc/community) uses MIT for its original
content. This documentation repository keeps its existing licenses.

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
