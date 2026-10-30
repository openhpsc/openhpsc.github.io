<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# First demonstrator

## Objective

Demonstrate a repeatable RISC-V control workload, introduce a bounded fault
model, and measure how a selected protection mechanism changes the outcomes.

This is the proposed first hardware/software milestone. It establishes a
baseline for later RTEMS integration and larger computing configurations.

## Minimum scope

- One documented processor/subsystem configuration in RTL simulation.
- Boot memory, working RAM, a timer, and an observable result interface.
- A deterministic bare-metal workload with known expected outputs.
- An unprotected baseline and a clearly specified protected configuration.
- Campaign scripts producing replayable, machine-readable records.

Use a periodic control-oriented workload with known inputs and output checks.
The exact algorithm, numerical representation, execution period, and output
oracle must be agreed before measuring results.

## First protection experiment

Begin with one mechanism, such as protected working memory or core lockstep.
Choose it based on upstream support and the question being tested. Avoid changing
CPU, workload, memory layout, and protection policy simultaneously: the
comparison needs an interpretable baseline.

List unprotected components explicitly, including any voters, buses, clocks,
reset logic, debug paths, or external memory outside the experiment's scope.

## Acceptance criteria

| Gate | Required result |
| --- | --- |
| Functional baseline | Known workload outputs and a reproducible completion condition |
| Dependency control | Exact revisions, licenses, host tools, and configuration recorded |
| Fault-free behaviour | Both configurations pass the selected functional tests |
| Fault observability | Injection and outcome records can be correlated |
| Replay | A selected fault record can be rerun deterministically |
| Classification | Correct output, recovery, detected failure, silent corruption, and timeout are distinguished |
| Cost comparison | Protection overhead is reported with a clear measurement method |
| Independent reproduction | Another contributor can reproduce a documented run |

## FPGA follow-up

After simulation, select one board and publish the build flow, constraints,
resource utilization, timing results, programming steps, and hardware logs.
A board is supported only when that configuration has actually been exercised.

A desktop FPGA prototype establishes functionality on that device. It does not
by itself establish radiation performance or flight qualification.

## Deliverables

A release should contain a configuration manifest, build instructions, workload,
expected outputs, fault campaign configuration, raw records, analysis, and a
short limitations statement. See [Verification](verification.md) for the evidence format.
