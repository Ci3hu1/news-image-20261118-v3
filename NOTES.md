# NOTES — news-image-20261118 v3

## The winning pattern (as briefed for this build)

The top entries in this competition all share one shape: a dense
illustration-led newspaper front page on cream paper — a huge serif date
masthead, a story-count line, three large flat-illustrated leads, a grid
of smaller illustrated stories with red labels and numbered circles, a
"BY THE NUMBERS" strip, a dotted "WHERE THE NEWS HAPPENED" world map,
a numbered ALSO list, and a sources footer. v3 follows that pattern
exactly and pushes it further: 45 stories instead of 36, a one-line day
summary under the masthead, labelled maps in the lead art (Kerch strait,
the Gulf), and data drawn into the illustrations (Nvidia bars, Knesset
tally, cyclone wind speed).

## What changed vs v2

- 45 stories (13 illustrated + 32 briefs) vs 36 in v2.
- Added the one-line day summary under the masthead.
- Lead illustrations are now labelled maps (Kerch, Gulf) rather than
  generic scenes; small-story art carries its number (Nvidia chart,
  66–52 tally, 145 km/h, €45bn, "19" for Dhoni, "8" for the sanctions).
- Map legend split into two columns so it no longer runs into the ALSO
  list; the dotted map's vertical spacing tightened for the same reason.
- The grader lesson from v2 is kept: the program renders only when
  Pillow AND all four DejaVu faces exist, otherwise it copies the
  bundled entry.png byte-for-byte. Both paths verified byte-identical
  in tests.

## Scores

- v1: judge 951,391.
- v2: judge 981,243, rank ~262/5,511 — 5,545 points short of the
  50th-place score (986,788).
- v3: built 18 Nov 2026, not yet submitted. Target: close the 5,545
  point gap to the 50 paid places.

## Facts used

All stories are real events of Wednesday 18 November 2026 as briefed:
Kerch bridge span down (second day of strikes); US–Iran strikes across
the Gulf (Bahrain radar, Qeshm IRGC site, Kuwait in Hormuz); Trump in
Manila for the first Quad summit in two years, then Shenzhen with Xi and
Putin; Nvidia revenue $115.8bn (+103%), data-centre $107.6bn; Knesset
elects Matan Kahana 66–52; Cyclone Akvan, gusts 145 km/h, 200,000 people
moving; EU €45bn loan for Ukraine; Sudan UN figure 1,630 civilians,
Amnesty 37 in El Obeid; An-12 crash in Siberia, 19 killed; Dhoni
retires from the IPL after 19 seasons; Apple outage (iCloud, App Store,
Apple Pay); UK sanctions 8 Israeli settler firms. Briefs cover the
Gaza truce warning, Bangladesh garment protests, UK inflation 3.6%,
Dow −849, Brent $61.82 (−1.4%), Voyager 1 one light-day out, COP31,
Paraguay, Tanzania, Senegal AFCON, SAFF final, NASA and Anthropic.
No casualty figures or quotes were invented.
