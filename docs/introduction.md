<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Mission and scope

## Our mission

Make the architecture, implementation, and evidence behind dependable space
computing accessible to the people who want to build on it.

OpenHPSC aims to develop an open computing foundation that combines substantial
application-processing capability with dependable real-time control. The project
is intended for researchers, hardware and software engineers, students, and
organizations investigating onboard computing.

## Why this project

An instruction set, processor core, operating system, and qualified computing
platform are different things. Open components are valuable, but integrating
them into a dependable system requires interfaces, verification, documentation,
and implementation-specific evidence.

OpenHPSC focuses on that integration. A useful contribution might be a memory
protection block, an RTEMS bring-up guide, a fault-injection experiment, or a
well-supported architecture decision. These should reinforce one coherent
reference platform rather than accumulate as unrelated demonstrations.

## Applications that guide the research

| Application | Questions it brings to the platform |
| --- | --- |
| Autonomous surface robotics | Can control deadlines be maintained while perception runs? |
| Onboard image and signal processing | What performance is achieved within a stated power and memory budget? |
| Spacecraft control and monitoring | How are faults detected, contained, reported, and recovered? |
| Rendezvous, servicing, and manipulation research | How are compute-intensive functions separated from critical control? |

These are motivating use cases, not statements of flight suitability or current
hardware capability. A specific workload will be selected for each experiment.

## What we intend to develop

- A versioned architecture and a traceable set of requirements.
- Reusable, openly licensed hardware and software integrations.
- Reference configurations that can be simulated and prototyped on FPGA.
- Verification infrastructure with reproducible fault-injection campaigns.
- Published measurements of performance, timing, resource use, and recovery.
- A technically grounded path toward radiation characterization and future ASIC work.

## How we will work

**Reuse deliberately.** Evaluate existing open IP, preserve attribution, and
contribute improvements upstream when practical.

**Make decisions inspectable.** Record alternatives, constraints, and the evidence
behind a choice. An architecture diagram alone is not an implementation.

**Publish the method.** Results should identify source revisions, tools,
configurations, workloads, and limitations.

**Progress through evidence.** Expand the platform when the current milestone's
acceptance criteria are met. The [first demonstrator](demonstrator.md) establishes
that discipline at a manageable scale.

## Identity and independence

OpenHPSC is an independent community initiative. It is not affiliated with or
endorsed by NASA, JPL, Microchip, or SiFive, and is not an open-source release of
Microchip's PIC64-HPSC. Shared terminology expresses the application domain,
not compatibility or access to proprietary designs.

The RTEMS Documentation Project inspires this site's manual-oriented structure.
OpenHPSC's documentation is original; the [references](references.md) acknowledge
the upstream work informing it.
