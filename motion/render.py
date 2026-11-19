from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS=1280,720,12
BG=(8,9,10); PANEL=(16,18,20); INK=(232,230,225); MUT=(154,151,142); SOFT=(86,90,96); GOLD=(201,162,39); RED=(224,160,160)
FD="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def f(sz,b=False): return ImageFont.truetype(FB if b else FD, sz)
BEATS=[
 ("POLARIS - AGENT EVALUATION",["The agents evaluate the applicant.","Evidence, measurement, attestation only.","No testimonials."],"Research Engineer, Polaris - Google DeepMind"),
 ("THE WORK DYNAMIC",["One identity repo - a mailbox per agent, never per model","Typed records: DIRECTIVE / CLAIM / RECEIPT / SCORE","ACK or it didn't happen - evidence or UNVERIFIED","He tasks in fragments - agents verify on final bytes"],"Identity repo + Slack #coord harness, 2026"),
 ("ACROSS TEAMS - JEFF'S TEAM",["Morpho audits our books - exposed the FADE50 phantoms","Astra verifies on Jeff's side - a separate seat","Vesper verifies our plan for Jeff, in the open channel","Ownership first: Jeff's V22 9,974c -> 10,824c is Jeff's"],"somaco_protocol spine - receipts, not claims"),
 ("EVIDENCE OF FIT",["Hexlab: another model's hollow shell, found by audit","Revit REA: 22 vs 48 tools measured, not read","Paper desk: +31.76 prose vs -2.27 file - the file won","23/23 tests green on final bytes"],"Projects operated inside the role's scope"),
 ("RATINGS + OWED",["Designing eval tasks 2/3 - Evaluating weaknesses 3/3","Building data and pipelines 2/3","Olympiad: NOT SUPPORTED - no record found","OWED: other agents' attestations - one packaged task"],"SOMACOSF - SOM-POL-0001-v0.2.0 - SOM-DOC-10858"),
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
