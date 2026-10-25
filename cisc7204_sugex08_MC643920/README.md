# CISC7204 Suggested Exercise 08

LU MENGJIE — MC643920

Six completed Geoplotlib notebooks, saved outputs, 30 Jupyter screenshots, the four course datasets, compatibility support and original third-party licence files are included. Notebook code and saved outputs are byte-for-byte unchanged from the completed assignment.

## Restore the full dataset and run

The original `world_cities_pop.csv` is 164,325,024 bytes (over GitHub's ordinary 100 MiB file limit). It is stored losslessly as `Datasets/world_cities_pop.csv.zip`; no rows or columns were removed.

From this folder run:

```bash
python restore_large_files.py
python -m pip install -r requirements.txt
jupyter notebook
```

Open the notebooks under `P1_folder/Jupyter Notebooks` and `P2_folder/Jupyter Notebooks`, and run all cells. Keep the folder layout intact. The restore script verifies SHA-256 `14d45883d3d2426e50054c8777a7bad2fe68e59a6ddbbdb952c6bb68aafa8636`. The restored large CSV is ignored by Git so it is not accidentally committed above the limit.

## What is demonstrated

- Practice 01: layered point data, GeoJSON maps and filtering.
- Practice 02: city layers, keyboard interaction, alternative tile styles and aircraft animation.
- Real graphical windows require a desktop OpenGL environment; saved maps and animation outputs can be inspected without rerunning.
- CARTO's tutorial endpoints required an unavailable API key. With the student's approval, the original work used the documented Esri public light/dark basemap replacement and HTTPS for the Humanitarian style. The images do not claim to use CARTO.
- `Support/README.txt` documents the Python 3 / NumPy / SciPy compatibility changes. Vendored licences and attribution are preserved.

The original Moodle deadline was 18 October 2026, 23:00. This GitHub publication on 25 October is a later portfolio addition, not evidence of an on-time GitHub submission. Dataset files are course-provided; no new licence is asserted for third-party material.

AI assistance: OpenAI Codex assisted with implementation, checks and publication preparation.
