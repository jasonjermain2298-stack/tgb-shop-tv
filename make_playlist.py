import json,subprocess
R='https://github.com/jasonjermain2298-stack/tgb-shop-tv/releases/download/media-v1/'
RAW='https://raw.githubusercontent.com/jasonjermain2298-stack/tgb-shop-tv/main/video/'
a=json.loads(subprocess.check_output(['gh','api','repos/jasonjermain2298-stack/tgb-shop-tv/releases/tags/media-v1']))
names=sorted(x['name'] for x in a['assets'] if x['state']=='uploaded' and x['name'][:2].isdigit())
rows=['Title,URL,Description,Type,DisplayDuration','TGB TV Logo,%slogo-tv.mp4,Logo,Video,'%RAW]
logos=['logo-crest.mp4','logo-tv.mp4']
for i,n in enumerate(names):
    rows.append('%s,%s%s,Clip,Video,'%(n[:-4],R,n))
    if i%2==1: rows.append('Logo,%s%s,Logo,Video,'%(RAW,logos[(i//2)%2]))
rows.append('Shop TV Loop,%stgb-shop-tv-loop-v2.mp4,Loop,Video,'%R)
open('playlist.csv','w').write('\n'.join(rows)+'\n'); print(len(names),'clips')
