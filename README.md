[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/yuyan5319-crypto/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/yuyan5319-crypto/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World in One Day — 25 November 2026

One image summing up the world news of Wednesday 25 November 2026, as a
newspaper front page with a masthead and six stories from around the
world:

1. **War — Ukraine:** Zelenskiy confirms Ukraine sank Russian ships in
   the Gulf of Finland and off Benghazi, Libya; Moscow calls the drone
   strikes "terrorism".
2. **Middle East — Riyadh:** Houthis strike the PIF Tower, the city's
   tallest skyscraper, wounding 11 — the second hit in a week.
3. **Technology — Washington:** a US jury convicts Huawei of stealing
   trade secrets in the trial over its Iran business.
4. **China — Beijing:** China investigates Politburo member and Shanghai
   party chief Chen Jining.
5. **Climate — Antalya, Türkiye:** COP31 collapses with no deal after
   oil and gas producers block fossil-fuel phaseout language.
6. **Gaza:** Israel kills Hamas internal security chief Naeem Abu Nahel
   in a Gaza City air strike.

The footer strip adds four more stories from the same day: the UN
finding that five women were killed every hour by relatives in 2025,
Sarkozy's corruption case sent to trial, Shein's $100M FTC settlement,
and gunmen seizing 25 hostages in a Colombia supermarket.

The image is drawn by hand with Pillow (flat pictograms and typeset
headlines) — no news photographs. `draw.py` draws `entry.png`;
`main.py` copies it to `/output/entry.png` because the grading sandbox
runs Python 3.13 with the standard library only, so Pillow is not
available there. Run it locally with
`MAKEFUN_OUTPUT_DIR=out python3 main.py`. Two runs write identical
bytes.

License: MIT.
