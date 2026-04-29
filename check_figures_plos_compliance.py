"""
PLOS ONE figure compliance checker for figures_tif/.

Requirements (per https://journals.plos.org/plosone/s/figures, 2024-2025):
  - Format: TIFF or EPS (TIFF preferred for raster)
  - File size: max 10 MB per figure
  - Width: 789-2250 px (1.04-7.5 inch at 300 DPI; double-column = 2250)
  - Height: max 2625 px (8.75 inch at 300 DPI)
  - Resolution: 300-600 DPI for halftone, 600-1200 for line art
  - Color mode: RGB (sRGB IEC61966-2.1 profile preferred)
  - Bit depth: 8 bit per channel (24-bit RGB) or higher
  - Compression: LZW for TIFF (preferred); ZIP/none acceptable but LZW best
  - Layered files NOT accepted (must be flattened)
  - Fonts: embedded (or rasterized at 600 DPI)
"""
import os
from PIL import Image

FIG_DIR = "/Users/gscott/Dropbox/文件/我的程式/Github/PLOS-BCAT/figures_tif"

PLOS = {
    "max_file_size_mb": 10.0,
    "min_width_px": 789,
    "max_width_px": 2250,
    "max_height_px": 2625,
    "min_dpi": 300,
    "max_dpi": 600,
    "rec_dpi": 300,
}

# Compression code → name (TIFF tag 259)
COMP_NAMES = {
    1: "none (uncompressed)",
    2: "CCITT modified Huffman",
    3: "CCITT T.4",
    4: "CCITT T.6",
    5: "LZW",
    6: "JPEG (old)",
    7: "JPEG",
    8: "Deflate (Adobe ZIP)",
    32773: "PackBits",
    32946: "Deflate (ZIP)",
}


def inspect(path):
    size_bytes = os.path.getsize(path)
    with Image.open(path) as img:
        w, h = img.size
        mode = img.mode
        info = img.info
        raw_dpi = info.get("dpi", (None, None))
        dpi = (
            float(raw_dpi[0]) if raw_dpi[0] is not None else None,
            float(raw_dpi[1]) if raw_dpi[1] is not None else None,
        )
        # Compression tag for TIFF
        compression = None
        if hasattr(img, "tag_v2"):
            compression = img.tag_v2.get(259)
        # Bit depth
        bit_per_sample = None
        if hasattr(img, "tag_v2"):
            bps = img.tag_v2.get(258)
            if bps:
                bit_per_sample = bps if isinstance(bps, int) else tuple(bps)
        # Page count (layers)
        n_frames = getattr(img, "n_frames", 1)
        # ICC profile
        icc = "yes" if info.get("icc_profile") else "no"
    return {
        "path": path,
        "name": os.path.basename(path),
        "size_mb": size_bytes / 1024 / 1024,
        "width": w,
        "height": h,
        "mode": mode,
        "dpi": dpi,
        "compression_code": compression,
        "compression_name": COMP_NAMES.get(compression, f"unknown ({compression})"),
        "bit_per_sample": bit_per_sample,
        "n_frames": n_frames,
        "icc_profile": icc,
    }


def check_compliance(r):
    issues = []
    warnings = []

    # File size
    if r["size_mb"] > PLOS["max_file_size_mb"]:
        issues.append(f"file size {r['size_mb']:.2f} MB > 10 MB")

    # Width
    if r["width"] < PLOS["min_width_px"]:
        issues.append(f"width {r['width']} px < {PLOS['min_width_px']} (min)")
    if r["width"] > PLOS["max_width_px"]:
        issues.append(f"width {r['width']} px > {PLOS['max_width_px']} (max)")

    # Height
    if r["height"] > PLOS["max_height_px"]:
        issues.append(f"height {r['height']} px > {PLOS['max_height_px']} (max)")

    # DPI
    dpi_x, dpi_y = r["dpi"]
    if dpi_x is None:
        warnings.append("DPI metadata absent (PLOS may auto-default to 72 — verify)")
    else:
        if dpi_x < PLOS["min_dpi"]:
            issues.append(f"DPI {dpi_x:.0f} < {PLOS['min_dpi']}")
        if dpi_x > PLOS["max_dpi"] * 2:
            warnings.append(f"DPI {dpi_x:.0f} unusually high (>1200)")

    # Color mode
    if r["mode"] not in ("RGB", "L"):
        issues.append(f"color mode '{r['mode']}' (PLOS expects RGB; L = grayscale OK)")

    # Compression
    if r["compression_code"] == 1:
        warnings.append("uncompressed TIFF (PLOS prefers LZW; size may inflate)")
    elif r["compression_code"] not in (5, 8, 32946, 32773):
        warnings.append(f"compression '{r['compression_name']}' (PLOS prefers LZW)")

    # Bit depth
    if r["bit_per_sample"] and isinstance(r["bit_per_sample"], (tuple, list)):
        if any(b < 8 for b in r["bit_per_sample"]):
            issues.append(f"bit depth {r['bit_per_sample']} < 8 per channel")
    elif r["bit_per_sample"] and r["bit_per_sample"] < 8:
        issues.append(f"bit depth {r['bit_per_sample']} < 8")

    # Multi-page (layers)
    if r["n_frames"] > 1:
        issues.append(f"{r['n_frames']} frames/layers (PLOS needs flattened single image)")

    return issues, warnings


