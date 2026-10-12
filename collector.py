import json, re, html, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).parent
FEEDS={'Slickdeals':'https://slickdeals.net/newsearch.php?mode=frontpage&searcharea=deals&searchin=first&rss=1','9to5Toys':'https://9to5toys.com/feed/'}
CATEGORIES={'Saat':['watch','seiko','citizen','casio','bulova','timex'],'Oyuncak':['lego','toy','pokemon','barbie','hot wheels','nerf','playset'],'Giyim':['shirt','jacket','jeans','hoodie','coat','levis','columbia','nike','adidas'],'Ayakkabı':['shoes','sneaker','boots','crocs','skechers','new balance'],'Elektronik':['airpods','headphone','ipad','tablet','anker','earbuds','speaker','airtag'],'Çanta / Cüzdan':['wallet','handbag','purse','coach','kate spade','backpack'],'Kozmetik':['perfume','fragrance','skincare','beauty','makeup'],'Termos':['stanley','owala','tumbler','thermos']}
def category(s):
 s=s.lower()
 for k,words in CATEGORIES.items():
  if any(w in s for w in words): return k
 return 'Diğer'
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'GiftDealTracker/1.1 (+personal RSS reader)'})
 with urllib.request.urlopen(req,timeout=20) as r: return r.read()
def run():
 path=ROOT/'data'/'deals.json'
 try: old=json.loads(path.read_text())['deals']
 except Exception: old=[]
 entries={x['url']:x for x in old if 'url' in x}
 success=0
 for source,url in FEEDS.items():
  try:
   root=ET.fromstring(get(url)); items=root.findall('.//item')
   for item in items:
    title=html.unescape((item.findtext('title') or '').strip()); link=(item.findtext('link') or '').strip()
    if not title or not link or not link.startswith('https://'): continue
    desc=html.unescape(re.sub('<[^>]+>',' ',item.findtext('description') or ''))
    price=re.search(r'(?<!\w)\$\s?(\d[\d,]*(?:\.\d{1,2})?)',title)
    entries[link]={'title':title[:240],'url':link,'source':source,'category':category(title+' '+desc[:250]),'price':float(price.group(1).replace(',','')) if price else None,'published':item.findtext('pubDate') or '', 'seen':datetime.now(timezone.utc).isoformat()}
   success+=1
  except Exception as e: print('Feed failed:',source,str(e))
 deals=list(entries.values()); deals.sort(key=lambda d:d.get('seen',''),reverse=True)
 # Retain recent discovery records; never manufacture a price.
 output={'updated':datetime.now(timezone.utc).isoformat(),'successful_feeds':success,'feeds_total':len(FEEDS),'deals':deals[:600]}
 path.write_text(json.dumps(output,ensure_ascii=False,indent=2))
 print('deals',len(output['deals']),'feeds',success)
if __name__=='__main__':run()
