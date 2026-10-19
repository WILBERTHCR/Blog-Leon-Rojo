import numpy as np
from PIL import Image
T=np.array([242,242,240],float)
def flat_bbox(path,maxdim=2400):
    im=Image.open(path).convert('RGB')
    if max(im.size)>maxdim: im.thumbnail((maxdim,maxdim),Image.LANCZOS)
    a=np.asarray(im).astype(float); h,w,_=a.shape
    yy,xx=np.mgrid[0:h,0:w]; x=xx/w-.5; y=yy/h-.5
    A=np.stack([np.ones_like(x),x,y,x*x,y*y,x*y],-1)
    m=np.zeros((h,w),bool); b=int(min(h,w)*.08); m[:b]=m[-b:]=True; m[:,:b]=m[:,-b:]=True
    sat=a.max(-1)-a.min(-1); g=a.mean(-1); m&=(sat<16)&(g>180)
    out=np.empty_like(a); bg=np.empty_like(a)
    for c in range(3):
        co,*_=np.linalg.lstsq(A[m],a[...,c][m],rcond=None); r=a[...,c]-A@co; mm=m&(np.abs(r)<6)
        co,*_=np.linalg.lstsq(A[mm],a[...,c][mm],rcond=None); bg[...,c]=A@co; out[...,c]=a[...,c]*T[c]/bg[...,c]
    d=np.abs(a-bg).sum(-1)
    # gradient too
    gx=np.abs(np.diff(g,axis=1,prepend=g[:,:1])); gy=np.abs(np.diff(g,axis=0,prepend=g[:1]))
    s=(d>24)|((gx+gy)>14)
    s[:int(h*.02)]=0;s[-int(h*.02):]=0;s[:,:int(w*.02)]=0;s[:,-int(w*.02):]=0
    ys,xs=np.where(s)
    y0,y1=np.percentile(ys,[0.1,99.9]).astype(int); x0,x1=np.percentile(xs,[0.1,99.9]).astype(int)
    return np.clip(out,0,255),(x0,y0,x1,y1)

def composite(paths,heights,out,gap=60):
    pieces=[]
    for p,hrel in zip(paths,heights):
        a,(x0,y0,x1,y1)=flat_bbox(p)
        mg=int((y1-y0)*.09)
        piece=Image.fromarray(a[max(0,y0-mg):y1+mg,max(0,x0-mg):x1+mg].astype(np.uint8))
        th=int(1400*hrel); sc=th/(y1-y0)
        pieces.append(piece.resize((int(piece.width*sc),int(piece.height*sc)),Image.LANCZOS))
    H=max(p.height for p in pieces)+200; W=sum(p.width for p in pieces)+gap*(len(pieces)-1)+300
    c=Image.new('RGB',(W,H),tuple(int(v) for v in T)); x=150
    for p in pieces:
        w,h=p.size; yy,xx=np.mgrid[0:h,0:w]; d=np.minimum(np.minimum(xx,w-1-xx),np.minimum(yy,h-1-yy)).astype(float)
        t=np.clip(d/(min(w,h)*.07),0,1); al=Image.fromarray((t*t*(3-2*t)*255).astype(np.uint8))
        c.paste(p,(x,H-100-p.height),al); x+=p.width+gap
    c.save(out,quality=93)
