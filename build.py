"""Generate the static studio portfolio from content.json (standard library only)."""
import html
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs

ROOT = Path(__file__).resolve().parent
BASE = 'https://laniusfilms.github.io/'
c = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
s = c['site']
esc = html.escape
projects = c['projects']

def brand():
    return '<a class="brand brand-logo" href="index.html" aria-label="Lanius Films — home"><img src="assets/lanius-logo.png" alt="Lanius Films" width="100" height="100"></a>'

def head(title, description, path='index.html', cover='assets/lanius-logo.png'):
    full_title = f'{title} — Lanius Films'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(description)}"><meta name="theme-color" content="#0b0d0d">
<link rel="canonical" href="{BASE}{path}"><meta property="og:type" content="website"><meta property="og:site_name" content="Lanius Films"><meta property="og:url" content="{BASE}{path}"><meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:image" content="{esc(urljoin(BASE, cover))}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(full_title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{esc(urljoin(BASE, cover))}">
<title>{esc(full_title)}</title><link rel="icon" href="assets/lanius-logo.png" type="image/png"><link rel="stylesheet" href="styles.css?v=20261119-inline"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="container">{brand()}<nav aria-label="Main navigation"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a></nav></header>'''

def footer():
    return f'<footer class="container">{brand()}<p>Independent visions. Cinematic worlds.</p><a href="index.html#contact">Contact the studio</a><span>© 2026 Lanius Films</span></footer><script src="script.js?v=20261119-inline" defer></script></body></html>'

def video_id(url):
    u = urlparse(url)
    candidate = parse_qs(u.query).get('v', [''])[0] if u.path == '/watch' else u.path.strip('/').split('/')[-1]
    return candidate if len(candidate) == 11 and all(ch.isalnum() or ch in '_-' for ch in candidate) else ''

def video_data(url, title, description=''):
    vid = video_id(url)
    return f' data-video-id="{esc(vid)}" data-video-title="{esc(title)}" data-video-description="{esc(description)}"' if vid else ''

def external(url, label, cls='button'):
    # Watch links open the embedded player. The real URL remains the no-JS fallback.
    data = video_data(url, label.removeprefix('Watch ')) if label.startswith('Watch ') else ''
    return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer"{data}>{esc(label)}{ "" if data else " ↗"}</a>'

def source_image(p):
    return f"assets/{p['image']}.jpg" if p.get('image') else p['cover_url']

def image(p, loading='lazy'):
    width,height = (941,1672) if p['id'] in ('valeria','alura-thorne') else (1280,720)
    return f'<img src="{esc(source_image(p))}" alt="{esc(p["alt"])}" width="{width}" height="{height}" loading="{loading}" decoding="async">'

def film_card(v, show_description=True):
    thumb = f'<img src="{esc(v["thumbnail"])}" alt="{esc(v["title"])} — film poster" loading="lazy" decoding="async">'
    description = f'<p class="film-description">{esc(v["description"])}</p>' if show_description and v.get('description') else ''
    data = video_data(v['url'], v['title'], v.get('description',''))
    return f'''<article class="film-card {esc(v.get('format', 'portrait'))}"><a class="film-thumb" href="{esc(v['url'])}" target="_blank" rel="noopener noreferrer" aria-label="Play {esc(v['title'])}"{data}>{thumb}<span class="play-mark" aria-hidden="true">▶</span></a><p class="eyebrow">{esc(v.get('category', 'Film'))}</p><h3>{esc(v['title'])}</h3>{description}<a class="film-cta" href="{esc(v['url'])}" target="_blank" rel="noopener noreferrer">Open on YouTube ↗</a></article>'''

def project_card(p, number, wide=False):
    cls = ('wide ' if wide else '') + ('portrait' if p['id'] in ('valeria', 'alura-thorne') else '')
    count = len(p['videos'])
    return f'''<article class="project {cls}"><a class="media" href="{p['id']}.html" aria-label="Explore {esc(p['title'])}">{image(p)}<span class="media-label">{number:02d} / {esc(p['category'])}</span><span class="arrow" aria-hidden="true">↗</span></a><div class="project-text"><div><p class="eyebrow">{esc(p['category'])}</p><h3><a href="{p['id']}.html">{esc(p['title'])}</a></h3></div><p>{esc(p['description'])}</p></div><div class="project-actions">{external(p['video_url'], 'Watch '+p['videos'][0]['title'])}<a class="text-link" href="{p['id']}.html#films">{'Explore project' if count == 1 else 'Explore '+str(count)+' films'} →</a></div></article>'''

def section_heading(kicker, title, note):
    return f'<div class="section-heading"><div><p class="eyebrow">{esc(kicker)}</p><h2>{title}</h2></div><p>{note}</p></div>'

narrative = [p for p in projects if p['home_group'] == 'narrative']
worlds = [p for p in projects if p['home_group'] == 'worlds']
campaign = next(p for p in projects if p['home_group'] == 'campaigns')
features = ''.join(project_card(p, i+1) for i,p in enumerate(narrative))
world_cards = ''.join(project_card(p, i+1, p['id']=='vex-darkness') for i,p in enumerate(worlds))
capabilities = ''.join(f'<span>{esc(x)}</span>' for x in s['capabilities'])
socials = ''.join(external(x['url'],x['label'],'social-link') for x in s['socials'])
index = head(s['title'],s['description'],cover=source_image(narrative[0])) + f'''
<main id="main">
<section class="hero"><img class="hero-image" src="{esc(s['hero_image'])}" alt="" fetchpriority="high"><div class="hero-shade"></div><div class="container hero-inner"><p class="eyebrow">{esc(s['hero_kicker'])}</p><h1>{s['hero_title']}</h1><p class="intro">{esc(s['hero_intro'])}</p><div class="actions">{external(narrative[0]['video_url'],'Watch THE WISH')}<a class="text-link" href="#work">Explore selected work ↓</a></div><div class="hero-caption"><span>{esc(s['hero_caption'])}</span><span>BARCELONA / INDEPENDENT STUDIO</span></div></div></section>
<section class="container reel-section" aria-label="Showreel 2026"><a class="reel-preview" href="{esc(c['reel_url'])}" target="_blank" rel="noopener noreferrer"{video_data(c['reel_url'], "Showreel 2026")}><div class="reel-image"><img src="{esc(c['reel_thumbnail'])}" alt="Jorge Sánchez — AI Filmmaker Showreel 2026" loading="lazy"><span class="play-mark" aria-hidden="true">▶</span></div><div><p class="eyebrow">A FIRST LOOK / 20 SECONDS</p><h2>Showreel<br>2026.</h2><p>Jorge Sánchez · Direction, generative production & post.</p><span class="film-cta">Play showreel</span></div></a></section>
<section id="work" class="container section">{section_heading('01 / NARRATIVE FILMS','Stories with<br><span>an atmosphere.</span>','Independent short films.<br>Direction, image and sound.')}<div class="project-grid narrative-grid">{features}</div></section>
<section id="campaigns" class="container section">{section_heading('02 / BRANDED CONCEPTS','Creative direction.<br><span>Cinematic possibilities.</span>','Self-initiated spec work.<br>Fragrance, fashion and technology.')}<article class="project spec-project"><div class="spec-copy"><p class="eyebrow">INDEPENDENT SPEC CAMPAIGNS</p><h3>From an idea<br>to a world.</h3><p>{esc(campaign['description'])}</p><a class="text-link" href="spec-ai-campaigns.html">Explore campaigns & studies →</a></div><div class="spec-films campaign-films">{''.join(film_card(v) for v in c['featured_films'])}</div></article></section>
<section id="worlds" class="container section">{section_heading('03 / CINEMATIC WORLDS','Distinct identities.<br><span>Stories that continue.</span>','Horror, fashion and character-led series.<br>Explore each collection.')}<div class="project-grid">{world_cards}</div></section>
<section id="more-work" class="container section more-work">{section_heading('04 / SELECTED RELEASES','A selection<br><span>from our worlds.</span>','Horror, fashion and fragrance.<br>Full collections remain on each project page.')}<div class="film-grid recent-grid">{''.join(film_card(v) for v in c['more_work'])}</div><details class="film-archive"><summary>Earlier selected films</summary><div class="film-grid archive-grid">{''.join(film_card(v) for v in c['more_work_archive'])}</div></details><a class="text-link channel-link" href="{esc(c['youtube'])}" target="_blank" rel="noopener noreferrer">Explore the full YouTube channel ↗</a></section>
<section id="about" class="container section about"><div><p class="eyebrow">05 / THE STUDIO</p><h2>Filmmaking first.<br><span>From the idea<br>to the final master.</span></h2></div><div class="about-copy"><p class="lead">{esc(s['about_lead'])}</p><p>{esc(s['about_copy'])}</p><p>{esc(s['about_process'])}</p><div class="capabilities">{capabilities}</div></div></section>
<section id="contact" class="container section contact"><p class="eyebrow">06 / LET’S TALK</p><h2>Have a world<br><em>in mind?</em></h2><p>{esc(s['contact_copy'])}</p><a class="contact-email" href="mailto:{esc(c['email'])}">{esc(c['email'])} ↗</a><div class="socials">{socials}</div></section></main>''' + footer()
(ROOT/'index.html').write_text(index,encoding='utf-8')

alts={'passenger-mirror':'A driver reflected in a rain-streaked rear-view mirror','passenger-forest':'Two figures in a moonlit forest','vex-entities':'Four shadowy entities emerging from ocean surf','valeria-ocean':'Valeria Satie beside rocks and breaking waves','alura-fashion-1':'Fashion detail with dark lace and warm light','alura-fashion-2':'Close-up of a black corset with cinematic lighting'}

def film_group(vv, cls='', show_description=True):
    return f'<div class="film-grid {cls}">'+''.join(film_card(v, show_description) for v in vv)+'</div>'

def collection(p):
    vv=p['videos']
    landscape=[v for v in vv if v.get('format')=='landscape']
    portrait=[v for v in vv if v.get('format')=='portrait']
    sections=[]
    if portrait:
        selected=portrait[:p.get('featured_count',4)]
        older=portrait[len(selected):]
        sections.append('<h2>Selected films · 9:16</h2>'+film_group(selected,'portrait-grid'))
        if older:
            sections.append('<details class="film-archive"><summary>Earlier films & archive</summary>'+film_group(older,'portrait-grid archive-grid')+'</details>')
    if landscape:
        label='Narrative film · 16:9' if p['home_group']=='narrative' else ('Cinematic trailer · 16:9' if p['id']=='alura-thorne' else 'Branded concepts · 16:9')
        # On character collections the trailer is a separate introduction, not a recent release.
        intro='<h2>'+label+'</h2>'+film_group(landscape,'landscape-grid'+(' trailer-layout' if p['id']=='alura-thorne' else ''),p['home_group']!='narrative')
        sections.insert(0,intro)
    out='<section id="films" class="project-films"><p class="eyebrow">WATCH THE WORK</p>'+''.join(sections)+'</section>'
    if p.get('alternate_versions'):
        out+='<div class="alternate-cuts">'+''.join(external(v['url'],v['title'],'text-link') for v in p['alternate_versions'])+'</div>'
    return out

gallery_sizes={'valeria-ocean':(1496,2000),'alura-fashion-1':(572,1024),'alura-fashion-2':(572,1024),'vex-entities':(2000,1500),'passenger-forest':(2000,1140),'passenger-mirror':(1672,941)}
def gallery_figure(g):
    if isinstance(g, str):
        src='assets/'+g+'.jpg'; alt=alts.get(g,g); width,height=gallery_sizes[g]; caption=''
    else:
        src=g['src']; alt=g['alt']; width,height=g['width'],g['height']; caption=g.get('caption','')
    return f'<figure><img src="{esc(src)}" alt="{esc(alt)}" width="{width}" height="{height}" loading="lazy" decoding="async">'+(f'<figcaption>{esc(caption)}</figcaption>' if caption else '')+'</figure>'

for i,p in enumerate(projects):
    gallery=''.join(gallery_figure(g) for g in p['gallery'])
    vertical=p['id'] in ('valeria','alura-thorne')
    cover=f'<figure class="detail-cover {"vertical" if vertical else ""}">{image(p,"eager")}</figure>'
    if p['home_group']=='narrative': cover=''
    nextp=projects[(i+1)%len(projects)]
    count=len(p['videos'])
    page=head(p['title'],p['description'],p['id']+'.html',source_image(p))+f'''<main id="main" class="container detail"><a class="back" href="index.html#work">← All projects</a><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['title'])}</h1><div class="detail-intro"><p>{esc(p['description'])}</p><a class="button" href="#films">Explore {count} {"films" if count>1 else "film"} ↓</a></div>{cover}<div class="detail-meta"><p class="eyebrow">PROJECT FOCUS</p><p>{esc(p['tags'])}</p></div>{collection(p)}<section class="stills-section" aria-label="Project stills"><p class="eyebrow">PROJECT STILLS & START FRAMES</p><div class="gallery">{gallery}</div></section><div class="next"><span class="eyebrow">NEXT PROJECT</span><a href="{nextp['id']}.html">{esc(nextp['title'])} ↗</a></div></main>'''+footer()
    (ROOT/(p['id']+'.html')).write_text(page,encoding='utf-8')
print(f'Built homepage and {len(projects)} project pages from content.json.')