# ---- Run ----
files = sorted([f for f in os.listdir(FIG_DIR) if f.lower().endswith((".tif", ".tiff"))])
results = [inspect(os.path.join(FIG_DIR, f)) for f in files]

# Print specs table
print("=" * 130)
print(f"{'File':<12} {'Size MB':>8} {'WxH (px)':>14} {'Inch@300':>11} "
      f"{'Mode':>5} {'Bits':>5} {'DPI':>10} {'Compression':<22} {'Frames':>6} {'ICC':>4}")
print("=" * 130)
for r in results:
    dpi_str = f"{r['dpi'][0]:.0f}x{r['dpi'][1]:.0f}" if r['dpi'][0] else "?"
    inch_str = f"{r['width']/300:.2f}x{r['height']/300:.2f}" if r['dpi'][0] else "?"
    bps = r['bit_per_sample']
    bps_str = str(bps[0]) if isinstance(bps, (tuple, list)) else str(bps)
    wh = f"{r['width']}x{r['height']}"
    print(f"{r['name']:<12} {r['size_mb']:>8.2f} {wh:>14} "
          f"{inch_str:>11} {r['mode']:>5} {bps_str:>5} {dpi_str:>10} "
          f"{r['compression_name']:<22} {r['n_frames']:>6} {r['icc_profile']:>4}")

# Print PLOS specs reference
print("\n" + "=" * 130)
print("PLOS ONE figure specs (from https://journals.plos.org/plosone/s/figures):")
print(f"  - File size:    ≤ 10 MB")
print(f"  - Width:        789–2250 px  (1.04–7.5 in @ 300 DPI; double-column = 2250)")
print(f"  - Height:       ≤ 2625 px    (≤ 8.75 in @ 300 DPI)")
print(f"  - DPI:          300 minimum (300–600 typical)")
print(f"  - Color mode:   RGB (sRGB profile preferred); grayscale (L) acceptable for line art")
print(f"  - Bit depth:    8 per channel (24-bit RGB)")
print(f"  - Compression:  LZW preferred for TIFF")
print(f"  - Frames:       1 (must be flattened, no layers)")

# Per-file compliance
print("\n" + "=" * 130)
print("Per-file compliance:")
print("=" * 130)
all_pass = True
all_warn = False
for r in results:
    issues, warnings = check_compliance(r)
    if issues:
        all_pass = False
        print(f"❌ {r['name']:<12}  ISSUES:    {'; '.join(issues)}")
        if warnings:
            print(f"   {' ':<12}  warnings:  {'; '.join(warnings)}")
    elif warnings:
        all_warn = True
        print(f"⚠  {r['name']:<12}  warnings:  {'; '.join(warnings)}")
    else:
        print(f"✓  {r['name']:<12}  PASS")

print("\n" + "=" * 130)
if all_pass and not all_warn:
    print("OVERALL: ALL FILES PASS PLOS ONE FIGURE SPECS")
elif all_pass:
    print("OVERALL: ALL FILES PASS hard requirements; some have soft warnings (see above)")
else:
    print("OVERALL: ONE OR MORE FILES HAVE ISSUES — fix before upload")

# Also note: graphical_abstract.jpg
print("\n" + "=" * 130)
print("NOTE: graphical_abstract.jpg is NOT a journal-submission figure (PLOS ONE has no GA workflow).")
print("It is for personal/promotional use only and does not need to meet these specs.")
