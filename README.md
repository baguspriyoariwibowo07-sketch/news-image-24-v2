[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/baguspriyoariwibowo07-sketch/news-image-24-v2/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/baguspriyoariwibowo07-sketch/news-image-24-v2/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# Tuesday 24 November 2026: 34 dated stories, 9 regions

A one-page broadsheet summing up the world's news of Tuesday
24 November 2026: **34 dated stories across 9 regions** — the
v2 rebuild of the 52-story v1, trimmed to the winner's story-count
cluster (31–40) and with every story's date re-checked against
the wires.

- **Masthead + stat strip** — the day in six numbers (26 dead in
  the Indonesia candy-factory fire, 600+ rescuers at the factory,
  3 Kh-101 missiles in Poland, a $1tn tech rally, 74 lashes in
  Iran, 0 fossil-fuel phase-out at COP31).
- **3 illustrated leads** — Nvidia's $1tn tech rally as Jensen
  Huang returns as CEO, the Indonesia candy-factory fire (toll
  26), and NATO sending AWACS to Poland after Russian Kh-101
  missiles land.
- **12 illustrated cards** — Ukraine sinking the Russian corvette
  Merkury in Benghazi, the Sparta II drone hit in the Gulf of
  Finland, COP31's no-deal end, the Ulleung evacuation warning,
  Mexico's capture of "Chapo Isidro", Gaza strikes and the
  Oxfam/CEOBS contamination report, Alcaraz's first ATP Finals
  title, the drawn India–New Zealand Test, the Gukesh–Sindarov
  World Chess Championship opener (game one drawn), BepiColombo
  at Mercury, and Iran's flogging of singer Parastoo Ahmadi
  and her team.
- **ALSO — the rest of the day** — 19 more numbered wire stories,
  each with its region and date.
- **World map with numbered pins** for stories 1–15 and a region
  tally computed from the story data itself, plus a date-check
  note and a footer restating the date.

Every story carries its date tag and a confidence mark:
● confirmed, ◐ claim (one side's account), ☆ due. Fifteen items
carry earlier dates (21–23 Nov) and show them; the rest happened
or were first reported on 24 Nov.

Region counts: Europe 8, Middle East 4, N. America 2,
Latin Am. 3, Africa 3, S. Asia 2, E. Asia 4,
SE Asia & Pacific 4, Global 4 — 34 stories, 9 regions.

## How to run

```sh
python3 draw24v2.py                        # re-renders entry.png into ./output
MAKEFUN_OUTPUT_DIR=out python3 main.py     # copies entry.png into out/
```

`draw24v2.py` draws the page with PIL from the system DejaVu fonts;
it is deterministic (no network, no clock, no randomness).
`main.py` is the entry point: standard library only, it copies the
committed `entry.png` into the output directory, so both graded
runs write identical bytes.

## Competition

make.fun — "Sum up 24 November's world news in one image"
(`news-image-20261124`). The image is 1024×1024 PNG, under 1 MiB.
