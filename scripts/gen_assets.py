"""Generate the Claude Code–style SVG assets used in README.md.

Run:  python scripts/gen_assets.py
Writes to assets/claude/.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "claude"

CREAM = "#FAF9F5"
CREAM_2 = "#F0EEE6"
BORDER = "#E3DFD3"
INK = "#1F1E1D"
MUTED = "#6B6862"
CORAL = "#D97757"
CORAL_DARK = "#C15F3C"
FONT = "'JetBrains Mono','SF Mono','Cascadia Code',Menlo,Consolas,'Liberation Mono',monospace"


def svg(w, h, body, title):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<style>text{{font-family:{FONT};}}</style>
{body}
</svg>
"""


def hero():
    w, h = 1200, 330
    lines = [
        (f'<tspan fill="{CORAL}">✻</tspan> <tspan font-weight="700">Kanal Pawadi Piragond</tspan>', 30, INK),
        ("Applied AI Engineer · Generative AI / ML · Full-Stack Developer", 19, MUTED),
    ]
    body = f"""
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{CREAM}" stroke="{BORDER}" stroke-width="2"/>
<path d="M1 19a18 18 0 0 1 18-18h{w-38}a18 18 0 0 1 18 18v27H1z" fill="{CREAM_2}"/>
<line x1="1" y1="46" x2="{w-1}" y2="46" stroke="{BORDER}" stroke-width="2"/>
<circle cx="30" cy="24" r="7" fill="{CORAL}"/>
<circle cx="54" cy="24" r="7" fill="#E5B98F"/>
<circle cx="78" cy="24" r="7" fill="#C9C4B5"/>
<text x="{w/2}" y="29" text-anchor="middle" font-size="14" fill="{MUTED}">kanal@ai-engineer: ~/portfolio</text>

<rect x="48" y="78" width="{w-96}" height="150" rx="10" fill="none" stroke="{CORAL}" stroke-width="1.5"/>
<text x="76" y="128" font-size="{lines[0][1]}" fill="{lines[0][2]}">{lines[0][0]}</text>
<text x="76" y="166" font-size="{lines[1][1]}" fill="{lines[1][2]}">{escape(lines[1][0])}</text>
<text x="76" y="202" font-size="15" fill="{MUTED}">cwd: <tspan fill="{INK}">Sangli, Maharashtra, India</tspan>   ·   CGPA <tspan fill="{INK}">9.04/10</tspan>   ·   B.Tech AI &amp; DS '27</text>

<text x="52" y="270" font-size="18" fill="{INK}"><tspan fill="{CORAL}">&gt;</tspan> building production-grade RAG, NLP &amp; agentic AI systems</text>
<rect x="676" y="254" width="11" height="21" fill="{CORAL}">
  <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/>
</rect>
<text x="52" y="305" font-size="13" fill="{MUTED}">? for shortcuts  ·  open to Applied AI Engineering internships → full-time</text>
"""
    return svg(w, h, body, "Kanal Pawadi Piragond — Applied AI Engineer")


def header(slug, label, comment):
    w, h = 1200, 64
    body = f"""
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="{CREAM}" stroke="{BORDER}" stroke-width="2"/>
<rect x="1" y="1" width="8" height="{h-2}" rx="4" fill="{CORAL}"/>
<text x="34" y="41" font-size="22" font-weight="700" fill="{INK}"><tspan fill="{CORAL}">✻</tspan> {escape(label)}</text>
<text x="{w-30}" y="40" text-anchor="end" font-size="15" fill="{MUTED}"># {escape(comment)}</text>
"""
    (OUT / f"h_{slug}.svg").write_text(svg(w, h, body, label), encoding="utf-8")


def impact():
    tiles = [
        ("30%", "lower RAG latency", "vs. OpenAI baseline"),
        ("100%", "retrieval accuracy", "on dynamic documents"),
        ("35%", "FAQ support", "workload automated"),
        ("22%", "lower MAE", "inventory forecasting"),
        ("0.96 F2", "hazard detection", "530k-report corpus"),
        ("4.6–5.9mm", "RMSE in 3D", "heritage reconstruction"),
    ]
    w, h = 1200, 300
    tw, th, gap = 376, 130, 16
    parts = []
    for i, (big, l1, l2) in enumerate(tiles):
        x = 8 + (i % 3) * (tw + gap)
        y = 12 + (i // 3) * (th + gap)
        parts.append(f"""
<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="12" fill="{CREAM}" stroke="{BORDER}" stroke-width="2"/>
<text x="{x+26}" y="{y+56}" font-size="34" font-weight="700" fill="{CORAL}">{escape(big)}</text>
<text x="{x+26}" y="{y+88}" font-size="16" fill="{INK}">{escape(l1)}</text>
<text x="{x+26}" y="{y+111}" font-size="14" fill="{MUTED}">{escape(l2)}</text>""")
    (OUT / "impact.svg").write_text(svg(w, h, "".join(parts), "Impact at a glance"), encoding="utf-8")


HEADERS = [
    ("about", "about_me", "whoami"),
    ("impact", "impact_at_a_glance", "numbers that shipped"),
    ("experience", "work_experience", "git log --author=kanal"),
    ("projects", "featured_projects", "ls ~/projects"),
    ("achievements", "achievements_and_research", "cat awards.md"),
    ("techstack", "tech_stack", "pip freeze | npm ls"),
    ("stats", "github_analytics", "gh api /users/kanalpawadi"),
    ("education", "education", "cat transcript.txt"),
    ("certs", "certifications_and_leadership", "ls ~/certs"),
    ("connect", "lets_connect", "ssh kanal@open-to-work"),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "hero.svg").write_text(hero(), encoding="utf-8")
    impact()
    for h in HEADERS:
        header(*h)
    print("wrote", len(list(OUT.glob("*.svg"))), "files to", OUT)
