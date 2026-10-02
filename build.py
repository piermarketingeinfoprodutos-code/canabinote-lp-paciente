from pathlib import Path
import json,html,re
ROOT=Path(__file__).parent
D=ROOT/'dist'
S=[x['lines'] for x in json.loads((D/'copy.json').read_text(encoding='utf-8'))]
WA='https://wa.me/5511916901512?text=Oi%2C%20quero%20saber%20mais%20sobre%20o%20tratamento%20com%20cannabis%20medicinal.'
MD='https://prd.canabinote.com/#/prescribers?formation=100'
def fmt(s): return re.sub(r'==(.*?)==',r'<mark>\1</mark>',html.escape(s))
def para(s,cls=''):return f'<p class="{cls}">{fmt(s)}</p>'
def img(name,alt,cls='',priority=False):return f'<img class="{cls}" src="assets/{name}" alt="{html.escape(alt)}" '+('fetchpriority="high"' if priority else 'loading="lazy"')+' decoding="async">'
def action(secondary=True):return '<div class="actions"><a class="cta" href="'+html.escape(WA)+'" target="_blank" rel="noopener noreferrer"><span>QUERO SABER MAIS SOBRE A CANNABIS MEDICINAL</span><span class="cta-arrow" aria-hidden="true">↗</span></a>'+('<a class="secondary" href="'+html.escape(MD)+'" target="_blank" rel="noopener noreferrer">Já quero escolher um médico prescritor →</a>' if secondary else '')+'</div>'
def logo():return '<span class="brand">'+img('logo-canabinote.png','Canabinote — Guiada pela ciência',priority=True)+'</span>'
head='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Canabinote | Cannabis medicinal e acompanhamento</title><meta name="description" content="Entenda a cannabis medicinal e conheça uma jornada de cuidado guiada pela ciência, da escolha do médico ao acompanhamento."><link rel="icon" href="assets/logo-canabinote.png"><link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head><body><a class="skip" href="#conteudo">Ir para o conteúdo</a>'''
header='<header class="site-header"><div class="header-inner"><a href="#inicio" aria-label="Canabinote, início">'+logo()+'</a><a class="header-link" href="'+MD+'" target="_blank" rel="noopener noreferrer"><span class="header-cta-copy"><small>Já sabe o próximo passo?</small><strong>Escolher um profissional</strong></span><span class="header-cta-arrow" aria-hidden="true">→</span></a></div></header>'
s=S[0]
hero='<section class="hero" id="inicio"><div class="hero-photo">'+img('casal.jpg','Casal conversando em casa em um momento de tranquilidade.',priority=True)+'</div><div class="hero-inner"><div class="hero-copy"><h1>'+fmt(s[2]).replace('sua dor.','sua <strong>dor.</strong>')+'</h1>'+para(s[4],'hero-subtitle')+para(s[6],'hero-support')+action()+'</div></div></section>'
strip='<div class="condition-strip" aria-label="Condições"><div class="ticker"><div>'+fmt(s[10])+'</div><div aria-hidden="true">'+fmt(s[10])+'</div></div><div class="strip-controls"><button type="button" data-strip="-1" aria-label="Condições anteriores">←</button><button type="button" data-strip="1" aria-label="Próximas condições">→</button></div></div>'+para(s[6],'mobile-support wrap')
rest=''
exec((ROOT/'sections.py').read_text(encoding='utf-8-sig'))
(D/'index.html').write_text(head+header+'<main id="conteudo">'+hero+strip+rest+'</main></body></html>',encoding='utf-8')

