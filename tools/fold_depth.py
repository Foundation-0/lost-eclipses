"""Finite phase-bin screen; no physical disappearance is inferred from its flag."""
import argparse,csv,json,math,statistics

def screen(rows,period,epoch,amplitude,bins=100,min_per_bin=3):
    if not all(math.isfinite(x) for x in (period,epoch,amplitude)) or period<=0 or amplitude<=0: raise ValueError('finite positive period and amplitude required')
    phase=[[] for _ in range(bins)];sectors=set()
    for r in rows:
        t,m=float(r['time_days']),float(r['magnitude'])
        if not math.isfinite(t) or not math.isfinite(m):continue
        if r.get('quality','0')!='0':continue
        phase[int(((t-epoch)/period%1)*bins)%bins].append(m);sectors.add(r['sector'])
    med=[statistics.median(b) for b in phase if len(b)>=min_per_bin]
    coverage=len(med)/bins
    if coverage<0.9:return dict(status='insufficient_phase_coverage',coverage=coverage,sectors=sorted(sectors),flag=None)
    depth=max(med)-statistics.median(med)
    return dict(status='screened',coverage=coverage,sectors=sorted(sectors),depth_mag=depth,gcvs_amplitude_mag=amplitude,ratio=depth/amplitude,flag=depth/amplitude<0.2,phase_bins=phase)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('csv');p.add_argument('--period',type=float,required=True);p.add_argument('--epoch',type=float,required=True);p.add_argument('--amplitude',type=float,required=True);p.add_argument('--output',required=True);a=p.parse_args()
    with open(a.csv) as f:r=screen(list(csv.DictReader(f)),a.period,a.epoch,a.amplitude)
    with open(a.output,'w') as f:json.dump(r,f,indent=2)
