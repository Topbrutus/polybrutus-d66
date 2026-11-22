#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d66.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==66
assert c['vertices']==m['norm_one_vertices']==71
assert c['pairs']==m['exact_labelled_squared_pairs']==2485
assert c['affine_rank']==c['centered_gram_rank']==66
assert c['eigenvalue_71_over_2_multiplicity']==m['model_eigenvalue_71_over_2_multiplicity']==60
assert c['eigenvalue_35_multiplicity']==m['model_eigenvalue_35_multiplicity']==4
assert c['parent_tag_commit']=='32fb982037750653f416546ba721333011532adc'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24432568'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24432568','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-six' in m['keywords']
assert 'sixtyfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24432568' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty-five','fifty-ninefold ideal eigenvalue','affine Euclidean dimension sixty-seven','sixty-onefold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_66D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24432568','10.5281/zenodo.24407952'))
print('D66_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D65_PARENT_AND_SEPARATE_D65_D7_REFERENCES_PASS')
