CISC7204 Suggested Exercise 09 — LU MENGJIE (MC643920)

Six executed notebooks follow the supplied Bokeh tutorial tasks. Data are unchanged.
P1_folder: Exercise9.01, Exercise9.02, Activity9.01.
P2_folder: Exercise9.03, Exercise9.04, Activity9.02.
Each contains Jupyter Notebooks and Screen Shots. Datasets is shared.

Run: install requirements.txt, open a notebook in Jupyter and select Restart Kernel
and Run All Cells. Preserve the ../../Datasets relative path. Run All also reconnects
the Python ipywidgets callbacks. Saved widget states alone cannot execute Python.

Compatibility: Bokeh 3 width/height replace plot_width/plot_height; scatter(marker=...)
replaces legacy marker helpers and Cross; TabPanel replaces Panel. Numeric-only
group means avoid pandas errors on text columns. Stock dates contain both date-only
and full timestamps and are parsed with format='ISO8601'.
The present helper executes show and embeds the same real Bokeh model as a portable
inline HTML document for saved-output viewing in Notebook 7. outputs/*.html are
standalone plots with bundled Bokeh JavaScript. HTML plots support Bokeh tools and
tabs, but Python dropdown/slider callbacks require a live notebook kernel.

Interpretation: world_population.csv contains population DENSITY, not total people.
The tutorial dataset-row mean includes aggregate regions and is not an area-weighted
global density. Olympic medal sums are athlete medal counts, including team sports,
and differ from official country medal-table totals.

The empty models plot in Exercise9.02 is intentional before renderers are added;
the Bokeh W-1000 warning at this stage is the tutorial demonstration, not a failed
final plot. The completed plot follows in subsequent cells.

References for compatibility:
https://github.com/bokeh/bokeh/wiki/Migration-Guides
https://docs.bokeh.org/en/latest/docs/user_guide/basic/scatters.html

AI assistance: OpenAI Codex assisted with coding, debugging, execution checks,
and preparing the submission guide. The required Moodle forum posts and ZIP submission were verified on 25 October 2026.
