import html
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

USER = "vadimtkacj1"
WIDTH = 1200
EDGE = 40
PLOT_LEFT, PLOT_TOP, PLOT_WIDTH, PLOT_HEIGHT = EDGE, 92, 776, 200

SHOWCASE = [
    "hybrid-recommendation-system-diplom",
    "fine-tuning-llama",
    "real-estate-appraisal-agent",
    "clip-retrieval-ai",
    "vessel-segmentation",
    "brain-tumour-segmentation",
    "mindEasy-llm-chat-bot",
]

LAYERS = [
    ("core", "Input", [("Python", "python"), ("NumPy", "numpy"), ("pandas", "pandas"), ("Jupyter", "jupyter"), ("Git", "git"), ("Linux", "linux")]),
    ("llm", "Adapter", [("Transformers", "huggingface"), ("PEFT / LoRA", None), ("bitsandbytes", None), ("OpenAI", "openai"), ("Claude", "claude"), ("Gemini", "googlegemini")]),
    ("vision", "Encoder", [("PyTorch", "pytorch"), ("segmentation-models", None), ("OpenCV", "opencv"), ("CLIP", "openai"), ("Albumentations", None)]),
    ("ranking", "Hybrid", [("scikit-learn", "scikitlearn"), ("implicit ALS", None), ("sentence-transformers", "huggingface"), ("XGBoost", None)]),
    ("serving", "Head", [("FastAPI", "fastapi"), ("Docker", "docker"), ("PostgreSQL", "postgresql"), ("SQLite", "sqlite"), ("nginx", "nginx"), ("GitHub Actions", "githubactions")]),
    ("product", "Interface", [("TypeScript", "typescript"), ("React", "react"), ("Next.js", "nextdotjs"), ("Tailwind CSS", "tailwindcss")]),
]

ICONS = json.loads((Path(__file__).parent / "icons.json").read_text(encoding="utf-8"))

THEMES = {
    "dark": {
        "bg": "#0d1117", "panel": "#161b22", "border": "#30363d", "grid": "#21262d",
        "text": "#e6edf3", "muted": "#8b949e", "bar": "#1f6feb", "line": "#3fb950", "dot": "#58a6ff",
    },
    "light": {
        "bg": "#ffffff", "panel": "#f6f8fa", "border": "#d0d7de", "grid": "#eaeef2",
        "text": "#1f2328", "muted": "#59636e", "bar": "#b6d4fe", "line": "#1a7f37", "dot": "#0969da",
    },
}

SKYLINE_START = "<!-- skyline:start -->"
SKYLINE_END = "<!-- skyline:end -->"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, Segoe UI, Helvetica, Arial, sans-serif"
MONO_CHAR = 7.4


def request(url, accept="application/vnd.github+json"):
    headers = {"User-Agent": "profile-cards", "Accept": accept}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com"):
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30).read().decode("utf-8")


def github_json(path):
    return json.loads(request(f"https://api.github.com{path}"))


def fetch_days(user):
    page = request(f"https://github.com/users/{user}/contributions", accept="text/html")
    dates = dict(re.findall(r'data-date="([0-9-]+)"[^>]*id="([^"]+)"', page))
    cell_to_date = {cell: day for day, cell in dates.items()}
    counts = {}
    for cell, label in re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]*)', page):
        if cell not in cell_to_date:
            continue
        match = re.match(r"([0-9,]+) contribution", label)
        counts[cell_to_date[cell]] = int(match.group(1).replace(",", "")) if match else 0
    return sorted((date.fromisoformat(day), count) for day, count in counts.items())


def fetch_recent_work(user, limit=4):
    work = []
    for repo in SHOWCASE:
        commits = github_json(f"/repos/{user}/{repo}/commits?per_page=1")
        if not commits:
            continue
        commit = commits[0]["commit"]
        moment = datetime.fromisoformat(commit["author"]["date"].replace("Z", "+00:00"))
        work.append((repo, commit["message"].splitlines()[0], moment))
    return sorted(work, key=lambda item: item[2], reverse=True)[:limit]


def weekly_totals(days):
    weeks = {}
    for day, count in days:
        key = day.isocalendar()[:2]
        weeks[key] = weeks.get(key, 0) + count
    return [weeks[key] for key in sorted(weeks)][-52:]


def ema(values, alpha=0.3):
    smoothed, current = [], values[0] if values else 0
    for value in values:
        current = alpha * value + (1 - alpha) * current
        smoothed.append(current)
    return smoothed


def current_streak(days):
    streak = 0
    for index, (_, count) in enumerate(reversed(days)):
        if count > 0:
            streak += 1
        elif index > 0:
            break
    return streak


def longest_streak(days):
    best = run = 0
    for _, count in days:
        run = run + 1 if count > 0 else 0
        best = max(best, run)
    return best


