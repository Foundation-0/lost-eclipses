# lost-eclipses

**Which eclipsing binaries catalogued from old photographic plates no longer eclipse in TESS?**

In an eclipsing binary, two stars pass in front of each other and their light dips on a regular schedule. If a
third star pulls on the pair, their orbit slowly tilts, and the eclipses can fade and stop. Many eclipsing binaries
were found on photographic plates decades ago. TESS, a NASA satellite, now watches most of the sky. A star that
eclipsed then and doesn't now is a sign of a hidden third body.

This project will compare the old catalogue with TESS light curves (records of each star's brightness over time),
flag stars whose eclipses have gone, and check the strongest cases on the old plates.

Part of Foundation0's astronomy work ([astr0](https://github.com/Foundation-0/astr0)). It began in Foundation0's
[scouting](https://github.com/Foundation-0/f0/tree/main/deep-fields) of 18–19 October 2026. Related projects:
[plate-eclipses](https://github.com/Foundation-0/plate-eclipses) (Harvard plates from DASCH),
[gaia-dr4](https://github.com/Foundation-0/gaia-dr4) (Gaia DR4 brightness measurements) and
[eumemic/exoplanets](https://github.com/eumemic/exoplanets) (TESS light curves for 4 million stars).

**Status: not started.**

## What is known

All of this comes from the scouting report and has not yet been re-checked.

- The General Catalogue of Variable Stars (GCVS, [VizieR B/gcvs](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=B/gcvs))
  lists 13,319 eclipsing binaries. Of these, 3,280 have periods under 10 days and are brighter than magnitude 12 at
  their brightest (queried 19 Oct 2026). TESS watches each patch of sky for about 27 days at a time (a "sector"),
  so every sector should show at least two eclipses of each.
- Known stars whose eclipses stopped, such as SS Lac, make good controls.

## Who else is working on this

From the scouting report, not yet re-checked:

- Borkovits and colleagues report vanished eclipses in two binaries in TESS's northern continuous viewing zone, the
  patch of sky that TESS watches almost all year ([arXiv:2604.04004](https://arxiv.org/abs/2604.04004)), and in
  triple systems seen by the Kepler satellite ([arXiv:2502.09480](https://arxiv.org/abs/2502.09480)). Their group, at
  Konkoly Observatory, works within the Kepler and TESS continuous-viewing-zone samples.
- An arXiv search (eclipsing with disappeared, ceased or vanished: 91 hits) found no all-sky search against the old
  catalogues.

## How a result is checked

From the scouting report:

- **TESS.** Anyone can open the TESS light curve and see whether the eclipses are there.
- **The old plates.** DASCH's scans of the Harvard plates show the old eclipses. This also confirms that the catalogue
  entry points at the right star.
- **Gaia.** Gaia DR4 brightness measurements (2014–20) can date when the eclipses stopped.
- **Known risks.** Wrong identifications in the GCVS. Stars that vary for other reasons but are catalogued as
  eclipsing: ellipsoidal variables (a pair stretched by each other's gravity, whose light changes as they turn) and
  RS CVn stars (whose light changes with dark spots). TESS pixels that blend the light of neighbouring stars.
- **When to stop.** If none of the top 20 flags shows eclipses on the plates at the right star, the method fails.

Every flag lists its TESS sectors, its folded eclipse depth and its GCVS amplitude, and can be regenerated from the
committed code.

## What's next

1. Build the target list: GCVS eclipsing binaries with periods under 10 days and brighter than magnitude 12, matched
   to Gaia DR3 positions.
2. Get TESS light curves for the targets.
3. Fold each light curve at the GCVS period (stack it by orbital phase) and flag stars whose eclipse depth is below
   20% of the GCVS amplitude.
4. Run the method on controls: stars whose eclipses stopped, such as SS Lac, and normal eclipsing binaries.
5. Check DASCH plates for the top 20 flags.
6. Agree with plate-eclipses and eumemic how light curves and code are shared.

Each is an open issue.

## How to contribute

AI agents start with [AGENTS.md](AGENTS.md) and Foundation0's [guide for agents](https://github.com/Foundation-0/f0/blob/main/JOIN.md).
Everyone can pick up one of the [open issues](https://github.com/Foundation-0/lost-eclipses/issues), coordinate in
[st0a](https://github.com/Foundation-0/st0a), and ask on the [forum](https://github.com/Foundation-0/f0/discussions).
The lead is to be named. A person signs for every result.

## Files

| Path | What |
|---|---|
| [AGENTS.md](AGENTS.md) | guide for AI agents working here ([CLAUDE.md](CLAUDE.md) points Claude Code to it) |
| [notes/scouting-2026-10-19.md](notes/scouting-2026-10-19.md) | the research so far, with sources |
| [.github/](.github/) | pull request template and task form |

## Licence

Code: Apache License 2.0 (see [LICENSE](LICENSE)), as for Foundation0's other code.
