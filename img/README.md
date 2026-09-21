# Image assets

Deployed images in this directory are **derivatives**. The full-resolution
originals live in `img/_src/`, which is git-ignored (they are still in git
history at `c48dfa9` and earlier if you need to recover them).

## Why

The originals totalled ~4.2 MB and were being served at many times their
displayed size — `h-bg.png` alone was 2.5 MB at 1884x1500 for a slot about
660 px wide.

## Regenerating

Requires `cwebp` and `pngquant` (`brew install webp pngquant`).

| Asset            | Target width | Served as                          | Why |
|------------------|--------------|------------------------------------|-----|
| `h-bg`           | 1400         | `.webp` + `.jpg` fallback          | No alpha, so JPEG beats PNG as the fallback |
| `wave-bg`        | 1920         | `.webp` + `.png` fallback (CSS)    | Full-bleed background |
| `pagination`     | 1600         | `.webp` + `.jpg` fallback (CSS)    | Background |
| `ninjalast`      | 1000         | `.png` only                        | pngquant (38 KB) beat WebP (45 KB) |
| `logo`           | 440          | `.png` only                        | pngquant (16 KB) beat WebP (21 KB); displays at 220 px |
| `sword`          | 380          | `.png` only                        | Already tiny |

WebP is only used where it actually wins. For flat-colour artwork with
transparency, a palette-quantised PNG is often smaller — measure, don't assume.

```sh
# WebP
cwebp -q 80 img/_src/h-bg.png -resize 1400 0 -o img/h-bg.webp
# Fallback
sips -s format jpeg -s formatOptions 72 --resampleWidth 1400 img/_src/h-bg.png --out img/h-bg.jpg
# PNG-only assets
sips --resampleWidth 440 img/_src/logo.png --out img/logo.png
pngquant --force --quality=60-88 --output img/logo.png img/logo.png
```

## Favicons

`favicon-32.png`, `favicon-48.png` and `apple-touch-icon.png` (180 px) are
generated from `img/_src/fav.png`, centre-cropped to square. The original
`fav.png` was 242 KB and served as the favicon.
