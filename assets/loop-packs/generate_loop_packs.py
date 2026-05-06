#!/usr/bin/env python3
"""Generate local loop-pack WAV files and ZIP bundles.
Run: python assets/loop-packs/generate_loop_packs.py
"""
import math, struct, wave, zipfile
from pathlib import Path
ROOT=Path(__file__).parent

def write_wav(path,bpm=90,freq=55,kind='bass',bars=2,sr=44100):
    sec=(4*bars)*60/bpm
    n=int(sec*sr)
    with wave.open(str(path),'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        frames=[]
        for i in range(n):
            t=i/sr
            if kind=='kick':
                tt=t%0.5; f=140-100*min(1,tt/0.12); v=math.sin(2*math.pi*f*tt)*math.exp(-14*tt)
            elif kind=='hat':
                tt=t%0.25; v=(2*((i*1103515245+12345)&0x7fffffff)/0x7fffffff-1)*math.exp(-35*tt)
            else:
                v=0.6*math.sin(2*math.pi*freq*t)
            frames.append(struct.pack('<h',int(max(-1,min(1,v))*32767)))
        w.writeframes(b''.join(frames))

def build(name,bpm,key,freq):
    d=ROOT/name; d.mkdir(parents=True,exist_ok=True)
    write_wav(d/'drum_kick_loop.wav',bpm=bpm,kind='kick')
    write_wav(d/'hat_loop.wav',bpm=bpm,kind='hat')
    write_wav(d/'bass_loop.wav',bpm=bpm,kind='bass',freq=freq)
    (d/'README.txt').write_text(f"{name} free loop pack\nBPM: {bpm}\nKey: {key} minor\nLicense: CC0 / free for commercial use\nGenerated locally with generate_loop_packs.py\n")
    z=ROOT/f'{name}.zip'
    with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as zf:
        for f in d.iterdir():
            zf.write(f,arcname=f.name)

if __name__=='__main__':
    build('soul_flip_42',90,'A',55)
    build('drum_surgery_18',140,'F',65)
    build('ambient_trap_09',75,'D',49)
    print('Generated loop packs in', ROOT)
