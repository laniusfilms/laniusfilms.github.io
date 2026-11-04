"""Edit content.json and run python3 build.py. Standard library only."""
import html,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
c=json.loads((ROOT/'content.json').read_text()); esc=html.escape

def brand():
 return '<a class="brand brand-logo" href="index.html" aria-label="Lanius Films — home"><img src="assets/lanius-logo.png" alt="Lanius Films" width="100" height="100"></a>'
def head(title,description):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#0b0d0d"><meta property="og:title" content="{esc(title)} — Lanius Films"><meta property="og:description" content="{esc(description)}"><meta property="og:image" content="https://laniusfilms.github.io/assets/lanius-logo.png"><title>{esc(title)} — Lanius Films</title><link rel="icon" href="assets/lanius-logo.png" type="image/png"><link rel="stylesheet" href="styles.css?v=20261104-formats"></head><body><a class="skip" href="#main">Skip to content</a><header class="container">{brand()}<nav aria-label="Main navigation"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact ↗</a></nav></header>'''
def footer():
 return f'<footer class="container">{brand()}<p>Independent visions. Cinematic worlds.</p><span>© 2026 Lanius Films</span></footer></body></html>'
def external(url,label,cls='button'):
 return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)} ↗</a>'
def image(p,loading='lazy'):
 src=f"assets/{p['image']}.jpg" if p.get('image') else p['cover_url']
 return f'<img src="{esc(src)}" alt="{esc(p["alt"])}" loading="{loading}" decoding="async">'
def videos(p):
 return p.get('videos') or ([dict(title='Film',url=p['video_url'])] if p.get('video_url') else [])
def primary_action(p):
 vv=videos(p)
 return external(vv[0]['url'],'Watch '+vv[0]['title']) if vv else '<span class="pending">Film link coming soon</span>'
def film_card(v):
 thumb=f'<img src="{esc(v["thumbnail"])}" alt="" loading="lazy" decoding="async">' if v.get('thumbnail') else ''
 return f'''<article class="film-card {esc(v.get('format','portrait'))}"><a href="{esc(v['url'])}" target="_blank" rel="noopener noreferrer" aria-label="Watch {esc(v['title'])} on YouTube"><div class="film-thumb">{thumb}<span class="play-mark" aria-hidden="true">▶</span></div><p class="eyebrow">{esc(v.get('category','Film'))}</p><h3>{esc(v['title'])}</h3><span class="film-cta">Watch on YouTube ↗</span></a></article>'''

cards=[]
for i,p in enumerate(c['projects']):
 vv=videos(p)
 collection=f'<a class="text-link" href="{p["id"]}.html#films">Explore {len(vv)} films →</a>' if len(vv)>1 else f'<a class="text-link" href="{p["id"]}.html">Explore project →</a>'
 if p['id']=='spec-ai-campaigns':
  films=''.join(film_card(v) for v in c['featured_films'])
  cards.append(f'''<article class="project spec-project" style="grid-column:1/-1"><div class="spec-copy"><p class="eyebrow">05 / CAMPAIGNS & CHARACTER FILMS</p><h3>Featured AI Films</h3><p>Commercial concepts and character-led storytelling, developed through generative production and cinematic editing.</p><p class="spec-focus">AI campaigns · Cinematic trailers</p><a class="text-link" href="{p['id']}.html">Explore AI campaigns →</a></div><div><p class="eyebrow">HORIZONTAL FILMS / 16:9</p><div class="spec-films campaign-films">{films}</div></div></article>''')
  continue
 cls=('featured ' if i==0 else '')+('portrait ' if p['id'] in ('valeria','alura-thorne') else '')+('spec-project' if p['id']=='spec-ai-campaigns' else '')
 cards.append(f'''<article class="project {cls}"><a class="media" href="{p['id']}.html" aria-label="Explore {esc(p['title'])}">{image(p)}<span class="media-label">{i+1:02d} / {esc(p['category'])}</span><span class="arrow" aria-hidden="true">↗</span></a><div class="project-text"><div><p class="eyebrow">{esc(p['category'])}</p><h3><a href="{p['id']}.html">{esc(p['title'])}</a></h3></div><p>{esc(p['description'])}</p></div><div class="project-actions">{primary_action(p)}{collection}</div></article>''')
