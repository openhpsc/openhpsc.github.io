<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Reference architecture

**Status: proposed.** This page defines responsibilities and interfaces to
investigate. It does not select a final core or claim an implemented SoC.

## Architectural direction

The long-term reference platform separates throughput-oriented application
processing from a dependable control subsystem. Communication, shared memory,
and recovery are part of the architecture rather than assumptions left to the
application developer.

| Subsystem | Responsibility | Questions before selection |
| --- | --- | --- |
| Application processing | Perception, signal processing, autonomy workloads, and application software | Required ISA, MMU support, memory bandwidth, and acceleration? |
| Dependable control | Periodic control, monitoring, fault handling, and controlled restart | Timing model, lockstep/redundancy strategy, and recovery semantics? |
| Memory and interconnect | Integrity, access control, communication, and fault containment | ECC boundaries, scrubbing, arbitration, DMA access, and isolation? |
| Boot and supervision | Initialization, configuration checks, watchdogs, and fault records | What remains operational when a subsystem fails? |
| I/O | Observable bring-up and workload interfaces | Which interfaces are necessary for the selected experiment? |

## Hardware and software contract

Before integration, document the memory map, interrupt sources, timer behaviour,
reset state, boot entry, console interface, and fault-status registers. Record
which properties are fixed and which are configuration-dependent.

RTEMS is the initial RTOS direction to investigate for the control subsystem.
An RTEMS BSP must match these interfaces and the chosen CPU configuration.
Application processing may later use Linux where justified by the workload.

## Candidate building blocks

| Candidate | Reason to evaluate | Evaluation boundary |
| --- | --- | --- |
| CVA6 / Cheshire | Open application-class RISC-V processing and a host SoC | Establish functional baseline and memory integration before resilience work |
| Carfield | Existing open mixed-criticality integration | Study subsystem interfaces, predictability, and recovery mechanisms |
| PULP Safety Island | Public triple-core-lockstep control subsystem | Review fault model, recovery, verification, and FPGA feasibility |
| Ibex | Smaller, extensively verified core | Review the exact configuration and system-level error response |
| Ara | Open vector acceleration | Evaluate only after baseline workloads and memory bottlenecks are understood |

These are upstream research candidates, not OpenHPSC partners. Follow their
[repositories and license notices](references.md); evaluate pinned revisions,
not just project descriptions.

## Design decisions that remain open

1. Which control subsystem best supports a small, reproducible first experiment?
2. Which faults can be handled locally, and which require a subsystem restart?
3. Which resources can be shared without violating the chosen timing model?
4. What evidence is required to justify adding an application processor?
5. Which board can contributors obtain and which design fits it with timing margin?

Record significant answers with the [architecture decision process](governance.md).
The first implementation should realize the [demonstrator](demonstrator.md),
not the entire long-term architecture in one step.
