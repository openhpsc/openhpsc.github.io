<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Research priorities

OpenHPSC's research should reduce a concrete design uncertainty. The following
questions are proposed work items, not claims of novelty or completed research.

## Priority questions

| Question | Useful first output | Decision it informs |
| --- | --- | --- |
| Which control subsystem is feasible? | Comparison of pinned configurations, licenses, tools, and bring-up effort | Initial implementation choice |
| What does memory protection cover? | Baseline/ECC experiment with a declared error model | Code, scrubbing policy, and protection boundary |
| How does recovery affect control? | Workload outputs and interruption measurements during injected faults | Recovery policy and timing requirements |
| Can control and application workloads coexist? | Interference measurements under declared shared-resource conditions | Isolation and memory/interconnect design |
| How do simulated faults relate to physical observations? | Literature review and a device-specific test proposal | Radiation-characterization methodology |
| Which workloads justify vector acceleration? | Reproducible scalar baseline and memory analysis | Whether and when to integrate an accelerator |

## Candidate evaluation checklist

For every processor or subsystem, record:

1. Exact source revision and license inventory, including generated files and dependencies.
2. Instruction-set configuration, privilege support, timer, interrupts, and debug interfaces.
3. Working simulation flow and known supported FPGA targets.
4. Available verification, assertions, tests, and unresolved limitations.
5. Protection mechanisms, reporting behaviour, and documented recovery semantics.
6. Integration effort, tool requirements, and resource measurements where available.

A feature named in a paper may not be present in the public repository. Verify
availability at the chosen revision before promising it in OpenHPSC.

## Reading path

Start with [Carfield and its safety island](references.md), then compare a
smaller Ibex-based route. Use HARV as a research reference for fault mitigation
and Trikarenos as a reference for connecting fault injection to measurements on
fabricated silicon. Explore Cheshire/CVA6 and Ara as the application-processing
and acceleration scope becomes concrete.

## Proposing a study

Explore an early idea in [Community Discussions](https://github.com/openhpsc/community/discussions). For a scoped
study, [open a community issue](https://github.com/openhpsc/community/issues/new) and define an answerable
question, baseline, method, expected artifacts, and acceptance criteria.
Link relevant requirements and the originating discussion. Maintainers can add
accepted work to the [R&D project](https://github.com/orgs/openhpsc/projects/2). Record reproducible findings
in the [community research directory](https://github.com/openhpsc/community/tree/main/research),
linking the issue and any implementation artifacts. Include limitations. State what can be done with existing
hardware and which parts require external facilities or funding.

Research contributions should retain negative findings and reproduction
failures. They prevent the community from repeating the same unsuccessful work.
