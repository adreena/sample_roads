from subprocess import call
import os

executables = [
    "sumo",
    "sumo-gui",
    "netconvert",
    "netedit",
    "duarouter"
]

libraries = [
    "/usr/local/opt/fox/lib/libFOX-1.6.0.dylib",
    "/usr/local/opt/freetype/lib/libfreetype.6.dylib",
    "/usr/local/opt/jpeg/lib/libjpeg.9.dylib",
    "/usr/local/opt/libpng/lib/libpng16.16.dylib",
    "/usr/local/opt/libtiff/lib/libtiff.5.dylib",
    "/usr/local/opt/proj/lib/libproj.12.dylib",
    "/usr/local/opt/xerces-c/lib/libxerces-c-3.1.dylib",
    "/usr/local/opt/gdal/lib/libgdal.1.dylib",
    "/usr/local/opt/json-c/lib/libjson-c.2.dylib",
    "/usr/local/opt/freexl/lib/libfreexl.1.dylib",
    "/usr/local/opt/geos/lib/libgeos_c.1.dylib",
    "/usr/local/opt/giflib/lib/libgif.7.dylib",
    "/usr/local/opt/libgeotiff/lib/libgeotiff.2.dylib",
    "/usr/local/opt/libspatialite/lib/libspatialite.7.dylib",
    "/usr/local/opt/sqlite/lib/libsqlite3.0.dylib",
    "/usr/local/opt/pcre/lib/libpcre.1.dylib",
    "/usr/local/opt/libxml2/lib/libxml2.2.dylib",
    "/usr/local/opt/liblwgeom/lib/liblwgeom-2.1.5.dylib",
    "/usr/local/Cellar/geos/3.6.2/lib/libgeos-3.6.2.dylib"
]

def command(cmd):
    print cmd
    call(cmd.split())

for lA in libraries:
    lAName = os.path.basename(lA)
    command("install_name_tool -id @loader_path/%s %s" % (lAName, lAName))
    for lB in libraries:
        lBName = os.path.basename(lB)
        command("install_name_tool -change %s @loader_path/%s %s" % (lB, lBName, lAName))

for executable in executables:
    for l in libraries:
        lName = os.path.basename(l)
        command("install_name_tool -change %s @loader_path/%s %s" % (l, lName, executable))
