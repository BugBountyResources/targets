# Public Bug Bounty Targets Data
---
![Logo](logo_bbr.png)

A collection of over **5.1M sub-domains and assets** belonging to bug bounty targets, all put in a single file (using a [script](https://github.com/BugBountyResources/targets/blob/main/targets_extract.py) ).

Goal of this repo is to track changes in targets and add/remove new/old targets, in order to perform reconnaissance en-masse, by putting them all in one place.
Collecting all sub-domains at one place can make certain bulk operations like bulk vulnerability testing by fingerprinting easy, all at once!

Also, it is supposed to work as a **mirror** for [ProjectDiscovery's public bug bounty assets recon data](https://chaos.projectdiscovery.io).

## Workflow
  - Extract target data from [Chaos](https://chaos.projectdiscovery.io/), using the [targets_extract.py script](https://github.com/BugBountyResources/targets/blob/main/targets_extract.py)
  - Push data to GitHub

## Stats
---

| File                 | Number of Assets     |
|---------------------- | --------------------------|
| [Download Part 1](https://github.com/BugBountyResources/targets/raw/main/all_0.txt)       | **2.55M**  (2,556,493)             |
| [Download Part 2](https://github.com/BugBountyResources/targets/raw/main/all_1.txt)       | **2.55M**   (2,556,493)            |

Total collected: **5.1M assets** (5,112,986 assets)


## Source of Data
---
Data collected from [ProjectDiscovery's Chaos Project](https://chaos.projectdiscovery.io/).

### Credits
Thanks to the [ProjectDiscovery team](https://projectdiscovery.io) for sharing updated reconnaissance data of Public Bug Bounty programs!