def stats(days, weeks):
    return [
        ("epochs", f"{len(weeks)}"),
        ("contributions", f"{sum(count for _, count in days):,}"),
        ("active days", f"{sum(1 for _, count in days if count > 0)}"),
        ("best epoch", f"{max(weeks, default=0)}"),
        ("longest streak", f"{longest_streak(days)} d"),
        ("current streak", f"{current_streak(days)} d"),
    ]


def escape(text, length=None):
    if length and len(text) > length:
        text = text[: length - 1] + "…"
    return html.escape(text, quote=True)


def frame(title, height, colors, note=""):
    return (
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="{colors["bg"]}" stroke="{colors["border"]}"/>'
        f'<text x="{EDGE}" y="36" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">{title}</text>'
        + (f'<text x="{WIDTH - EDGE}" y="36" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" text-anchor="end">{note}</text>' if note else "")
        + f'<line x1="0" y1="56" x2="{WIDTH}" y2="56" stroke="{colors["border"]}"/>'
    )


def svg(height, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">'
        f"{defs}{body}</svg>\n"
    )


def plot_points(values, peak):
    step = PLOT_WIDTH / max(len(values) - 1, 1)
    return [
        (PLOT_LEFT + index * step, PLOT_TOP + PLOT_HEIGHT - (value / peak) * PLOT_HEIGHT)
        for index, value in enumerate(values)
    ]


def render_training(days, theme):
    colors = THEMES[theme]
    height = 344
    weeks = weekly_totals(days)
    peak = max(max(weeks, default=1), 1) * 1.18
    points = plot_points(ema(weeks), peak)
    raw_points = plot_points(weeks, peak)
    path = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
    floor = PLOT_TOP + PLOT_HEIGHT
    area = path + f" L{points[-1][0]:.1f} {floor} L{PLOT_LEFT} {floor} Z"
    bar_width = PLOT_WIDTH / len(weeks) * 0.55
    bars = "".join(
        f'<rect x="{x - bar_width / 2:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{floor - y:.1f}" rx="1.5" fill="{colors["bar"]}" opacity="0.5"/>'
        for x, y in raw_points
    )
    grid = "".join(
        f'<line x1="{PLOT_LEFT}" y1="{PLOT_TOP + PLOT_HEIGHT * fraction:.1f}" x2="{PLOT_LEFT + PLOT_WIDTH}" y2="{PLOT_TOP + PLOT_HEIGHT * fraction:.1f}" stroke="{colors["grid"]}" stroke-dasharray="3 5"/>'
        for fraction in (0, 0.25, 0.5, 0.75, 1)
    )
    best_index = max(range(len(weeks)), key=lambda index: weeks[index])
    best_x, best_y = raw_points[best_index]
    label_anchor = "end" if best_x > PLOT_LEFT + PLOT_WIDTH - 120 else "start"
    label_x = best_x - 10 if label_anchor == "end" else best_x + 10
    last_x, last_y = points[-1]
    panel_x = PLOT_LEFT + PLOT_WIDTH + 32
    panel_width = WIDTH - EDGE - panel_x
    rows = "".join(
        f'<text x="{panel_x + 20}" y="{120 + index * 30}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">{label}</text>'
        f'<text x="{panel_x + panel_width - 20}" y="{120 + index * 30}" font-family="{MONO}" font-size="15" font-weight="600" fill="{colors["text"]}" text-anchor="end">{value}</text>'
        for index, (label, value) in enumerate(stats(days, weeks))
    )
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    defs = (
        f'<defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{colors["line"]}" stop-opacity="0.26"/>'
        f'<stop offset="1" stop-color="{colors["line"]}" stop-opacity="0"/></linearGradient></defs>'
    )
    body = (
        frame("TRAINING RUN · WEEKLY CONTRIBUTIONS · LAST 52 WEEKS", height, colors, f"updated {updated}")
        + grid
        + bars
        + f'<path d="{area}" fill="url(#area)" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1.6s" dur="0.8s" fill="freeze"/></path>'
        + f'<path d="{path}" fill="none" stroke="{colors["line"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">'
        f'<animate attributeName="stroke-dashoffset" from="1" to="0" dur="2s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" keyTimes="0;1"/></path>'
        + f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="2.1s" dur="0.4s" fill="freeze"/>'
        f'<circle cx="{best_x:.1f}" cy="{best_y:.1f}" r="4" fill="{colors["dot"]}"/>'
        f'<text x="{label_x:.1f}" y="{best_y + 4:.1f}" font-family="{MONO}" font-size="12" fill="{colors["text"]}" text-anchor="{label_anchor}">peak · {weeks[best_index]}</text></g>'
        + f'<circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="5" fill="{colors["bg"]}" stroke="{colors["line"]}" stroke-width="2.5" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" begin="2s" dur="0.3s" fill="freeze"/>'
        f'<animate attributeName="r" values="5;8;5" begin="2.3s" dur="2s" repeatCount="indefinite"/></circle>'
        + f'<text x="{PLOT_LEFT}" y="{floor + 26}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}">epoch 1</text>'
        + f'<text x="{PLOT_LEFT + PLOT_WIDTH}" y="{floor + 26}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" text-anchor="end">epoch {len(weeks)} · now</text>'
        + f'<rect x="{panel_x}" y="80" width="{panel_width}" height="{height - 112}" rx="8" fill="{colors["panel"]}" stroke="{colors["border"]}"/>'
        + rows
    )
    return svg(height, body, defs)


