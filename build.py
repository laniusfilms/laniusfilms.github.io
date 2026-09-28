"""Update content.json, then run python3 build.py. No packages required."""
import json,html
from pathlib import Path
ROOT=Path(__file__).resolve().parent
c=json.loads((ROOT/'content.json').read_text()); esc=html.escape

def head(title,description):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#0b0d0d"><title>{esc(title)} — Lanius Films</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"></head><body><a class="skip" href="#main">Skip to content</a><header class="container"><a class="brand" href="index.html">LANIUS<span>FILMS</span><i></i></a><nav aria-label="Main navigation"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact ↗</a></nav></header>'''

def footer():return '''<footer class="container"><a class="brand" href="index.html">LANIUS<span>FILMS</span></a><p>Independent visions. Cinematic worlds.</p><span>© 2026 Lanius Films</span></footer></body></html>'''

def image(p,loading='lazy'):return f'<img src="assets/{p["image"]}.jpg" alt="{esc(p["alt"])}" loading="{loading}" decoding="async">'

def action(url,label):
 return f'<a class="button" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{label} ↗</a>' if url else '<span class="pending">Film link coming soon</span>'

def video_actions(p):
 videos=p.get('videos') or ([dict(title='film',url=p['video_url'])] if p.get('video_url') else [])
 if not videos: return action('', '')
 return '<div class="video-actions">'+''.join(action(v['url'],'Watch '+esc(v['title'])) for v in videos)+'</div>'

cards=[]
for i,p in enumerate(c['projects']):
 media=image(p) if p['image'] else '<div class="spec-art"><span>CONCEPT / CREATE / CUT</span><strong>SPEC<span>STUDIES.</span></strong><small>INDEPENDENT COMMERCIAL EXPLORATIONS</small></div>'
 cards.append(f'''<article class="project {'featured' if i==0 else ''} {'portrait' if i in (2,3) else ''}"><a class="media" href="{p['id']}.html" aria-label="Explore {esc(p['title'])}">{media}<span class="media-label">{i+1:02d} / {esc(p['category'])}</span><span class="arrow" aria-hidden="true">↗</span></a><div class="project-text"><div><p class="eyebrow">{esc(p['category'])}</p><h3><a href="{p['id']}.html">{esc(p['title'])}</a></h3></div><p>{esc(p['description'])}</p></div>{video_actions(p) if p.get('videos') else ''}</article>''')
 hero=c['projects'][0]
index=head('AI Filmmaking & Visual Storytelling','Narrative AI films, digital characters and speculative campaigns. Explore the cinematic worlds of Lanius Films.')+f'''
<main id="main"><section class="hero"><img class="hero-image" src="assets/passenger.jpg" alt="" fetchpriority="high"><div class="hero-shade"></div><div class="container hero-inner"><p class="eyebrow">INDEPENDENT FILMMAKING / GENERATIVE IMAGINATION</p><h1>Stories with<br>an <em>atmosphere.</em></h1><p class="intro">Cinematic worlds, distinctive characters and bold visual ideas.<br>Filmmaking craft meets generative possibility.</p><div class="actions"><a class="button" href="#work">Explore selected work ↓</a><a class="text-link" href="{esc(c['reel_url'] or c['youtube'])}" target="_blank" rel="noopener noreferrer">{'Watch showreel' if c['reel_url'] else 'Watch on YouTube'} ↗</a></div><div class="hero-caption"><span>FEATURED WORLD / THE PASSENGER</span><span>NARRATIVE AI FILM — 01</span></div></div></section>
<section id="work" class="container section"><div class="section-heading"><div><p class="eyebrow">01 / SELECTED WORK</p><h2>Different worlds.<br><span>One cinematic instinct.</span></h2></div><p>A selection of narrative films,<br>character worlds and commercial studies.</p></div><div class="project-grid">{''.join(cards)}</div></section>
<section id="about" class="container section about"><div><p class="eyebrow">02 / THE APPROACH</p><h2>Filmmaking first.<br><span>New tools.<br>Same intent.</span></h2></div><div class="about-copy"><p class="lead">Lanius Films is an independent filmmaking label exploring cinematic storytelling through generative production.</p><p>From narrative worlds to character-led content, the focus is on coherent visual direction, atmosphere and the craft of the final edit.</p><div class="capabilities"><span>Visual development</span><span>Generative image & video</span><span>Character consistency</span><span>Editing & post-production</span></div></div></section>
<section id="contact" class="container section contact"><p class="eyebrow">03 / LET’S TALK</p><h2>Have a world<br><em>in mind?</em></h2><p>For creative teams, recruiters and collaborators.<br>Get in touch about AI filmmaking, visual development and branded content.</p><a class="contact-email" href="mailto:{esc(c['email'])}">{esc(c['email'])} ↗</a><div class="socials"><a href="{esc(c['youtube'])}" target="_blank" rel="noopener noreferrer">YouTube ↗</a><a href="{esc(c['archive'])}" target="_blank" rel="noopener noreferrer">Archive ↗</a></div></section></main>'''+footer()
(ROOT/'index.html').write_text(index)
alts={'passenger-mirror':'A driver reflected in a rain-streaked rear-view mirror','passenger-forest':'Two figures in a moonlit forest','vex-entities':'Four shadowy entities emerging from ocean surf','valeria-ocean':'Valeria Satie beside rocks and breaking waves','alura-fashion-1':'Fashion detail with dark lace and warm light','alura-fashion-2':'Close-up of a black corset with cinematic lighting'}
for i,p in enumerate(c['projects']):
 gallery=''.join(f'<figure><img src="assets/{g}.jpg" alt="{alts[g]}" loading="lazy"></figure>' for g in p['gallery'])
 cover=f'<figure class="detail-cover {"vertical" if p["id"] in ("valeria","alura-thorne") else ""}">{image(p,"eager")}</figure>' if p['image'] else '<div class="spec-art detail-spec"><span>SELF-INITIATED / COMMERCIAL CONCEPTS</span><strong>SPEC<span>STUDIES.</span></strong><small>Selected campaign visuals coming soon.</small></div>'
 nextp=c['projects'][(i+1)%len(c['projects'])]
 page=head(p['title'],p['description'])+f'''<main id="main" class="container detail"><a class="back" href="index.html#work">← All projects</a><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['title'])}</h1><div class="detail-intro"><p>{esc(p['description'])}</p>{video_actions(p)}</div>{cover}<div class="detail-meta"><p class="eyebrow">PROJECT FOCUS</p><p>{esc(p['tags'])}</p></div><div class="gallery">{gallery}</div><div class="next"><span class="eyebrow">NEXT PROJECT</span><a href="{nextp['id']}.html">{esc(nextp['title'])} ↗</a></div></main>'''+footer()
 (ROOT/f"{p['id']}.html").write_text(page)
print('Built home and five project pages.')
