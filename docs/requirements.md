<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Draft requirements

These requirements establish a reviewable starting point. They are **proposed**,
not validated capabilities. Numerical performance, power, and radiation targets
will follow workload selection and implementation studies.

## Initial requirements register

| ID | Proposed requirement | Verification evidence |
| --- | --- | --- |
| OH-REQ-001 | A released configuration shall identify all hardware/software source revisions and dependency licenses. | Manifest and license review |
| OH-REQ-002 | The baseline configuration shall build and run from documented instructions on a declared host environment. | Independent reproduction report |
| OH-REQ-003 | The demonstrator shall execute a fixed workload with a machine-readable pass/fail result. | Baseline functional test and expected outputs |
| OH-REQ-004 | Every protection mechanism shall identify the faults it detects or corrects and the resources outside its protection boundary. | Design review and targeted tests |
| OH-REQ-005 | A fault campaign shall record injection locations, timing, duration, multiplicity, and deterministic replay information. | Campaign configuration and raw records |
| OH-REQ-006 | Recovery shall specify the triggering condition, recovery action, preserved state, and measured interruption. | Recovery tests and timing results |
| OH-REQ-007 | An FPGA release shall identify the target device, tool version, constraints, timing status, and resource utilization. | Build and implementation reports |
| OH-REQ-008 | RTOS integration shall document startup, memory layout, interrupts, timer, console, and selected tests. | BSP documentation and execution logs |
| OH-REQ-009 | A performance claim shall specify workload, input, configuration, measurement method, and units. | Reproducible benchmark record |
| OH-REQ-010 | A radiation claim shall identify the tested device, implementation, test conditions, and applicable evidence. | Characterization report review |

## Requirements still to define

- The first representative control workload and its timing expectations.
- Memory capacities, protection granularity, and reporting interfaces.
- The supported instruction-set configuration and privilege mode.
- Boot behaviour, reset sequencing, and software-visible fault status.
- The intended environment for any future radiation-characterization campaign.

Do not infer a mission requirement from a commercial processor's headline
specification. Performance and reliability targets need an explicit use case.

## Traceability

For each accepted requirement, maintain links to its rationale, design decision,
implementation, test, and result. A Markdown table is sufficient initially; a
machine-readable register can follow when it reduces maintenance effort.

A result that covers only part of a requirement must identify the remaining gap.
An accepted requirement is not automatically an implemented or verified one.

## Proposing a requirement

[Open a community issue](https://github.com/openhpsc/community/issues/new). State the problem, proposed wording,
rationale, verification method, dependencies, and scope. Prefer a single
observable obligation over several unrelated obligations in one sentence.
Link any originating [discussion](https://github.com/openhpsc/community/discussions) and identify the
requirement being added or revised. The [R&D project](https://github.com/orgs/openhpsc/projects/2)
tracks follow-up work; the requirement text remains in this manual.
