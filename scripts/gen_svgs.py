"""Generates the animated SVGs for the GitHub profile README.

Usage: python gen_svgs.py <output_dir>
"""
import math
import os
import random
import sys
from xml.sax.saxutils import escape

MONO = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,'DejaVu Sans Mono',Menlo,monospace"
SANS = "'Segoe UI',Inter,'Helvetica Neue',Arial,sans-serif"

BG = "#0d1117"
PURPLE = "#7c3aed"
VIOLET = "#a78bfa"
LAVENDER = "#c4b5fd"
GREEN = "#a3e635"
BLUE = "#60a5fa"
AMBER = "#fbbf24"
WHITE = "#e6edf3"
GRAY = "#8b949e"

REDUCED_MOTION = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def f(x):
    return f"{x:.4f}".rstrip("0").rstrip(".")


def typed_chars(text, start, step, color, total=None, freeze=True):
    """One tspan per character, each revealed in turn (font-width independent)."""
    out = []
    for i, ch in enumerate(text):
        t = start + i * step
        if total is None:
            anim = (f'<set attributeName="fill-opacity" to="1" begin="{f(t)}s" fill="freeze"/>'
                    if freeze else "")
        else:
            k = t / total
            anim = (f'<animate attributeName="fill-opacity" values="0;1;1" keyTimes="0;{f(k)};1" '
                    f'dur="{f(total)}s" calcMode="discrete" repeatCount="indefinite"/>')
        out.append(f'<tspan fill="{color}" fill-opacity="0">{escape(ch)}{anim}</tspan>')
    return "".join(out)


