import html
import json
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


PREDICTIONS = [("AI Engineer", 0.91), ("ML Engineer", 0.06), ("Full-stack Developer", 0.03)]


def fetch_languages(user):
    request = urllib.request.Request(
        f"https://api.github.com/users/{user}/repos?per_page=100&type=owner",
        headers={"User-Agent": "training-run-card", "Accept": "application/vnd.github+json"},
    )
    repos = json.loads(urllib.request.urlopen(request, timeout=30).read().decode("utf-8"))
    counts = {}
    for repo in repos:
        language = repo.get("language")
        if language and not repo.get("fork"):
            counts[language] = counts.get(language, 0) + 1
    total = sum(counts.values()) or 1
    return [(name, count / total) for name, count in sorted(counts.items(), key=lambda item: -item[1])][:5]


def probability_bar(x, y, width, share, color, track, delay):
    filled = max(width * share, 4)
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="8" rx="4" fill="{track}"/>'
        f'<rect x="{x}" y="{y}" width="0" height="8" rx="4" fill="{color}">'
        f'<animate attributeName="width" from="0" to="{filled:.1f}" begin="{delay:.2f}s" dur="1.1s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" keyTimes="0;1"/></rect>'
    )


def render_inference(languages, theme):
    colors = THEMES[theme]
    height = 250
    predictions = "".join(
        f'<text x="40" y="{120 + index * 46}" font-family="{SANS}" font-size="{18 if index == 0 else 15}" font-weight="{700 if index == 0 else 400}" fill="{colors["text"] if index == 0 else colors["muted"]}">{label}</text>'
        f'<text x="540" y="{120 + index * 46}" font-family="{MONO}" font-size="14" fill="{colors["text"] if index == 0 else colors["muted"]}" text-anchor="end">p={share:.2f}</text>'
        + probability_bar(40, 132 + index * 46, 500, share, colors["line"] if index == 0 else colors["bar"], colors["grid"], 0.2 + index * 0.25)
        for index, (label, share) in enumerate(PREDICTIONS)
    )
    features = "".join(
        f'<text x="640" y="{120 + index * 34}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">{name}</text>'
        f'<text x="1160" y="{120 + index * 34}" font-family="{MONO}" font-size="13" fill="{colors["text"]}" text-anchor="end">{share:.0%}</text>'
        + probability_bar(800, 112, 300, share, colors["dot"], colors["grid"], 0.6 + index * 0.15).replace('y="112"', f'y="{112 + index * 34}"')
        for index, (name, share) in enumerate(languages)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="{colors["bg"]}" stroke="{colors["border"]}"/>
  <circle cx="28" cy="30" r="5" fill="#ff5f57"/><circle cx="46" cy="30" r="5" fill="#febc2e"/><circle cx="64" cy="30" r="5" fill="#28c840"/>
  <text x="88" y="35" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">&gt;&gt;&gt; model.predict("github.com/{USER}")</text>
  <line x1="0" y1="56" x2="{WIDTH}" y2="56" stroke="{colors["border"]}"/>
  <text x="40" y="84" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">PREDICTED ROLE</text>
  <text x="640" y="84" font-family="{MONO}" font-size="12" fill="{colors["muted"]}" letter-spacing="1.5">INPUT FEATURES · LANGUAGES BY REPOSITORY</text>
  <line x1="600" y1="76" x2="600" y2="{height - 28}" stroke="{colors["border"]}"/>
  {predictions}
  {features}
</svg>
'''


def github_json(path):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"User-Agent": "training-run-card", "Accept": "application/vnd.github+json"},
    )
    return json.loads(urllib.request.urlopen(request, timeout=30).read().decode("utf-8"))


def fetch_recent_work(user, limit=4):
    repos = github_json(f"/users/{user}/repos?per_page=30&sort=pushed&type=owner")
    work = []
    for repo in repos:
        if repo.get("fork") or repo["name"] == user:
            continue
        commits = github_json(f"/repos/{user}/{repo['name']}/commits?per_page=1")
        if not commits:
            continue
        message = commits[0]["commit"]["message"].splitlines()[0]
        pushed = datetime.fromisoformat(commits[0]["commit"]["author"]["date"].replace("Z", "+00:00"))
        work.append((repo["name"], message, pushed))
        if len(work) == limit:
            break
    return work


def ago(moment):
    hours = int((datetime.now(timezone.utc) - moment).total_seconds() // 3600)
    if hours < 24:
        return f"{max(hours, 1)}h ago"
    return f"{hours // 24}d ago"


def clip(text, length):
    text = text if len(text) <= length else text[: length - 1] + "…"
    return html.escape(text, quote=True)


def render_agent(work, theme):
    colors = THEMES[theme]
    lines = [(colors["muted"], f'task: "keep shipping"', "")]
    for repo, message, pushed in work:
        lines.append((colors["dot"], f'→ tool_call  git.log(repo="{clip(repo, 34)}")', ""))
        lines.append((colors["text"], f'  ✓ {clip(message, 62)}', ago(pushed)))
    lines.append((colors["line"], f"✓ done · {len(work)} repositories shipped recently", ""))
    height = 92 + len(lines) * 26 + 20
    rows = "".join(
        f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.3 + index * 0.35:.2f}s" dur="0.25s" fill="freeze"/>'
        f'<text x="40" y="{100 + index * 26}" font-family="{MONO}" font-size="14" fill="{color}">{text}</text>'
        + (f'<text x="1160" y="{100 + index * 26}" font-family="{MONO}" font-size="13" fill="{colors["muted"]}" text-anchor="end">{note}</text>' if note else "")
        + "</g>"
        for index, (color, text, note) in enumerate(lines)
    )
    cursor_y = 100 + (len(lines) - 1) * 26
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="{colors["bg"]}" stroke="{colors["border"]}"/>
  <circle cx="28" cy="30" r="5" fill="#ff5f57"/><circle cx="46" cy="30" r="5" fill="#febc2e"/><circle cx="64" cy="30" r="5" fill="#28c840"/>
  <text x="88" y="35" font-family="{MONO}" font-size="13" fill="{colors["muted"]}">agent.run() · live trace of recent commits</text>
  <line x1="0" y1="56" x2="{WIDTH}" y2="56" stroke="{colors["border"]}"/>
  {rows}
  <rect x="{48 + len(lines[-1][1]) * 8.4:.0f}" y="{cursor_y - 13}" width="8" height="16" fill="{colors["line"]}" opacity="0">
    <animate attributeName="opacity" values="0;1;0" begin="{0.3 + len(lines) * 0.35:.2f}s" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>
'''


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "assets")
    output.mkdir(parents=True, exist_ok=True)
    days = fetch_days(USER)
    languages = fetch_languages(USER)
    work = fetch_recent_work(USER)
    for theme in THEMES:
        (output / f"agent-{theme}.svg").write_text(render_agent(work, theme), encoding="utf-8")
        (output / f"training-run-{theme}.svg").write_text(render(days, theme), encoding="utf-8")
        (output / f"inference-{theme}.svg").write_text(render_inference(languages, theme), encoding="utf-8")


if __name__ == "__main__":
    main()
