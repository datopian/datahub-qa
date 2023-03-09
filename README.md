<p align="center">
  <a href="https://datahub.io/">
    <img alt="datahub" src="http://datahub.io/static/img/logo-cube.png" width="146">
  </a>
</p>

<p align="center">
  Bugs, issues and suggestions re datahub.io.
  <br />
  <br /><a href="https://gitter.im/datahubio/chat"><img src="https://img.shields.io/gitter/room/frictionlessdata/chat.svg" /></a>
</p>

## Create a new issue

If you have found a bug, have a suggestion for a feature or just have a question about DataHub.io, please:

**[Create a new issue &raquo;](https://github.com/datahubio/qa/issues/new)**

Note on our use of severities (choose the correct label):
- **Critical**
  - The system or a key scenario is broken, no workaround
  - System performance is highly degraded
  - High impact on user
  - Major security breach
  - Embarrassing
- **Major**
  - The system or a key scenario is broken, with a workaround
  - A common scenario is broken, no workaround
  - System performance is moderately degraded
  - Moderate impact on user
- **Minor** 
  - A common scenario is broken, with a workaround
  - An uncommon scenario is broken, no workaround
  - System performance is slightly degraded
  - Low impact on user
- **Trivial**
  - An uncommon scenario is broken, with a workaround
  - No impact on user
  - Minor cosmetic issues

We also have a **Blocker** label in cases where this issue blocks someone from working.

## Chat Resources

If you would prefer to get help via live chat rather than the issue tracker in
this repository, you can try:

[Discord](https://discord.com/invite/KrRzMKU)


## Daily statistics

Datahub-QA issues dataset shows daily statistics for this issue-tracker repo.
Watch it here: https://datahub.io/examples/datahub-qa-issues-tracker

### Data

Dataset count issues with labels:  
**'Critical', 'Major', 'Minor', 'Trivial', 'NEW FEATURE', 'closed'**

Last column shows how many issues was closed on this date (issues with 'Duplicate' label not counts)

Data is sourced from the github API.
Process is recorded and automated in python script.
Data updates daily using Travis cron job.
