import re
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

USER = "vadimtkacj1"
WIDTH, HEIGHT = 1200, 360
PLOT_LEFT, PLOT_TOP, PLOT_WIDTH, PLOT_HEIGHT = 56, 92, 760, 210

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

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, Segoe UI, Helvetica, Arial, sans-serif"


def fetch_days(user):
    request = urllib.request.Request(
        f"https://github.com/users/{user}/contributions",
        headers={"User-Agent": "training-run-card"},
    )
    html = urllib.request.urlopen(request, timeout=30).read().decode("utf-8")
    dates = dict(re.findall(r'data-date="([0-9-]+)"[^>]*id="([^"]+)"', html))
    cell_to_date = {cell: day for day, cell in dates.items()}
    counts = {}
    for cell, label in re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]*)', html):
        if cell not in cell_to_date:
            continue
        match = re.match(r"([0-9,]+) contribution", label)
        counts[cell_to_date[cell]] = int(match.group(1).replace(",", "")) if match else 0
    return sorted((date.fromisoformat(day), count) for day, count in counts.items())


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
    best_week = max(weeks) if weeks else 0
    return [
        ("epochs", f"{len(weeks)}"),
        ("contributions", f"{sum(count for _, count in days):,}"),
        ("active days", f"{sum(1 for _, count in days if count > 0)}"),
        ("best epoch", f"{best_week}"),
        ("longest streak", f"{longest_streak(days)} d"),
        ("current streak", f"{current_streak(days)} d"),
    ]


def plot_points(values, peak):
    step = PLOT_WIDTH / max(len(values) - 1, 1)
    return [
        (PLOT_LEFT + index * step, PLOT_TOP + PLOT_HEIGHT - (value / peak) * PLOT_HEIGHT)
        for index, value in enumerate(values)
    ]


def render(days, theme):
    colors = THEMES[theme]
    weeks = weekly_totals(days)
    peak = max(max(weeks, default=1), 1) * 1.15
    smoothed = ema(weeks)
    points = plot_points(smoothed, peak)
    path = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
    area = path + f" L{points[-1][0]:.1f} {PLOT_TOP + PLOT_HEIGHT} L{PLOT_LEFT} {PLOT_TOP + PLOT_HEIGHT} Z"
    bar_width = PLOT_WIDTH / len(weeks) * 0.55
    bars = "".join(
        f'<rect x="{x - bar_width / 2:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{PLOT_TOP + PLOT_HEIGHT - y:.1f}" rx="1.5" fill="{colors["bar"]}" opacity="0.55"/>'
        for x, y in plot_points(weeks, peak)
    )
    grid = "".join(
        f'<line x1="{PLOT_LEFT}" y1="{PLOT_TOP + PLOT_HEIGHT * fraction:.1f}" x2="{PLOT_LEFT + PLOT_WIDTH}" y2="{PLOT_TOP + PLOT_HEIGHT * fraction:.1f}" stroke="{colors["grid"]}" stroke-dasharray="3 5"/>'
        for fraction in (0, 0.25, 0.5, 0.75, 1)
    )
    last_x, last_y = points[-1]
    rows = "".join(
        f'<text x="880" y="{128 + index * 30}" font-family="{MONO}" font-size="14" fill="{colors["muted"]}">{label}</text>'
        f'<text x="1144" y="{128 + index * 30}" font-family="{MONO}" font-size="14" fill="{colors["text"]}" text-anchor="end" font-weight="600">{value}</text>'
        for index, (label, value) in enumerate(stats(days, weeks))
    )
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{colors["line"]}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="{colors["line"]}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="12" fill="{colors["bg"]}" stroke="{colors["border"]}"/>
  <circle cx="28" cy="30" r="5" fill="#ff5f57"/><circle cx="46" cy="30" r="5" fill="#febc2e"/><circle cx="64" cy="30" r="5" fill="#28c840"/>
  <text x="88" y="35" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">python train.py --model=vadim --data=github --epochs=52</text>
  <line x1="0" y1="56" x2="{WIDTH}" y2="56" stroke="{colors["border"]}"/>
  <text x="{PLOT_LEFT}" y="80" font-family="{SANS}" font-size="15" font-weight="600" fill="{colors["text"]}">Training run · weekly contributions, last 52 weeks</text>
  {grid}
  {bars}
  <path d="{area}" fill="url(#area)" opacity="0">
    <animate attributeName="opacity" from="0" to="1" begin="1.6s" dur="0.8s" fill="freeze"/>
  </path>
  <path d="{path}" fill="none" stroke="{colors["line"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">
    <animate attributeName="stroke-dashoffset" from="1" to="0" dur="2s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" keyTimes="0;1"/>
  </path>
  <circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="5" fill="{colors["bg"]}" stroke="{colors["dot"]}" stroke-width="2.5" opacity="0">
    <animate attributeName="opacity" from="0" to="1" begin="2s" dur="0.3s" fill="freeze"/>
    <animate attributeName="r" values="5;8;5" begin="2.3s" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="{PLOT_LEFT}" y="{PLOT_TOP + PLOT_HEIGHT + 26}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}">epoch 1</text>
  <text x="{PLOT_LEFT + PLOT_WIDTH}" y="{PLOT_TOP + PLOT_HEIGHT + 26}" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" text-anchor="end">epoch {len(weeks)} · now</text>
  <rect x="856" y="76" width="312" height="252" rx="8" fill="{colors["panel"]}" stroke="{colors["border"]}"/>
  <text x="880" y="100" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">METRICS</text>
  {rows}
  <text x="880" y="310" font-family="{MONO}" font-size="11" fill="{colors["muted"]}">checkpoint saved · {updated}</text>
</svg>
'''


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "assets")
    output.mkdir(parents=True, exist_ok=True)
    days = fetch_days(USER)
    for theme in THEMES:
        (output / f"training-run-{theme}.svg").write_text(render(days, theme), encoding="utf-8")


if __name__ == "__main__":
    main()
