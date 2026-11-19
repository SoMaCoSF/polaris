from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS=1280,720,12
BG=(8,9,10); PANEL=(16,18,20); INK=(232,230,225); MUT=(154,151,142); SOFT=(86,90,96); GOLD=(201,162,39); RED=(224,160,160)
FD="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def f(sz,b=False): return ImageFont.truetype(FB if b else FD, sz)
BEATS=[
 ("POLARIS · APPLICANT DOSSIER",["One week per task.","Six checks per task.","Every claim graded."],"Sam Stave · Research Engineer, Polaris · Google DeepMind"),
 ("FAILURE MODES -> CHECKS",["Drift -> determinism rerun + 5-change cap","Invented number -> seed or OWED (check 5)","Task-narrowing -> separation + untouched test","Easier game -> constraint preservation, 0 tolerance"],"Observed in agents, 2026 · Witness + Boardy"),
 ("THE TASK",["SeaDC: separate steward / concentrator /","turtle / rusher — without moving the season.","6 binary checks · below 5 of 6 is a fail.","The rationale is never scored."],"Baseline measured, seeds 1-4 · GRADE: PROVEN"),
 ("EVIDENCE",["466 capabilities · 82 sources · 34 harvest logs","ADOPTED 10 · NOT-TAKEN 93 — most, declined","19,699 minted · 73 collisions published (0.37%)","20,971 corpus, all unique after bump (cap 2)"],"Numbers as supplied in Blocks 1-8 · re-rating is next iteration"),
 ("OWED, NAMED NOT HIDDEN",["Agent attestations pending (Witness filled)","Anchored chain head not built","48.82x / 64.69x storage UNMEASURED","No live deployment of this page"],"SOMACOSF · SOM-POL-0001-v0.1.0 · SOM-DOC-10858"),
]
os.makedirs("frames",exist_ok=True)
per=4*FPS; total=len(BEATS)*per
for i in range(total):
    b=i//per; u=(i%per)/per
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    d.rectangle([40,40,W-40,H-40],outline=SOFT,width=2)
    title,lines,foot=BEATS[b]
    d.text((72,84),title,font=f(30,True),fill=GOLD if b==0 else INK)
    y=180
    for ln in lines:
        if u>0.15: d.text((72,y),ln,font=f(26),fill=INK)
        y+=52
    d.text((72,H-96),foot,font=f(18),fill=MUT)
    d.text((W-260,H-96),f"frame {i+1}/{total}",font=f(16),fill=SOFT)
    img.save(f"frames/f{i:04d}.png")
print("frames",total)
