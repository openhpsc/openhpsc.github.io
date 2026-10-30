<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Roadmap

OpenHPSC advances through reviewable milestones. The
[community roadmap](https://github.com/openhpsc/community/blob/main/ROADMAP.md)
is the maintained milestone plan. The [R&D project](https://github.com/orgs/openhpsc/projects/2) tracks
individual work items and their progress. This page explains how to follow and
contribute to that work.

## Follow the work

1. Read the community roadmap for milestone scope and completion criteria.
2. Browse the R&D project for tracked issues and current work.
3. Open a linked issue to inspect its question, expected output, and evidence.
4. Use [Community Discussions](https://github.com/openhpsc/community/discussions) to explore an idea before it
   becomes a scoped task.

Milestone status is maintained in the community repository rather than duplicated
here. Project-board status describes task progress; a completed task supports a
milestone only when its stated acceptance criteria are met.

## Immediate contributions

- Review the [draft requirements](requirements.md) for missing or untestable obligations.
- Propose the workload and fault model for the [first demonstrator](demonstrator.md).
- Reproduce one candidate's upstream simulation and record the exact revision and environment.
- Review dependency licenses and identify missing public implementation artifacts.

[Open a community issue](https://github.com/openhpsc/community/issues/new) for one bounded contribution.
Include its expected output, completion criteria, and relevant roadmap milestone.
Maintainers can add it to the R&D project; automatic issue intake is not assumed.

## Longer-term direction

The proposed sequence begins with project definition, a reproducible functional
baseline, and one measured protection experiment. FPGA implementation, RTEMS
integration, mixed-criticality evaluation, and physical radiation characterization
can follow as evidence and resources allow. ASIC feasibility remains a separate
evaluation, with no commitment to fabricate silicon.

A larger core count or accelerator needs a workload and measurements to justify
it. Early work prioritizes repeatability, observable behaviour, and traceability
from requirements to tests. Calendar commitments depend on contributors and
resources. See the community roadmap for the current plan.