more=''.join(film_card(v) for v in c['more_work'])
index=head('AI Filmmaking & Visual Storytelling','AI short films, digital characters and spec campaigns. Explore selected work and the 2026 showreel from Lanius Films.')+f'''
<main id="main"><section class="hero"><img class="hero-image" src="assets/passenger.jpg" alt="" fetchpriority="high"><div class="hero-shade"></div><div class="container hero-inner"><p class="eyebrow">AI FILMMAKING / SPEC CAMPAIGNS / CHARACTER WORLDS</p><h1>Stories with<br>an <em>atmosphere.</em></h1><p class="intro">Cinematic AI films, distinctive characters and spec campaigns.<br>From visual concept to the final edit.</p><div class="actions">{external(c['reel_url'],'Watch the 2026 showreel')}<a class="text-link" href="#work">Explore selected work ↓</a></div><div class="hero-caption"><span>FEATURED WORLD / THE PASSENGER</span><span>NARRATIVE AI FILM — 01</span></div></div></section>
<section class="container reel-section" aria-label="AI Filmmaker Showreel 2026"><a class="reel-preview" href="{esc(c['reel_url'])}" target="_blank" rel="noopener noreferrer"><div class="reel-image"><img src="{esc(c['reel_thumbnail'])}" alt="AI Filmmaker Showreel 2026" loading="lazy"><span class="play-mark" aria-hidden="true">▶</span></div><div><p class="eyebrow">START HERE / 20 SECONDS</p><h2>AI Filmmaker<br>Showreel 2026.</h2><p>Jorge Sánchez · A first look at the visual worlds.</p><span class="film-cta">Watch showreel on YouTube ↗</span></div></a></section>
<section id="work" class="container section"><div class="section-heading"><div><p class="eyebrow">01 / SELECTED WORLDS</p><h2>Different worlds.<br><span>One cinematic instinct.</span></h2></div><p>Narrative films, character worlds<br>and independent commercial studies.</p></div><div class="project-grid">{''.join(cards)}</div></section>
<section id="more-work" class="container section more-work"><div class="section-heading"><div><p class="eyebrow">02 / SELECTED AI FILMS</p><h2>New stories.<br><span>Generative imagination.</span></h2></div><p>Fragrance, fashion and character worlds.<br>Vertical films in their original format.</p></div><div class="film-grid">{more}</div><a class="text-link channel-link" href="{esc(c['youtube'])}" target="_blank" rel="noopener noreferrer">Explore the full YouTube channel ↗</a></section>
<section id="about" class="container section about"><div><p class="eyebrow">03 / THE APPROACH</p><h2>Filmmaking first.<br><span>New tools.<br>Same intent.</span></h2></div><div class="about-copy"><p class="lead">Lanius Films is an independent creative studio creating cinematic AI films, spec campaigns and recurring character worlds.</p><p>The work spans AI narrative shorts, fragrance and fashion campaigns, horror and digital characters. Across formats, the focus stays on visual direction, atmosphere and the craft of the final edit.</p><div class="capabilities"><span>Visual development</span><span>Generative image & video</span><span>Character consistency</span><span>Editing & post-production</span></div></div></section>
<section id="contact" class="container section contact"><p class="eyebrow">04 / LET’S TALK</p><h2>Have a world<br><em>in mind?</em></h2><p>For creative teams, recruiters and collaborators.<br>Get in touch about AI filmmaking, visual development and branded content.</p><a class="contact-email" href="mailto:{esc(c['email'])}">{esc(c['email'])} ↗</a><div class="socials">{external(c['youtube'],'YouTube','social-link')}{external(c['archive'],'Archive','social-link')}</div></section></main>'''+footer()
(ROOT/'index.html').write_text(index)
alts={'passenger-mirror':'A driver reflected in a rain-streaked rear-view mirror','passenger-forest':'Two figures in a moonlit forest','vex-entities':'Four shadowy entities emerging from ocean surf','valeria-ocean':'Valeria Satie beside rocks and breaking waves','alura-fashion-1':'Fashion detail with dark lace and warm light','alura-fashion-2':'Close-up of a black corset with cinematic lighting'}
for i,p in enumerate(c['projects']):
 gallery=''.join(f'<figure><img src="assets/{g}.jpg" alt="{esc(alts.get(g,g))}" loading="lazy"></figure>' for g in p['gallery'])
 cover=f'<figure class="detail-cover {"vertical" if p["id"] in ("valeria","alura-thorne","spec-ai-campaigns") else ""}">{image(p,"eager")}</figure>'
 vv=videos(p)
 groups=[]
 for fmt,label in [('landscape','Horizontal films · 16:9'),('portrait','Vertical films · 9:16')]:
  group=[v for v in vv if v.get('format','portrait')==fmt]
  if group:groups.append(f'<h2>{label}</h2><div class="film-grid {fmt}-grid">'+''.join(film_card(v) for v in group)+'</div>')
 film_section='<section id="films" class="project-films"><p class="eyebrow">WATCH THE WORK</p>'+''.join(groups)+'</section>' 
 if p['id']=='spec-ai-campaigns':
  alternates=''.join(external(v['url'],v['title'],'text-link') for v in p.get('alternate_versions',[]))
  film_section+=f'<div class="alternate-cuts">{alternates}</div>'
 nextp=c['projects'][(i+1)%len(c['projects'])]
 page=head(p['title'],p['description'])+f'''<main id="main" class="container detail"><a class="back" href="index.html#work">← All projects</a><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['title'])}</h1><div class="detail-intro"><p>{esc(p['description'])}</p><a class="button" href="#films">Explore {len(vv)} {"films" if len(vv)>1 else "film"} ↓</a></div>{cover}<div class="detail-meta"><p class="eyebrow">PROJECT FOCUS</p><p>{esc(p['tags'])}</p></div>{film_section}<div class="gallery">{gallery}</div><div class="next"><span class="eyebrow">NEXT PROJECT</span><a href="{nextp['id']}.html">{esc(nextp['title'])} ↗</a></div></main>'''+footer()
 (ROOT/f"{p['id']}.html").write_text(page)
print('Built home and five project pages with logo, showreel and expanded film selection.')

