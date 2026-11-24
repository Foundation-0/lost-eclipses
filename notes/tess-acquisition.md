# TESS cache acceptance

Status: preparation for review. No observational result is claimed.

The input CSV names star_id, sector, source_url, product_id, pipeline, retrieved_utc and cache_path. Run `python3 tools/cache_manifest.py products.csv /outside-git/cache manifest.json` after retrieval. The script hashes files without fetching data, loading credentials or assuming rights to an upstream cache.

Prefer a documented public MAST product where available. Record SPOC or QLP provenance and aperture/crowding metadata. An agreement is needed before using eumemic's cached products. Distinguish no product, failed retrieval, invalid product and no sector coverage.

Acceptance still needs a bounded MAST acquisition adapter, actual target IDs, cache downloads and ten independent MAST spot checks. This manifest is useful to bind those later products; it does not claim they already exist.