def luminance(hex_color):
    channels = [int(hex_color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def icon_color(slug, theme, colors):
    brand = ICONS[slug]["hex"]
    if theme == "dark" and luminance(brand) < 0.08:
        return colors["text"]
    if theme == "light" and luminance(brand) > 0.45:
        return "#" + "".join(f"{int(int(brand[index:index + 2], 16) * 0.72):02x}" for index in (1, 3, 5))
    return brand


def icon_symbols(theme, colors):
    slugs = sorted({slug for _, _, tools in LAYERS for _, slug in tools if slug})
    return "".join(
        f'<symbol id="{slug}" viewBox="0 0 24 24"><path d="{ICONS[slug]["path"]}" fill="{icon_color(slug, theme, colors)}"/></symbol>'
        for slug in slugs
    )


def chip(x, y, label, slug, colors):
    width = 10 + 14 + 7 + len(label) * MONO_CHAR + 12
    glyph = (
        f'<use href="#{slug}" x="{x + 10:.1f}" y="{y - 11}" width="14" height="14"/>'
        if slug
        else f'<circle cx="{x + 17:.1f}" cy="{y - 4}" r="3" fill="{colors["muted"]}"/>'
    )
    return width, (
        f'<rect x="{x:.1f}" y="{y - 17}" width="{width:.1f}" height="26" rx="13" fill="{colors["panel"]}" stroke="{colors["border"]}"/>'
        + glyph
        + f'<text x="{x + 31:.1f}" y="{y}" font-family="{MONO}" font-size="12" fill="{colors["text"]}">{escape(label)}</text>'
    )


def render_stack(theme):
    colors = THEMES[theme]
    header_y, top, row_height = 88, 134, 48
    rows = []
    for index, (name, kind, tools) in enumerate(LAYERS):
        y = top + index * row_height
        x = 270
        chips = []
        for label, slug in tools:
            width, markup = chip(x, y, label, slug, colors)
            chips.append(markup)
            x += width + 8
        divider = f'<line x1="{EDGE}" y1="{y + 22}" x2="{WIDTH - EDGE}" y2="{y + 22}" stroke="{colors["grid"]}"/>' if index < len(LAYERS) - 1 else ""
        rows.append(
            f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.2 + index * 0.18:.2f}s" dur="0.35s" fill="freeze"/>'
            f'<text x="{EDGE}" y="{y}" font-family="{MONO}" font-size="15" fill="{colors["text"]}">{name}<tspan fill="{colors["muted"]}" font-size="13"> ({kind})</tspan></text>'
            + "".join(chips)
            + f'<text x="{WIDTH - EDGE}" y="{y}" font-family="{MONO}" font-size="15" fill="{colors["muted"]}" text-anchor="end">{len(tools)}</text>'
            + divider
            + "</g>"
        )
    table_bottom = top + (len(LAYERS) - 1) * row_height + 26
    total = sum(len(tools) for _, _, tools in LAYERS)
    height = table_bottom + 52
    body = (
        frame("STACK · MODEL.SUMMARY()", height, colors)
        + f'<text x="{EDGE}" y="{header_y}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">LAYER (TYPE)</text>'
        + f'<text x="270" y="{header_y}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">COMPONENTS</text>'
        + f'<text x="{WIDTH - EDGE}" y="{header_y}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5" text-anchor="end">PARAMS</text>'
        + f'<line x1="{EDGE}" y1="{header_y + 12}" x2="{WIDTH - EDGE}" y2="{header_y + 12}" stroke="{colors["border"]}"/>'
        + "".join(rows)
        + f'<line x1="{EDGE}" y1="{table_bottom}" x2="{WIDTH - EDGE}" y2="{table_bottom}" stroke="{colors["border"]}"/>'
        + f'<text x="{EDGE}" y="{table_bottom + 30}" font-family="{MONO}" font-size="13" fill="{colors["text"]}">Total params: {total}</text>'
        + f'<text x="{WIDTH - EDGE}" y="{table_bottom + 30}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}" text-anchor="end">Trainable params: {total}</text>'
    )
    return svg(height, body, f"<defs>{icon_symbols(theme, colors)}</defs>")


def ago(moment):
    hours = int((datetime.now(timezone.utc) - moment).total_seconds() // 3600)
    if hours < 24:
        return f"{max(hours, 1)}h ago"
    if hours < 24 * 60:
        return f"{hours // 24}d ago"
    return moment.strftime("%b %Y")


def render_recent(work, theme):
    colors = THEMES[theme]
    top, row_height = 92, 34
    height = top + len(work) * row_height + 14
    rows = "".join(
        f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.2 + index * 0.2:.2f}s" dur="0.35s" fill="freeze"/>'
        f'<circle cx="{EDGE + 4}" cy="{top + index * row_height - 4}" r="4" fill="{colors["line"] if index == 0 else colors["border"]}"/>'
        f'<text x="{EDGE + 20}" y="{top + index * row_height}" font-family="{MONO}" font-size="14" fill="{colors["text"]}">{escape(repo, 30)}</text>'
        f'<text x="340" y="{top + index * row_height}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">{escape(message, 82)}</text>'
        f'<text x="{WIDTH - EDGE}" y="{top + index * row_height}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}" text-anchor="end">{ago(moment)}</text>'
        "</g>"
        for index, (repo, message, moment) in enumerate(work)
    )
    return svg(height, frame("LATEST COMMITS · SHOWCASE REPOSITORIES", height, colors) + rows)


def quad(points, normal):
    a, b, c, d = points
    return [(normal, a, b, c), (normal, a, c, d)]


def box(x, y, z, sx, sy, sz, with_bottom=False):
    x1, y1, z1 = x + sx, y + sy, z + sz
    faces = [
        quad([(x, y, z1), (x1, y, z1), (x1, y1, z1), (x, y1, z1)], (0, 0, 1)),
        quad([(x, y, z), (x1, y, z), (x1, y, z1), (x, y, z1)], (0, -1, 0)),
        quad([(x1, y1, z), (x, y1, z), (x, y1, z1), (x1, y1, z1)], (0, 1, 0)),
        quad([(x, y1, z), (x, y, z), (x, y, z1), (x, y1, z1)], (-1, 0, 0)),
        quad([(x1, y, z), (x1, y1, z), (x1, y1, z1), (x1, y, z1)], (1, 0, 0)),
    ]
    if with_bottom:
        faces.append(quad([(x, y1, z), (x1, y1, z), (x1, y, z), (x, y, z)], (0, 0, -1)))
    return [triangle for face in faces for triangle in face]


def number(value):
    return f"{value:.2f}".rstrip("0").rstrip(".")


def render_skyline(days):
    first = days[0][0]
    start = first.toordinal() - (first.weekday() + 1) % 7
    peak = max(count for _, count in days) or 1
    weeks = (days[-1][0].toordinal() - start) // 7 + 1
    triangles = box(-1, -1, -1.2, weeks + 1.2, 8.2, 1.2, with_bottom=True)
    for day, count in days:
        if count == 0:
            continue
        week = (day.toordinal() - start) // 7
        weekday = (day.weekday() + 1) % 7
        triangles += box(week + 0.1, 6 - weekday + 0.1, 0, 0.8, 0.8, 0.8 + 24 * (count / peak) ** 0.5)
    lines = ["solid contributions"]
    for normal, *vertices in triangles:
        lines.append(f"facet normal {' '.join(number(v) for v in normal)}")
        lines.append("outer loop")
        lines.extend(f"vertex {' '.join(number(v) for v in vertex)}" for vertex in vertices)
        lines.append("endloop")
        lines.append("endfacet")
    lines.append("endsolid contributions")
    return "\n".join(lines)


def replace_between(text, start_marker, end_marker, content):
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker)
    return text[:start] + "\n" + content + "\n" + text[end:]


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "assets")
    output.mkdir(parents=True, exist_ok=True)
    days = fetch_days(USER)
    work = fetch_recent_work(USER)
    for theme in THEMES:
        (output / f"training-run-{theme}.svg").write_text(render_training(days, theme), encoding="utf-8")
        (output / f"stack-{theme}.svg").write_text(render_stack(theme), encoding="utf-8")
        (output / f"recent-{theme}.svg").write_text(render_recent(work, theme), encoding="utf-8")
    readme = output.parent / "README.md"
    text = readme.read_text(encoding="utf-8")
    if SKYLINE_START in text and days:
        skyline = f"```stl\n{render_skyline(days)}\n```"
        readme.write_text(replace_between(text, SKYLINE_START, SKYLINE_END, skyline), encoding="utf-8")


if __name__ == "__main__":
    main()
