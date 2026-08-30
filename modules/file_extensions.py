"""
File-extension categories for an automated file organizer.

Source reference:
    https://fileinfo.com/filetypes

"""

FILE_TYPE_EXTENSIONS = {
    "Images": {
        # Raster image files
        ".bmp", ".dcm", ".dds", ".djvu", ".gif", ".heic", ".heif",
        ".jpg", ".jpeg", ".jfif", ".png", ".psd", ".psb", ".tga", ".tif", ".tiff",
        ".webp", ".raw", ".cr2", ".cr3", ".nef", ".arw", ".orf", ".rw2",
        ".dng", ".ico", ".jp2", ".exr", ".pcx", ".pbm", ".pgm", ".ppm",

        # Vector image files
        ".ai", ".cdr", ".emf", ".eps", ".ps", ".sketch",
        ".svg", ".vsdx", ".wmf", ".xar", ".cgm", ".fig", ".afdesign",
    },

    "Videos": {
        ".3gp", ".3g2", ".asf", ".avi", ".flv", ".m4v", ".mov",
        ".mp4", ".mkv", ".mpg", ".mpeg", ".swf", ".ts", ".vob", ".wmv",
        ".webm", ".ogv", ".rm", ".rmvb", ".divx", ".mts", ".m2ts", ".f4v",
    },

    "Audio": {
        ".aif", ".aiff", ".flac", ".m3u", ".m4a", ".mid", ".midi",
        ".mp3", ".ogg", ".wav", ".wma", ".aac", ".opus", ".amr",
        ".ape", ".cda", ".mpa", ".ra", ".voc", ".mka",
    },

    "Documents": {
        # Text files
        ".doc", ".docx", ".eml", ".msg", ".odt", ".pages",
        ".rtf", ".tex", ".txt", ".wpd", ".dot", ".dotx", ".ott",
        ".markdown", ".epub", ".mobi", ".azw", ".azw3", ".fb2",

        # Page-layout and presentation-style documents
        ".indd", ".key", ".oxps", ".pdf", ".pmd", ".ppt",
        ".pptx", ".pub", ".qxp", ".xps", ".pps", ".ppsx", ".potx",

        # Subtitle / caption files
        ".srt", ".vtt", ".ass", ".ssa", ".sub", ".sbv",
        ".sami", ".smi", ".stl", ".ttml", ".scc", ".dfxp", ".itt",
    },

    "Spreadsheets": {
        ".numbers", ".ods", ".xlr", ".xls", ".xlsx", ".xlsm",
        ".xltx", ".xltm", ".ots", ".gsheet",
    },

    "Data": {
        ".aae", ".csv", ".dat", ".log", ".mpp", ".obb",
        ".rpt", ".tar", ".vcf", ".xml", ".yaml", ".toml",
        ".parquet", ".avro", ".ndjson", ".jsonl", ".tsv",

        # GIS data
        ".gpx", ".kml", ".kmz", ".osm", ".shp", ".geojson",
    },

    "Archives": {
        ".7z", ".cbr", ".gz", ".rar", ".tar.gz", ".tgz",
        ".zip", ".zipx", ".bz2", ".xz", ".lz", ".lzma",
        ".cab", ".arj", ".z", ".cbz", ".tar.bz2", ".tar.xz",
    },

    "Installers": {
        ".apk", ".app", ".appx", ".deb", ".dmg", ".exe",
        ".ipa", ".jar", ".msi", ".pkg", ".rpm", ".run",
        ".xapk", ".msix", ".appimage", ".snap", ".aab",
    },

    "Code": {
        ".bat", ".c", ".class", ".cmd", ".com", ".config",
        ".cpp", ".cs", ".h", ".hpp", ".java", ".kt", ".lua", ".m",
        ".md", ".pl", ".py", ".sb3", ".sh", ".sln",
        ".swift", ".unity", ".vb", ".vcxproj", ".xcodeproj",
        ".yml", ".rb", ".go", ".rs", ".ts", ".tsx", ".jsx",
        ".r", ".scala", ".dart", ".ipynb", ".asm", ".pyc",
        ".gradle", ".make", ".cmake", ".dockerfile", ".env",
    },

    "Web": {
        ".asp", ".aspx", ".cer", ".cfm", ".csr", ".css",
        ".html", ".htm", ".js", ".json", ".jsp", ".php", ".xhtml",
        ".mjs", ".scss", ".sass", ".less", ".vue", ".wasm",

        # Browser/plugin extensions
        ".crx", ".ecf", ".plugin", ".safariextz", ".xpi",
    },

    "Databases": {
        ".accdb", ".crypt14", ".db", ".mdb", ".odb",
        ".pdb", ".sql", ".sqlite", ".sqlite3", ".db3",
        ".frm", ".myd", ".myi", ".ndf",
    },

    "CAD & 3D": {
        # 3D image/model files
        ".3dm", ".3ds", ".blend", ".dae", ".fbx", ".max", ".obj",
        ".gltf", ".glb", ".usdz", ".c4d", ".ma", ".mb",

        # CAD files
        ".dgn", ".dwg", ".dxf", ".step", ".stp",
        ".iges", ".igs", ".skp", ".catpart", ".sldprt", ".sldasm",
    },

    "Fonts": {
        ".fnt", ".otf", ".ttf", ".woff", ".woff2", ".eot",
        ".pfb", ".pfm", ".fon",
    },

    "System": {
        ".ani", ".cab", ".cpl", ".cur", ".deskthemepack",
        ".dll", ".dmp", ".drv", ".icns", ".ico", ".lnk",
        ".reg", ".sys", ".efi", ".ovl", ".vxd",
    },

    "Settings": {
        ".cfg", ".ini", ".set", ".plist", ".conf", ".prefs",
        ".properties",
    },

    "Misc": {
        # Ambiguous / game / encoded / disk-image / backup / misc
        ".abk", ".arc", ".asc", ".bak", ".bin", ".crdownload",
        ".dem", ".enc", ".gam", ".gba", ".ics", ".img", ".iso",
        ".mdf", ".mim", ".nes", ".nomedia", ".pak", ".part",
        ".pkpass", ".rom", ".sav", ".stl_game", ".tmp", ".torrent",
        ".uue", ".vcd", ".n64", ".gcz", ".wbfs", ".cso", ".nds",
    },
}