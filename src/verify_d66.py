#!/usr/bin/env python3
"""Polybrutus D66: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D65 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=71
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==66
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==2485 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d65'/'results'/'certificate_d65.json'
parent_archive=ROOT/'prior'/'d65'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='cf71e7db552567b3ff7383ccfcc4f8bb042da354896473d77588a91db36d0cc0'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d65.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='f772b6e713bc2cc0a713ffbf6d5fa1d0960384c808c811700f87e93bf3801bd5'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==65 and parent['vertices']==70
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==2415
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,70]==2 for i in range(70))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:2454,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==2485
assert sum(D[i,j] for i,j in pairs)==Q(19927,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==66
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-Q(71,2)*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-35*s.eye(n)).to_field().rank()==67
old=s.zeros(70)
for i,j in combinations(range(70),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:70,:70]-old==s.eye(70)/2
assert all(L[i,70]==-Q(1,2) for i in range(70))
assert L[70,70]==35

# Four adversarial negative controls.
damaged=D.copy();damaged[0,70]=damaged[70,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[70,:]=G[69,:];duplicate[:,70]=G[:,69];duplicate[70,70]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==65
tilted_dot_to_old_core=Q(3,10)
assert Q(3,10)**2+Q(91,100)==1
assert tilted_dot_to_old_core!=0 and 2-2*tilted_dot_to_old_core!=D[0,70]
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D66-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':66,'vertices':71,'pairs':2485,
  'affine_rank':66,'centered_gram_rank':66,'ambient_storage_coordinates':67,
  'radius':1,'parent':'Topbrutus/polybrutus-d65@v0.1.0',
  'parent_tag_commit':'32fb982037750653f416546ba721333011532adc',
  'parent_doi':'10.5281/zenodo.24432568',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':2415,'new_distances':70,
  'new_squared_distances':['2']*70,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'19927/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_71_over_2_multiplicity':60,
  'eigenvalue_35_multiplicity':4,
  'spectral_recurrence':'chi71(z)=z*(z-71/2)*chi70(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi71(z)=z*(z-71/2)^60*(z-35)^4*f6(z-32), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d66.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D66 PASS: 71 vertices, 2485 labelled pairs, affine rank 66; 2415/2415 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 71/2 x60; eigenvalue 35 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
