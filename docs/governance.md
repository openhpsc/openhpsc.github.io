<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Project governance

## Working model

OpenHPSC begins as a maintainer-led community project. Contributors propose
changes through issues and pull requests; repository maintainers merge changes
and publish releases. This model can evolve as the contributor community grows.

No technical steering committee, institutional partnership, or external review
board is claimed by this documentation.

## Decisions

Small corrections can be proposed directly. Changes to architecture, interfaces,
licenses, or release criteria should first be explored in
[Community Discussions](https://github.com/openhpsc/community/discussions). Turn agreed follow-up work into
[community issues](https://github.com/openhpsc/community/issues) and link the originating discussion.
Track scoped tasks in the [R&D project](https://github.com/orgs/openhpsc/projects/2).

Summarize significant decisions in an architecture decision record (ADR) in the
[community repository](https://github.com/openhpsc/community/tree/main/adrs), preserving the reasoning
as the implementation evolves. Link the discussion, issue, and relevant evidence.

Use the proposed decision template:

```markdown
# ADR-0001: <decision title>
Status: proposed | accepted | rejected | superseded
Date: YYYY-MM-DD

## Context
Problem, constraints, and linked requirements.

## Alternatives
Options considered and their trade-offs.

## Decision
Selected option and supporting evidence.

## Consequences
Costs, risks, limitations, and follow-up verification.

## References
Issues, upstream revisions, papers, and experiment results.
```

The example identifier is a template; no hardware-selection ADR is accepted yet.

## Review and releases

A technical change should explain its scope, evidence, and affected requirements.
At least one independent technical review is the intended practice for changes
to protection or recovery logic; if review is unavailable, record that limitation
rather than implying it occurred.

A release should identify supported configurations, dependency versions,
verification results, known issues, and remaining gaps. Documentation-only
releases should say so explicitly.

## Participation and attribution

Credit contributions and upstream work. Keep discussions respectful, evidence-led,
and focused on the technical issue. Avoid publishing personal or confidential
information in issues or test logs.

Commercial use and participation are welcome under the applicable licenses.
Contributing to the project does not imply endorsement, employment, or ownership
of other contributors' work. File-specific notices govern reuse.
