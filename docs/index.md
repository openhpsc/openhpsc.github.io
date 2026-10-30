<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# OpenHPSC

**Open High-Performance Spaceflight Computing**

An open foundation for the computers that will sense, decide, and act in space.

OpenHPSC is a community project working toward open-source, high-performance,
fault-tolerant computing for space applications. Our ambition spans the hardware,
real-time software, and verification evidence needed to understand a system,
reproduce it, and improve it together.

We begin with a shared technical foundation: clear requirements, reusable open
hardware, and experiments with published methods and results.

## A shared foundation for space computing

Spacecraft autonomy brings demanding computation closer to sensors and actuators.
Useful performance must coexist with predictable execution, bounded resources,
and recovery from faults. OpenHPSC brings these concerns into one public
engineering effort.

| Workstream | What we aim to publish |
| --- | --- |
| **Architecture & hardware** | Requirements, design decisions, openly licensed RTL, and reference configurations |
| **Real-time software** | Bring-up software, RTOS integration, drivers, and representative workloads |
| **Resilience & verification** | Fault models, protection mechanisms, repeatable tests, and traceable results |
| **Prototyping & characterization** | FPGA build flows, implementation measurements, and a path toward physical radiation testing |

## Explore the project

- **[Read the mission](introduction.md)**: the problem, purpose, and scope.
- **[Study the architecture](architecture.md)**: how application processing and dependable control could fit together.
- **[Review the first demonstrator](demonstrator.md)**: a bounded starting point with explicit acceptance criteria.
- **[Find a contribution](contributing.md)**: concrete ways to help with hardware, software, research, or documentation.

## Where we are today

**Definition phase · Documentation release 0.2**

This release establishes the project charter, draft requirements, research
priorities, and verification approach. Processor selection and hardware support
remain open decisions. Implementation results will be added as experiments are
completed; radiation tolerance and qualification will be claimed only for a
specific implementation with supporting evidence.

Our immediate objective is to agree on one reproducible control-subsystem
experiment. The [roadmap](roadmap.md) defines what must be demonstrated before
expanding the design.

## Build with the community

Start by reviewing a requirement, reproducing an upstream example, or proposing
an experiment. Each contribution should leave the next person with something
clearer, testable, or easier to reproduce.

- **[Start a discussion](https://github.com/openhpsc/community/discussions/new/choose)** to introduce yourself, ask a question, or explore an idea.
- **[Open a community issue](https://github.com/openhpsc/community/issues/new)** for a concrete research question, requirement, or experiment.
- **[Follow the R&D project](https://github.com/orgs/openhpsc/projects/2)** to see the work being tracked.

The [community repository](https://github.com/openhpsc/community) coordinates project work.
For website errors or broken documentation, use the
[documentation issue tracker](https://github.com/openhpsc/openhpsc.github.io/issues).

```{toctree}
:hidden:
:maxdepth: 2
:caption: Project

introduction
roadmap
governance
contributing
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Technical documentation

fundamentals
requirements
architecture
demonstrator
verification
research
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Resources

getting-started
troubleshooting
changelog
references
license
```
