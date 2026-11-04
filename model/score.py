W=dict(emis=.35,trans=.25,disc=.20,eff=.20)
# emissions pillar: position within sector band (best -> 100, worst -> 0)
band={'Steel':(1.37,4.28),'Aluminium':(4.0,20.0),'Cement':(0.45,0.80),'Fertilisers':(None,None)}
firms={
 'Tata Steel':dict(s='Steel',i=2.45,trans=70,disc=90,eff=60,tier='A'),
 'JSW Steel':dict(s='Steel',i=2.36,trans=75,disc=85,eff=55,tier='A'),
 'Hindalco':dict(s='Aluminium',i=19.6,trans=65,disc=70,eff=45,tier='B'),
 'NALCO':dict(s='Aluminium',i=19.5,trans=25,disc=40,eff=30,tier='C'),
 'UltraTech':dict(s='Cement',i=0.578,trans=90,disc=90,eff=80,tier='A'),
 'Ambuja':dict(s='Cement',i=None,trans=85,disc=70,eff=70,tier='B'),
 'Chambal':dict(s='Fertilisers',i=None,trans=30,disc=50,eff=70,tier='C'),
 'Coromandel':dict(s='Fertilisers',i=None,trans=25,disc=50,eff=50,tier='C'),
}
for n,f in firms.items():
    lo,hi=band[f['s']]
    e = 50 if f['i'] is None else max(0,min(100,100*(hi-f['i'])/(hi-lo)))
    sc = W['emis']*e+W['trans']*f['trans']+W['disc']*f['disc']+W['eff']*f['eff']
    print(f"{n:11s} emis {e:5.1f} total {sc:5.1f} tier {f['tier']}")
