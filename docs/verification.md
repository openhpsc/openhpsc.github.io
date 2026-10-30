<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Verification and evidence

## The question comes first

Every experiment must state what it is trying to establish. Functional
correctness, fault detection, recovery, real-time behaviour, and radiation
response require different evidence. One passing test cannot stand in for all
of them.

## Evidence progression

| Stage | What it can establish | What it does not establish alone |
| --- | --- | --- |
| Functional simulation | Behaviour under tested inputs and configuration | Exhaustive correctness or physical radiation response |
| Assertions and formal checks | Properties under stated assumptions and explored bounds | Properties beyond the model, assumptions, or bounds |
| Fault injection | Response to modeled faults at selected locations and times | A device's physical upset rates or TID tolerance |
| FPGA execution | Functionality and measurements on a specific implementation | ASIC behaviour or a space-qualified system |
| Physical radiation testing | Observed response under reported conditions | Suitability for every environment or mission |
| Qualification activity | Evidence against defined requirements and scope | Blanket qualification of every derivative design |

## Campaign definition

Record the model before the campaign runs:

- **Fault location:** which registers, memory bits, logic nodes, or interfaces are eligible?
- **Fault type:** bit flip, stuck-at state, transient pulse, or another explicit model?
- **Timing and duration:** when is the fault applied and when is it removed?
- **Multiplicity:** one fault at a time, multiple bits, or correlated events?
- **Workload:** inputs, expected outputs, checkpoints, and run duration.
- **Sampling:** exhaustive or sampled locations, random seeds, exclusions, and sample size.
- **Observation:** completion condition, timeout, fault indications, and classification rules.

Changing the fault model changes what the results mean. Keep campaigns versioned.

## Outcome classification

Use mutually exclusive primary outcomes and separate event flags. For example:

| Primary outcome | Definition |
| --- | --- |
| Correct, no recovery | Expected result without a recovery action |
| Correct after recovery | Expected result after an observed recovery action |
| Detected failure | System reports an error and cannot meet the expected result |
| Silent data corruption | Incorrect result without the required error indication |
| Timeout or hang | Completion condition is not reached within the declared observation window |
| Invalid experiment | Injection or instrumentation failed; report separately from valid trials |

A detected error flag can be recorded alongside a successful outcome. Define
precedence for simultaneous events before analyzing results. Include denominators,
excluded trials, raw counts, and uncertainty where appropriate.

## Suggested result record

```json
{
  "experiment_id": "example-memory-seu",
  "source_revision": "<commit>",
  "configuration": "<configuration-id>",
  "workload": "<workload-id>",
  "seed": 1,
  "injection": {"target": "<signal-or-memory>", "bit": 0, "cycle": 100},
  "outcome": "correct_after_recovery",
  "error_detected": true,
  "recovery_cycles": 12
}
```

This is an illustrative schema, not a test result. Add units, tool versions, fault
duration, multiplicity, and other model-specific fields in the campaign manifest.

## Release evidence

For each supported configuration, publish requirement coverage, passing and
failing tests, known limitations, reproducibility instructions, and measured
implementation costs. A failing result is useful when it is reported clearly
and can be reproduced.
