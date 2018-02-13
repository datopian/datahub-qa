Datahub-QA issues tracker shows day-to-day number of the issues in the https://github.com/datahq/datahub-qa/

## Data 

Dataset count issues with labels:  
**'Critical', 'Major', 'Minor', 'Trivial', 'NEW FEATURE', 'closed'**

Last column shows how many issues was closed on this date (issues with 'Duplicate' label not counts)

## Preparation

Data is sourced from the github API.
Process is recorded and automated in python script.
You should run `process.py` every day to have the actual day-to-day information.
