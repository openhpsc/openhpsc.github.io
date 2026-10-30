<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Fundamentals

## Space computing has several constraints

Useful compute capability depends on more than a peak benchmark. Power, thermal
limits, memory bandwidth, latency, fault recovery, and the mission's radiation
environment all influence a design. Requirements must identify the intended
workloads and operating environment before setting numerical targets.

## Radiation effects

| Effect | Meaning | Engineering response to investigate |
| --- | --- | --- |
| Single-event upset (SEU) | A particle changes stored state | Error-correcting codes, scrubbing, redundancy |
| Single-event transient (SET) | A transient pulse disturbs logic | Appropriate filtering, redundancy, implementation-aware analysis |
| Single-event latch-up (SEL) | A particle triggers a high-current condition | Suitable devices, current monitoring, power protection and recovery |
| Total ionizing dose (TID) | Cumulative exposure changes device characteristics | Device/process selection, dose analysis, irradiation testing |
| Displacement damage | Radiation changes the semiconductor lattice | Component-specific analysis and testing |

These are an introduction, not a complete radiation assurance plan. NASA's
[radiation overview](https://www.nasa.gov/reference/jsc-radiation/) and
[ECSS-Q-ST-60-15C Rev.1](https://ecss.nl/standard/ecss-q-st-60-15c-rev-1-radiation-hardness-assurance-20-march-2025/)
provide starting references.

## Fault tolerance and its limits

Dual-core lockstep compares execution to detect disagreement. It does not by
itself establish which result is correct. Triple-modular redundancy can mask a
fault under a suitable fault model, but voters, shared resources, and correlated
faults must also be considered.

Memory ECC can detect or correct particular error patterns. Its effectiveness
depends on the code, layout, access patterns, and scrubbing strategy.

```{important}
Fault injection evaluates a stated fault model. It does not establish TID
tolerance, latch-up immunity, or suitability for a mission. A result applies to
the tested implementation and conditions, not automatically to every FPGA or ASIC.
```

## Evidence levels

Use these descriptions precisely:

- **Proposed:** a requirement or design direction under discussion.
- **Implemented:** source and a reproducible build are available.
- **Verified:** a defined test has passed for an identified configuration.
- **Radiation-characterized:** physical test conditions and results are published.
- **Qualified:** a defined qualification process has been completed for a stated scope.
