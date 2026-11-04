import json
YEARS=list(range(2026,2035))
FA_LAW={2026:.975,2027:.95,2028:.90,2029:.775,2030:.515,2031:.39,2032:.265,2033:.14,2034:0}
FA_PROP={2026:.975,2027:.95,2028:.915,2029:.81,2030:.59,2031:.48,2032:.375,2033:.27,2034:.15}
PRICE={'low':{2026:75,2027:75,2028:78,2029:80,2030:85,2031:88,2032:90,2033:92,2034:95},
       'base':{2026:82,2027:90,2028:100,2029:110,2030:126,2031:132,2032:138,2033:144,2034:150},
       'high':{2026:85,2027:100,2028:115,2029:130,2030:145,2031:155,2032:165,2033:175,2034:185}}
EURINR=106.12
MARKUP={2026:.10,2027:.20}  # 30% from 2028; fertiliser 1%
def mk(y,sector): 
    if sector=='Fertilisers': return .01
    return MARKUP.get(y,.30)
firms=[
 # name, sector, product, BM, default, SEE_direct, indirect_t_per_t (stress), EU_vol_t, EBITDA_cr
 dict(name='Tata Steel',sector='Steel',cn='7208 HRC',bm=1.370,dflt=4.28,see=2.45,ind=0.22,eu=600000,ebitda=34848),
 dict(name='JSW Steel',sector='Steel',cn='7208 HRC',bm=1.370,dflt=4.28,see=2.36,ind=0.20,eu=890000,ebitda=29821),
 dict(name='Hindalco',sector='Aluminium',cn='7601 unwrought',bm=1.423,dflt=1.87,see=1.87,ind=17.7,eu=50000,ebitda=38097),
 dict(name='NALCO',sector='Aluminium',cn='7601 unwrought',bm=1.423,dflt=1.87,see=1.87,ind=17.6,eu=35000,ebitda=8613),
 dict(name='UltraTech',sector='Cement',cn='2523 29 Portland',bm=0.666,dflt=1.48,see=0.62,ind=0,eu=0,ebitda=17598),
 dict(name='Ambuja',sector='Cement',cn='2523 29 Portland',bm=0.666,dflt=1.48,see=0.62,ind=0,eu=0,ebitda=6539),
 dict(name='Chambal',sector='Fertilisers',cn='3102 10 urea',bm=None,dflt=2.17,see=None,ind=0,eu=0,ebitda=2679),
 dict(name='Coromandel',sector='Fertilisers',cn='3105 30 DAP',bm=None,dflt=0.81,see=None,ind=0,eu=0,ebitda=3232),
]
def cost(f,y,price='base',fa=FA_LAW,stress=False,use_default=False,india=0,passthru=1.0):
    if f['eu']==0 or f['bm'] is None: return 0,0
    see = f['dflt']*(1+mk(y,f['sector'])) if use_default else f['see']
    if stress: see += f['ind']
    net = max(see - f['bm']*fa[y],0)
    eur = f['eu']*net*max(PRICE[price][y]-india,0)*passthru
    cr = eur*EURINR/1e7
    return cr, cr/f['ebitda']*100
out={}
for f in firms:
    r={}
    for case,kw in {'base':{},'default':{'use_default':True},'stress':{'stress':True},'high':{'price':'high'},'proposal':{'fa':FA_PROP}}.items():
        r[case]={y:[round(v,1) for v in cost(f,y,**kw)] for y in YEARS}
    out[f['name']]=r
    b=r['base'];d=r['default'];s=r['stress']
    print(f"{f['name']:11s} base 2026 {b[2026]} 2030 {b[2030]} 2034 {b[2034]} | default 2026 {d[2026]} 2030 {d[2030]} | stress 2030 {s[2030]} 2034 {s[2034]}")
# per-tonne
for f in firms[:4]:
    for y in (2026,2030,2034):
        net=max(f['see']-f['bm']*FA_LAW[y],0); dnet=max(f['dflt']*(1+mk(y,f['sector']))-f['bm']*FA_LAW[y],0)
        print(f['name'],y,'€/t actual',round(net*PRICE['base'][y]),'€/t default',round(dnet*PRICE['base'][y]))
# total 9yr savings from verified data
for f in firms[:4]:
    a=sum(out[f['name']]['base'][y][0] for y in YEARS); d=sum(out[f['name']]['default'][y][0] for y in YEARS)
    print(f['name'],'cum 2026-34 base cr',round(a),'default',round(d),'saving',round(d-a))
json.dump(out,open('model_out.json','w'))
