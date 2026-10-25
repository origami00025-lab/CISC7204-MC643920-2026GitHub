Geoplotlib official source: https://github.com/andrea-cuttone/geoplotlib
Bundled under its MIT license; see geoplotlib/LICENSE.
Compatibility changes: official Python 2 syntax/imports converted with lib2to3;
NumPy int/float aliases replaced by builtin types; ndarray.ptp replaced by np.ptp;
SciPy Delaunay.vertices replaced by simplices; HTTPS for network services.
pyglet 1.5.31 is bundled to preserve the required OpenGL 1.x API.
course_maps.py prepares the public tile cache, captures actual renderer frames,
and dispatches real keyboard events to test the custom layer. No maps are simulated.
Approved service replacement: Esri World Light Gray Base / World Dark Gray Base
replace key-protected CARTO Positron / Dark Matter. Custom HOT remains OSM France.
Tiles retain provider attribution. Cached tiles permit the captured views offline;
new zoom levels require internet access. User's source data have not been changed.
Run notebooks in Anaconda Python 3 with the whole directory preserved.
