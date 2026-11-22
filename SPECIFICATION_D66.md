# Polybrutus D66 — exact 71-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d65@v0.1.0, actual peeled scientific Git commit \`32fb982037750653f416546ba721333011532adc\`, DOI 10.5281/zenodo.24432568, original full source ZIP SHA256 \`cf71e7db552567b3ff7383ccfcc4f8bb042da354896473d77588a91db36d0cc0\`, original D65 certificate SHA256 \`f772b6e713bc2cc0a713ffbf6d5fa1d0960384c808c811700f87e93bf3801bd5\`.

## Conservative perpendicular norm-one extension

Embed all 70 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_71. Every one of C(70,2)=2415 old labelled squared distances remains unchanged; all 70 new squared distances equal 2R². Total C(71,2)=2485 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **59** independent mutually orthogonal norm-one axes (rank 59). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+59=66**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/71, B=-(HDH)/2=HGH is PSD of rank **66**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 66 (67 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2454, 9:3, 10:10, 12:6, 13:2, 16:2; total 2485. Exact sum of squared pair distances R=1: **19927/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 70 old points with weight 1/2. The chosen ideal Laplacian is L66=[[L65+I70/2,-1_70/2],[-1_70ᵀ/2,70/2]]. Its characteristic recurrence is chi71(z)=z(z-71/2)chi70(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi71(z)=z(z-71/2)^60(z-35)^4*f6(z-32).
Exact rational nullities yield Laplacian eigenvalue **71/2 multiplicity 60**, and **35 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D65 DOI 10.5281/zenodo.24432568; historical D7 DOI 10.5281/zenodo.24407952.
