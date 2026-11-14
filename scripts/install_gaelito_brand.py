#!/usr/bin/env python3
"""Install the approved Gaelito TV baby mascot into Android resources.

Run from repository root after extracting gaelito_tv_identidad_visual.zip:
    python3 scripts/install_gaelito_brand.py /path/to/extracted/brand

Requires Pillow: python3 -m pip install Pillow
Only modifies visual resources and the launcher resource references.
"""
from pathlib import Path
import re
import sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "app/src/main/res"
MANIFEST = ROOT / "app/src/main/AndroidManifest.xml"

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/install_gaelito_brand.py <brand-folder>")
    folder = Path(sys.argv[1]).resolve()
    icon = folder / "gaelito_tv_icon_512.png"
    banner = folder / "gaelito_tv_banner_1280x720.png"
    if not icon.is_file() or not banner.is_file():
        raise SystemExit("Missing approved Gaelito TV PNGs in supplied folder")
    with Image.open(icon) as src:
        art = src.convert("RGBA")
        for density, size in (("mdpi", 48), ("hdpi", 72), ("xhdpi", 96),
                              ("xxhdpi", 144), ("xxxhdpi", 192)):
            dst = RES / f"mipmap-{density}/gaelito_tv_icon.png"
            dst.parent.mkdir(parents=True, exist_ok=True)
            ImageOps.fit(art, (size, size), method=Image.Resampling.LANCZOS).save(dst)
        splash = RES / "drawable-nodpi/gaelito_tv_splash.png"
        splash.parent.mkdir(parents=True, exist_ok=True)
        art.save(splash)
    with Image.open(banner) as src:
        dst = RES / "drawable-nodpi/gaelito_tv_banner.png"
        src.convert("RGBA").save(dst)

    manifest = MANIFEST.read_text(encoding="utf-8")
    manifest = re.sub(r'android:banner="@drawable/owntv_banner_[^"]+"',
                      'android:banner="@drawable/gaelito_tv_banner"', manifest)
    manifest = re.sub(r'android:(icon|roundIcon)="@mipmap/owntv_icon_[^"]+"',
                      lambda m: f'android:{m.group(1)}="@mipmap/gaelito_tv_icon"', manifest)
    MANIFEST.write_text(manifest, encoding="utf-8")

    # Existing themes are kept so the core icon switcher still works.
    # All launch themes use the same approved mascot still image.
    for path in (RES / "values/themes.xml", RES / "values-v31/themes.xml"):
        if not path.exists():
            continue
        xml = path.read_text(encoding="utf-8")
        xml = re.sub(
            r'(<item name="windowSplashScreenAnimatedIcon">)@drawable/[^<]+(</item>)',
            r'\1@drawable/gaelito_tv_splash\2', xml)
        xml = re.sub(
            r'(<item name="android:windowSplashScreenBrandingImage">)@drawable/[^<]+(</item>)',
            r'\1@drawable/gaelito_tv_banner\2', xml)
        path.write_text(xml, encoding="utf-8")
    print("Gaelito TV visual resources installed. Run ./gradlew assembleStandardDebug to verify.")

if __name__ == "__main__":
    main()