# ---------------------------------------------------------------- header
def header():
    W, H = 1200, 320
    rnd = random.Random(7)
    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
             f'role="img" aria-label="Emir Karabulut: Information Security, Cybersecurity, Developer">')
    s.append(f"""<style>
@keyframes fall{{from{{transform:translateY(-460px)}}to{{transform:translateY(360px)}}}}
@keyframes scan{{from{{transform:translateY(-90px)}}to{{transform:translateY({H}px)}}}}
@keyframes glitchA{{0%,86%,100%{{opacity:0;transform:translate(0,0)}}87%{{opacity:.9;transform:translate(-5px,1px)}}89%{{opacity:.9;transform:translate(4px,-2px)}}91%{{opacity:.8;transform:translate(-2px,2px)}}92%{{opacity:0}}}}
@keyframes glitchB{{0%,86%,100%{{opacity:0;transform:translate(0,0)}}87%{{opacity:.9;transform:translate(5px,-1px)}}89%{{opacity:.9;transform:translate(-4px,2px)}}91%{{opacity:.8;transform:translate(2px,-2px)}}92%{{opacity:0}}}}
@keyframes jitter{{0%,86%,92%,100%{{transform:translate(0,0)}}88%{{transform:translate(2px,0)}}90%{{transform:translate(-2px,0)}}}}
@keyframes border{{from{{stroke-dashoffset:0}}to{{stroke-dashoffset:-3030}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
.rain{{animation:fall linear infinite}}
.scan{{animation:scan 6s linear infinite}}
.ga{{animation:glitchA 5s steps(1) infinite}}
.gb{{animation:glitchB 5s steps(1) infinite .08s}}
.nm{{animation:jitter 5s steps(1) infinite}}
.edge{{animation:border 9s linear infinite}}
.dot{{animation:pulse 1.6s ease-in-out infinite}}
.chip{{opacity:0;animation:rise .5s ease-out forwards}}
.cur{{animation:blink 1s steps(1) infinite}}
{REDUCED_MOTION}
</style>""")
    s.append(f"""<defs>
<radialGradient id="glowL" cx="22%" cy="50%" r="55%"><stop offset="0" stop-color="#3b0764" stop-opacity=".75"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<radialGradient id="glowR" cx="84%" cy="50%" r="30%"><stop offset="0" stop-color="{PURPLE}" stop-opacity=".22"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<linearGradient id="fadeH" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".55" stop-color="#fff" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="1"/></linearGradient>
<mask id="rainMask"><rect width="{W}" height="{H}" fill="url(#fadeH)"/></mask>
<linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0"/><stop offset=".85" stop-color="{VIOLET}" stop-opacity=".09"/><stop offset="1" stop-color="{LAVENDER}" stop-opacity=".25"/></linearGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{PURPLE}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0"/><stop offset="1" stop-color="{VIOLET}" stop-opacity=".45"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{VIOLET}" stroke-opacity=".06"/></pattern>
<clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
<clipPath id="subClip"><rect x="60" y="180" height="44" width="0"><animate attributeName="width" from="0" to="760" begin="1.7s" dur="1.4s" fill="freeze"/></rect></clipPath>
</defs>""")
    s.append('<g clip-path="url(#card)">')
    s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#glowL)"/><rect width="{W}" height="{H}" fill="url(#glowR)"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')

    # binary/hex rain
    glyphs = "0123456789ABCDEF<>/{}[]#$%*+=;:"
    s.append(f'<g mask="url(#rainMask)" font-family="{MONO}" font-size="14">')
    for x in range(14, W, 26):
        n = rnd.randint(9, 17)
        dur = rnd.uniform(7, 15)
        delay = -rnd.uniform(0, dur)
        op = rnd.uniform(.10, .26)
        spans = []
        for i in range(n):
            ch = escape(rnd.choice(glyphs))
            head = i == n - 1
            fill = LAVENDER if head else VIOLET
            fo = "1" if head else f(.25 + .75 * i / n)
            spans.append(f'<tspan x="{x}" dy="20" fill="{fill}" fill-opacity="{fo}">{ch}</tspan>')
        s.append(f'<text class="rain" opacity="{f(op)}" style="animation-duration:{f(dur)}s;animation-delay:{f(delay)}s">{"".join(spans)}</text>')
    s.append("</g>")
    s.append(f'<rect class="scan" width="{W}" height="90" fill="url(#scanG)"/>')

    # typed boot line
    prompt = "waqkin@kali:~$ "
    cmd = "./init --profile"
    s.append(f'<text x="60" y="78" font-family="{MONO}" font-size="16" xml:space="preserve">'
             f'<tspan fill="{GREEN}">{prompt}</tspan>'
             f'{typed_chars(cmd, 0.4, 0.055, WHITE)}'
             f'<tspan class="cur" fill="{VIOLET}">█</tspan></text>')

    # glitching name
    name = "EMİR KARABULUT"
    common = f'x="58" y="160" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="3"'
    s.append(f'<text class="ga" {common} fill="#22d3ee">{name}</text>')
    s.append(f'<text class="gb" {common} fill="#f472b6">{name}</text>')
    s.append(f'<text class="nm" {common} fill="#ffffff">{name}</text>')
    s.append(f'<rect x="60" y="176" height="3" rx="1.5" width="0" fill="url(#bar)">'
             f'<animate attributeName="width" from="0" to="320" begin="1.2s" dur=".8s" fill="freeze"/></rect>')
    s.append(f'<text clip-path="url(#subClip)" x="60" y="214" font-family="{SANS}" font-size="23" fill="{LAVENDER}">'
             f'Information Security  ·  Cybersecurity  ·  Developer</text>')

    # status chips
    chips = [("● ONLINE", GREEN, True), ("ISTANBUL, TR", GRAY, False), ("PENTEST", VIOLET, False),
             ("NETWORK SEC", VIOLET, False), ("ISO 27001", VIOLET, False), ("AI TOOLING", VIOLET, False)]
    x = 60
    for i, (label, color, live) in enumerate(chips):
        w = len(label) * 8.4 + 26
        s.append(f'<g class="chip" style="animation-delay:{f(2.9 + i * .12)}s">'
                 f'<rect x="{f(x)}" y="246" width="{f(w)}" height="28" rx="14" fill="{color}" fill-opacity=".08" stroke="{color}" stroke-opacity=".45"/>')
        if live:
            s.append(f'<text x="{f(x + w / 2)}" y="265" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{color}">'
                     f'<tspan class="dot">●</tspan> ONLINE</text></g>')
        else:
            s.append(f'<text x="{f(x + w / 2)}" y="265" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{color}">{escape(label)}</text></g>')
        x += w + 10

    # radar
    cx, cy, R, T = 1010, 158, 118, 4.0
    s.append(f'<g stroke="{VIOLET}" fill="none">')
    for r, o in ((R, .45), (R * 2 / 3, .3), (R / 3, .25)):
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{f(r)}" stroke-opacity="{o}"/>')
    s.append(f'<path d="M{cx - R} {cy}H{cx + R}M{cx} {cy - R}V{cy + R}" stroke-opacity=".18"/></g>')
    a = math.radians(-55)
    ex, ey = cx + R * math.cos(a), cy + R * math.sin(a)
    s.append(f'<g><path d="M{cx} {cy}L{cx + R} {cy}A{R} {R} 0 0 0 {f(ex)} {f(ey)}Z" fill="url(#sweep)"/>'
             f'<line x1="{cx}" y1="{cy}" x2="{cx + R}" y2="{cy}" stroke="{LAVENDER}" stroke-width="2" stroke-opacity=".9"/>'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="{T}s" repeatCount="indefinite"/></g>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{LAVENDER}"/>')
    blips = [(35, 72, "WNSpace"), (138, 96, "Cybersectr"), (218, 58, "WaqOS"), (302, 98, "HomeLab")]
    for deg, r, label in blips:
        bx = cx + r * math.cos(math.radians(deg))
        by = cy + r * math.sin(math.radians(deg))
        begin = deg / 360 * T
        fade = (f'<animate attributeName="opacity" values="1;.85;.15;0" keyTimes="0;.25;.85;1" '
                f'dur="{T}s" begin="{f(begin)}s" repeatCount="indefinite"/>')
        s.append(f'<g opacity="0">{fade}'
                 f'<circle cx="{f(bx)}" cy="{f(by)}" r="4" fill="{GREEN}"/>'
                 f'<circle cx="{f(bx)}" cy="{f(by)}" r="4" fill="none" stroke="{GREEN}">'
                 f'<animate attributeName="r" values="4;14" dur="{T}s" begin="{f(begin)}s" repeatCount="indefinite"/></circle>'
                 f'<text x="{f(bx + 9)}" y="{f(by - 7)}" font-family="{MONO}" font-size="11" fill="{LAVENDER}">{label}</text></g>')
    s.append(f'<text x="{cx}" y="300" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{GRAY}">'
             f'// scanning active projects</text>')

    s.append("</g>")
    s.append(f'<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="none" stroke="{VIOLET}" stroke-opacity=".25"/>')
    s.append(f'<rect class="edge" x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="none" stroke="{LAVENDER}" stroke-width="2" stroke-dasharray="180 2850" stroke-linecap="round"/>')
    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------- network map
def network():
    W, H = 1200, 600
    cx, cy, RX, RY = 600, 296, 310, 172
    rnd = random.Random(11)

    skills = [("pt", "Penetration Testing", -90), ("ns", "Network Security", -30),
              ("hl", "Linux & Home Lab", 30), ("grc", "GRC · ISO 27001", 90),
              ("web", "Web Development", 150), ("ai", "AI Tooling", 210)]
    projects = [("cs", "Cybersectr", "security news & CVEs", (1056, 112)),
                ("hs", "Home Server", "control center", (1056, 482)),
                ("wq", "WaqOS", "developer workspace", (144, 482)),
                ("wn", "WNSpace", "local AI team office", (144, 112))]
    pos = {"me": (cx, cy)}
    label = {"me": "Emir Karabulut"}
    for key, text, deg in skills:
        a = math.radians(deg)
        pos[key] = (cx + RX * math.cos(a), cy + RY * math.sin(a))
        label[key] = text
    for key, text, _, xy in projects:
        pos[key] = xy
        label[key] = text

    edges = [("me", k) for k, _, _ in skills] + [
        ("pt", "cs"), ("ns", "cs"), ("hl", "hs"), ("ns", "hs"), ("grc", "hs"),
        ("web", "wq"), ("ai", "wq"), ("ai", "wn"), ("web", "wn")]

    # nodes light up one after another, like a scan walking the map
    order = ["me"] + [k for k, _, _ in skills] + [k for k, _, _, _ in projects]
    slot = 0.9
    T = len(order) * slot + 1.2

    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
             f'aria-label="Network map: Emir Karabulut connected to Penetration Testing, Network Security, Linux and Home Lab, '
             f'GRC and ISO 27001, Web Development and AI Tooling, and to the projects Cybersectr, Home Server, WaqOS and WNSpace">')
    s.append(f"""<style>
@keyframes border{{from{{stroke-dashoffset:0}}to{{stroke-dashoffset:-3530}}}}
@keyframes orbit{{from{{stroke-dashoffset:0}}to{{stroke-dashoffset:-240}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.edge{{animation:border 10s linear infinite}}
.orbit{{animation:orbit 6s linear infinite}}
.dot{{animation:pulse 1.6s ease-in-out infinite}}
{REDUCED_MOTION}
</style>""")
    s.append(f"""<defs>
<radialGradient id="nglow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#3b0764" stop-opacity=".7"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<radialGradient id="core" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="{VIOLET}"/><stop offset=".6" stop-color="{PURPLE}"/><stop offset="1" stop-color="#3b0764"/></radialGradient>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{VIOLET}" fill-opacity=".14"/></pattern>
<clipPath id="ncard"><rect width="{W}" height="{H}" rx="16"/></clipPath>
</defs>""")
    s.append('<g clip-path="url(#ncard)">')
    s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/><rect width="{W}" height="{H}" fill="url(#dots)"/>')
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="560" ry="300" fill="url(#nglow)"/>')
    s.append(f'<ellipse class="orbit" cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="none" stroke="{VIOLET}" stroke-opacity=".22" stroke-dasharray="4 8"/>')
    s.append(f'<ellipse class="orbit" cx="{cx}" cy="{cy}" rx="{RX + 150}" ry="{RY + 110}" fill="none" stroke="{VIOLET}" '
             f'stroke-opacity=".08" stroke-dasharray="2 10" style="animation-direction:reverse"/>')

    # links
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        core = a == "me"
        dash = "" if core else ' stroke-dasharray="6 5"'
        s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{VIOLET}" '
                 f'stroke-opacity="{".4" if core else ".22"}" stroke-width="{"1.6" if core else "1.2"}"{dash}/>')

    # packets travelling along links, both directions
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        length = math.hypot(x2 - x1, y2 - y1)
        for forward in (True, False):
            p = f"M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}" if forward else f"M{f(x2)} {f(y2)}L{f(x1)} {f(y1)}"
            dur = max(1.8, min(5.0, length / rnd.uniform(90, 140)))
            begin = -rnd.uniform(0, dur)
            color = LAVENDER if forward else GREEN
            s.append(f'<g opacity="0"><circle r="7" fill="{color}" fill-opacity=".18"/><circle r="2.8" fill="{color}"/>'
                     f'<animateMotion path="{p}" dur="{f(dur)}s" begin="{f(begin)}s" repeatCount="indefinite"/>'
                     f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.88;1" dur="{f(dur)}s" '
                     f'begin="{f(begin)}s" repeatCount="indefinite"/></g>')

    def halo(i, shape):
        return (f'<g opacity="0">{shape}<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.015;.065;.11" '
                f'dur="{f(T)}s" begin="{f(i * slot)}s" repeatCount="indefinite"/></g>')

    # skill nodes
    for key, text, _ in skills:
        x, y = pos[key]
        w = len(text) * 8.6 + 38
        i = order.index(key)
        s.append(halo(i, f'<rect x="{f(x - w / 2 - 6)}" y="{f(y - 23)}" width="{f(w + 12)}" height="46" rx="23" '
                         f'fill="{VIOLET}" fill-opacity=".14" stroke="{LAVENDER}" stroke-width="2"/>'))
        s.append(f'<rect x="{f(x - w / 2)}" y="{f(y - 17)}" width="{f(w)}" height="34" rx="17" fill="#120d1f" stroke="{VIOLET}" stroke-opacity=".7"/>')
        s.append(f'<text x="{f(x)}" y="{f(y + 5)}" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{WHITE}">{escape(text)}</text>')

    # project nodes
    for key, text, sub, (x, y) in projects:
        w, h = 200, 60
        i = order.index(key)
        s.append(halo(i, f'<rect x="{x - w / 2 - 6}" y="{y - h / 2 - 6}" width="{w + 12}" height="{h + 12}" rx="14" '
                         f'fill="{GREEN}" fill-opacity=".08" stroke="{GREEN}" stroke-width="2"/>'))
        s.append(f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="10" fill="#0f1a12" stroke="{GREEN}" stroke-opacity=".55"/>')
        s.append(f'<text x="{x - w / 2 + 16}" y="{y - 4}" font-family="{SANS}" font-size="16" font-weight="700" fill="{WHITE}">◆ {escape(text)}</text>')
        s.append(f'<text x="{x - w / 2 + 16}" y="{y + 17}" font-family="{MONO}" font-size="11.5" fill="{GRAY}">{escape(sub)}</text>')
        s.append(f'<circle class="dot" cx="{x + w / 2 - 14}" cy="{y - h / 2 + 14}" r="4" fill="{GREEN}"/>')

    # core node with sonar rings
    for begin in (0, 1.5):
        s.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="none" stroke="{LAVENDER}" stroke-width="1.5" stroke-opacity="0">'
                 f'<animate attributeName="r" values="58;150" dur="3s" begin="{begin}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="stroke-opacity" values=".6;0" dur="3s" begin="{begin}s" repeatCount="indefinite"/></circle>')
    s.append(halo(0, f'<circle cx="{cx}" cy="{cy}" r="74" fill="{VIOLET}" fill-opacity=".18"/>'))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="72" fill="none" stroke="{VIOLET}" stroke-opacity=".6" stroke-dasharray="3 9">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="24s" repeatCount="indefinite"/></circle>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)" stroke="{LAVENDER}" stroke-width="2"/>')
    s.append(f'<text x="{cx}" y="{cy + 2}" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="800" fill="#fff" letter-spacing="1">EMİR</text>')
    s.append(f'<text x="{cx}" y="{cy + 20}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{LAVENDER}" letter-spacing="2">KARABULUT</text>')

    # captions
    s.append(f'<text x="36" y="40" font-family="{MONO}" font-size="13" fill="{VIOLET}">// NETWORK MAP</text>')
    s.append(f'<text x="{W - 36}" y="40" text-anchor="end" font-family="{MONO}" font-size="12" fill="{GRAY}">'
             f'nodes: {len(order)} · links: {len(edges)} · status: <tspan fill="{GREEN}">secure</tspan></text>')
    for i, key in enumerate(order):
        s.append(f'<text x="36" y="{H - 26}" font-family="{MONO}" font-size="13" opacity="0" xml:space="preserve">'
                 f'<tspan fill="{GRAY}">$ recon --map  › </tspan><tspan fill="{LAVENDER}">{escape(label[key])}</tspan>'
                 f'<tspan fill="{GREEN}">  [ok]</tspan>'
                 f'<animate attributeName="opacity" values="1;0" keyTimes="0;{f(slot / T)}" dur="{f(T)}s" begin="{f(i * slot)}s" '
                 f'calcMode="discrete" repeatCount="indefinite"/></text>')
    s.append(f'<text x="{W - 36}" y="{H - 26}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{GRAY}" xml:space="preserve">'
             f'<tspan fill="{VIOLET}">●</tspan> skill   <tspan fill="{GREEN}">◆</tspan> project   '
             f'<tspan fill="{LAVENDER}">•</tspan> data flow</text>')
    s.append("</g>")
    s.append(f'<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="none" stroke="{VIOLET}" stroke-opacity=".25"/>')
    s.append(f'<rect class="edge" x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="none" stroke="{LAVENDER}" '
             f'stroke-width="2" stroke-dasharray="200 3330" stroke-linecap="round"/>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    for name, fn in (("header.svg", header), ("network.svg", network)):
        with open(os.path.join(out_dir, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(fn())
        print("wrote", name)
