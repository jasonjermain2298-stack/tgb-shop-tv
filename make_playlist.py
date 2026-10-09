import json,subprocess
R='https://github.com/jasonjermain2298-stack/tgb-shop-tv/releases/download/media-v1/'
RAW='https://raw.githubusercontent.com/jasonjermain2298-stack/tgb-shop-tv/main/video/'
a=json.loads(subprocess.check_output(['gh','api','repos/jasonjermain2298-stack/tgb-shop-tv/releases/tags/media-v1']))
have={x['name'] for x in a['assets'] if x['state']=='uploaded'}
ORDER=['01-private-studio','02-athlete-braids','03-precision-cut','04-hot-towel','11-athletes','33-maxie-all-american','34-maxie-event','05-locs-client','12-sc-06','06-beard-ritual','13-sc-07','08-athlete-braids-2','14-sc-11','fv-01','07-client-chair','15-sc-13','10-products','apparel-albums','16-sc-24','17-sc-26','30-tour','18-sc-38','19-sc-46','fv-02','09-the-studio','20-sc-47','21-sc-49','cooking-show','31-mobile-unit','35-ruff-endz-shoot','22-sc-03','23-sc-17','fv-03','24-sc-18','25-sc-23','32-jaxson-prime','fv-04','fv-05','fv-06','fv-07','fv-08']
EXTRA={'apparel-albums','cooking-show'}
for e in EXTRA: have.add(e+'.mp4')
names=[o+'.mp4' for o in ORDER if o+'.mp4' in have]
names+=sorted(n for n in have if n not in names and n[0].isdigit())
rows=['Title,URL,Description,Type,DisplayDuration','TGB TV Logo,%slogo-tv.mp4,Logo,Video,'%RAW]
logos=['logo-crest.mp4','logo-tv.mp4']
for i,n in enumerate(names):
    rows.append('%s,%s%s,Clip,Video,'%(n[:-4],RAW if n[:-4] in EXTRA else R,n))
    if i%2==1: rows.append('Logo,%s%s,Logo,Video,'%(RAW,logos[(i//2)%2]))
rows.append('Shop TV Loop,%stgb-shop-tv-loop-v2.mp4,Loop,Video,'%R)
open('playlist.csv','w').write('\n'.join(rows)+'\n'); print(len(names),'clips')
