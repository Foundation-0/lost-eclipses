# GCVS target export

Status: preparation for review. No observational result is claimed.

Query VizieR catalogue B/gcvs for eclipsing types EA, EB and EW, retaining compound classifications for review. Select a finite positive period below ten days and a recorded maximum magnitude below twelve. Export the original type, photometric band, limit flags, period, epoch, maximum and minimum, not only a derived amplitude.

The output schema is gcvs_id, type_raw, period_days, epoch_and_scale, max_mag, min_mag, band, amplitude_status, ra_deg, dec_deg, coordinate_epoch, gaia_dr3_source_id, match_distance_arcsec, candidate_count and match_status. A magnitude limit or mixed bands cannot silently become an exact eclipse amplitude.

Cache the raw VizieR response with query text, UTC time and SHA-256. Match positions with proper motion and epoch accounted for; retain every plausible Gaia neighbour and an unmatched record. A nearest neighbour alone is insufficient in crowded fields.

Reconcile the observed count with the unverified scouting count 3280. Use a fixed seed to select ten matches for independent SIMBAD inspection. Catalogue acquisition, match adjudication and that inspection remain outstanding; this file supplies the export and acceptance contract.
