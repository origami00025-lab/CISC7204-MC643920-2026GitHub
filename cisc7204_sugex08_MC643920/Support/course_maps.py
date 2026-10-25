from pathlib import Path
import os,math,urllib.request,concurrent.futures,json
from PIL import Image as PILImage
from IPython.display import Image,display
import geoplotlib,pyglet
from geoplotlib import core
from geoplotlib.utils import BoundingBox

ROOT=Path(__file__).resolve().parent.parent
CACHE=ROOT/'Support'/'tiles'
os.environ['GEOPLOTLIB_TILE_CACHE']=str(CACHE)
for name,service in [('positron','World_Light_Gray_Base'),('darkmatter','World_Dark_Gray_Base')]:
 core._DEFAULT_TILE_PROVIDERS[name]={
  'url':lambda z,x,y,s=service:f'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/{s}/MapServer/tile/{z}/{y}/{x}',
  'attribution':'Geoplotlib | Esri, HERE, Garmin, OpenStreetMap contributors | public '+service}

def _run(config,mode='snapshot',name='map',layer=None,hover=None):
 config.screen_w=1000;config.screen_h=650
 app=core.GeoplotlibApp(config)
 bbox=config.bbox or (BoundingBox.from_bboxes([l.bbox() for l in config.layers]) if config.layers else BoundingBox.WORLD)
 app.proj.fit(bbox,force_zoom=config.requested_zoom)
 p=app.proj;tasks=[]
 for x in range(int(p.xtile),int(p.xtile+p.tiles_horizontally+1)):
  for y in range(int(p.ytile),int(p.ytile+p.tiles_vertically+1)):
   if 0<=x<2**p.zoom and 0<=y<2**p.zoom:
    file=CACHE/app.map_layer.tiles_dir/str(p.zoom)/str(x)/f'{y}.png'
    tasks.append((app.map_layer.url_generator(p.zoom,x,y),file))
 def download(item):
  url,file=item
  if file.exists():return
  file.parent.mkdir(parents=True,exist_ok=True)
  req=urllib.request.Request(url,headers={'User-Agent':'CISC7204-course-exercise/1.0 (educational local map)'})
  data=urllib.request.urlopen(req,timeout=25).read()
  file.write_bytes(data)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(download,tasks))
 if hover:
  x,y=p.lonlat_to_screen([hover[0]],[hover[1]])
  app.mouse_x=float(x[0]-p.xtile*256)
  app.mouse_y=650-float(y[0]+p.ytile*256)
 images=[];frames=[];count=0;done=False
 original=app.on_draw
 def draw():
  nonlocal count,done
  original();count+=1
  if mode=='animation' and count%12==0:
   file=Path(f'{name}_{len(frames):02d}.png');core.GeoplotlibApp.screenshot(str(file));frames.append(file)
   if len(frames)==10:pyglet.app.exit()
  if mode=='keyboard' and count in [10,20,30]:
   suffix={10:'A',20:'C',30:'Z'}[count]
   assert layer.start_letters[layer.start_letter]==suffix
   file=Path(f'{name}_{suffix}.png');core.GeoplotlibApp.screenshot(str(file));images.append(file)
   if count==10:
    app.on_key_release(pyglet.window.key.RIGHT,0);app.on_key_release(pyglet.window.key.RIGHT,0)
   elif count==20:
    for _ in range(3):app.on_key_release(pyglet.window.key.LEFT,0)
   else:pyglet.app.exit()
 app.on_draw=draw
 try:
  app.start()
 finally:
  pyglet.clock.unschedule(app.on_update);app.close();geoplotlib._global_config.reset()
 if mode=='animation':
  pics=[PILImage.open(f).convert('RGB') for f in frames]
  pics[0].save(name+'.gif',save_all=True,append_images=pics[1:],duration=250,loop=0)
  display(Image(filename=str(frames[0]),width=900));display(Image(filename=str(frames[-1]),width=900))
  print('Saved real rendered animation:',name+'.gif','| distinct frames:',len({im.tobytes() for im in pics}))
 if mode=='keyboard':
  for file in images:display(Image(filename=str(file),width=900))
  print('Real key-event checks passed: A -> RIGHT twice -> C; C -> LEFT three times -> Z.')

def snapshot(name,hover=None):
 Path('outputs').mkdir(exist_ok=True)
 name='outputs/'+name
 config=geoplotlib._global_config
 config.savefig=str(Path(name).resolve())
 _run(config,name=name,hover=hover)
 file=Path(name+'.png')
 assert file.exists(),'Map renderer did not create output'
 display(Image(filename=str(file),width=900))

def animation(name,layer):
 Path('outputs').mkdir(exist_ok=True)
 _run(geoplotlib._global_config,mode='animation',name='outputs/'+name,layer=layer)
def keyboard_demo(name,layer):
 Path('outputs').mkdir(exist_ok=True)
 _run(geoplotlib._global_config,mode='keyboard',name='outputs/'+name,layer=layer)
