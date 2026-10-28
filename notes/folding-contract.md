# Eclipse screen contract

Status: preparation for review. No observational result is claimed.

Inputs must use a common time scale and epoch, and magnitudes in a compatible band. TESS flux must be converted to differential magnitudes before this script; a magnitude amplitude cannot be divided by a relative-flux depth. Preserve sectors, quality masks and source hashes.

The screen takes medians in one hundred phase bins, requires three samples in at least ninety percent of bins and compares the deepest bin with the baseline median. Its below-twenty-percent flag is candidate triage, not a disappearance verdict. Narrow eclipses, period drift, doubled/halved periods, phase gaps, crowding and different passbands can defeat it.

Run `python3 tools/fold_depth.py lightcurve.csv --period DAYS --epoch EPOCH --amplitude MAG --output folded.json`. The output retains every phase-bin sample so a reviewer can plot it. Plot generation, actual catalogue-linked curves, period alternatives, stopped/ordinary controls and independent reruns remain acceptance requirements.
