<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Roadmap

OpenHPSC advances through reviewable milestones. The sequence is proposed;
calendar commitments will follow available contributors and resources.

## Milestones and exit criteria

| Milestone | Deliverable | Exit criterion |
| --- | --- | --- |
| **M0 · Shared foundation** | Mission, documentation, draft requirements, contribution process | Site builds cleanly; scope and a first experiment can be reviewed |
| **M1 · Baseline selection** | Candidate comparison and an architecture decision | A pinned configuration runs the chosen workload in simulation |
| **M2 · Resilience experiment** | Defined fault model and baseline/protected comparison | Replayable records and documented outcome analysis |
| **M3 · FPGA reference** | One board implementation and bring-up instructions | Functional run, timing status, utilization, and independent reproduction |
| **M4 · RTEMS integration** | Minimum BSP and a control-oriented application | Startup, clock, interrupts, console, and selected tests pass |
| **M5 · Mixed-criticality evaluation** | Application/control integration with workload measurements | Shared-resource behaviour and recovery limits are documented |
| **M6 · Radiation characterization** | Device-specific plan and physical test campaign | Methods, device conditions, results, and limits are published |
| **M7 · ASIC feasibility** | Process, IP, test, packaging, and funding study | A reviewed case for implementation and verification exists |

Later milestones can change as earlier results reveal better directions. M7 is
an evaluation gate, not a commitment to fabricate silicon.

## Current status

**M0 is in progress.** This documentation release supplies the initial foundation;
community review and publication are the next steps. No milestone beyond M0 is
claimed complete by this release.

## Immediate contributions

- Review the [draft requirements](requirements.md) for missing or untestable obligations.
- Propose the workload and fault model for the [first demonstrator](demonstrator.md).
- Reproduce one candidate's upstream simulation and record the exact revision and environment.
- Review dependency licenses and identify missing public implementation artifacts.

## What will guide scope

A larger core count or accelerator is useful only when a workload and measurements
justify it. Early releases prioritize repeatability, observable behaviour, and a
clear path from requirements to tests. Performance ambitions remain part of the
project, with targets grounded in evidence as the platform matures.
