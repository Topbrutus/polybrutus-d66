# Polybrutus 66D: Exact 71-point Euclidean metric and a sixtyfold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible synthetic case study**
**AI disclosure:** OpenAI ChatGPT (Astra) materially assisted two independently implemented exact rational verifiers, mathematical manuscript and controlled publication. AI is not the human scientific author.

## Abstract

We construct one exact labelled synthetic Euclidean squared-distance metric on 71 norm-one points through a conservative orthogonal unit-vector extension of the original immutable Polybrutus D65 [1]. All 2415 predecessor labelled squared distances remain unchanged; 70 new squared distances each equal 2R², producing 2485 unordered labelled pairs. The centered exact rational Euclidean Gram is PSD with rank 66, proving minimum affine Euclidean realization dimension 66 for this specified metric. For a separately freely stipulated ideal equal-scalar-mass weighted complete graph with w_ij=1/d_ij², rational Laplacian eigenspace ranks yield eigenvalue 71/2 multiplicity 60 and 35 multiplicity 4. Two independently implemented rational programs verify all 2485 pair labels, all 2415 authentic inherited parent labels, centered Gram rank, ideal graph nullities, and frozen full parent scientific source. No physical discovery or empirical measurement is claimed.

## 1. Immutable immediate parent and exact distance conservation

The sole direct scientific predecessor is St-Pierre, Polybrutus D65 [1], DOI 10.5281/zenodo.24432568, scientific frozen Git tag Topbrutus/polybrutus-d65@v0.1.0 at real peeled commit 32fb982037750653f416546ba721333011532adc. Its **entire original Git scientific source ZIP** is preserved byte-identically at prior/d65/frozen_scientific_tag_v0.1.0.zip, size 4390926 bytes with 32 entries and ZIP CRC PASS, SHA256 cf71e7db552567b3ff7383ccfcc4f8bb042da354896473d77588a91db36d0cc0. All earlier original scientific source archives remain nested unchanged. The original D65 deterministic certificate is copied byte-identically at prior/d65/results/certificate_d65.json, SHA256 f772b6e713bc2cc0a713ffbf6d5fa1d0960384c808c811700f87e93bf3801bd5. Both independent checkers authenticate source ZIP SHA/CRC, certificate bytes and all 2415 old labelled pairs.

Let p_i (i=1,...,70) be parent norm-one vectors and embed them by q_i=(p_i,0) into larger Euclidean coordinates. Append new perpendicular norm-one q_71. Then each old labelled squared distance remains unchanged, ||q_i-q_j||²=||p_i-p_j||². All 70 new squared distances satisfy ||q_71-q_i||²=2R². Thus C(71,2)=2485=2415+70 exact labelled unordered pairs. This is a constructed synthetic metric, not evidence for new physical spacetime dimensions.

## 2. Rational Gram PSD, exact affine rank and labelled histogram

Construct Gram G over rationals as an orthogonal sum of the seven canonical norm-one point Gram (rank 3), a centered regular five-point unit simplex with mutual inner products -1/4 (rank 4), and 59 independent perpendicular norm-one axes (rank 59). Hence G=XXᵀ is PSD with unit diagonal and rank 3+4+59=66. Define D_ii=0, D_ij=2-2G_ij and H=I-11ᵀ/71. The centered Euclidean Gram B=-(HDH)/2=HGH is PSD of exact rank 66. The inherited canonical antipodal pair puts the origin in the affine hull; the minimum affine Euclidean realization dimension for this metric is therefore 66, using 67 coordinate storage.

At R=1, exhaustive normalized histogram k=4d²/R² is 4:6, 7:2, 8:2454, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 2485 unordered labelled pairs. Their exact sum of squared distances is 19927/4. Both programs verify all 2415 parent pair values by their exact original labels; histogram equality alone would not be an adequate conservation proof.

## 3. Separately specified ideal graph and rational spectral eigenspaces

We stipulate unit scalar masses and symmetric positive complete-graph edge weights w_ij=1/d_ij². The new perpendicular norm-one vertex joins all 70 old vertices with edge weight 1/2. The ideal Laplacian block is L66=[[L65+I70/2,-1_70/2],[-1_70ᵀ/2,70/2]]. Its characteristic polynomial satisfies chi71(z)=z(z-71/2)chi70(z-1/2)/(z-1/2). With the inherited seven-point core factor f6(z)=chiP7(z)/z, the chosen-model expression is chi71(z)=z(z-71/2)^60(z-35)^4*f6(z-32).

Independent exact rational rank-nullity for this Laplacian establishes eigenvalue 71/2 multiplicity 60 and 35 multiplicity 4. These are mathematically dimensionless eigenmodes of a freely chosen ideal graph, not measured acoustic or electromagnetic hertz, particles, or physical extra dimensions.

## 4. Two independent implementations and adversarial negative controls

Primary src/verify_d66.py constructs exact Gram G with SymPy, exhausts all 2485 labelled squared distances, independently authenticates parent complete ZIP SHA256/CRC and byte-identical original certificate, compares all 2415 inherited D65 labels, and computes centered Gram and ideal graph eigenspace ranks. Independent tests/independent_d66.py uses separate Python fractions.Fraction distance rules without importing the first program's Gram builder, and independently recomputes every pair label, centered rank and model eigenvalues. Both output the identical deterministic JSON results/certificate_d66.json with matching SHA256.

Four adversarial primary negative controls detect a corrupted new squared distance, duplicate final point, nonperpendicular tilted but norm-one added point, and histogram-preserving pair relabelling. Independent tests separately reject corrupted labels and histogram-preserving relabelled metrics.

The original D47 certificate carries an inaccurate textual D46 grandparent Git commit, disclosed since D48; historical source archives remain unmodified and the actual direct D65 scientific frozen tag is authenticated separately.

## 5. Reproducibility, DOI relationship and scientific boundaries

Python 3.12 and sympy==1.14.0 reproduce the exact calculations. Orthogonal norm-one vector extension and complete graph joins are standard mathematical constructions. This preprint proves properties of this constructed synthetic metric and the separately selected ideal graph, not a novel universal law, independently human-peer-reviewed experimental result, physical particle, measured hertz or extra physical spacetime dimension.

Zenodo metadata must contain nine current D66 keywords including sixty-six and sixtyfold, structured isDerivedFrom to immediate direct D65 DOI 10.5281/zenodo.24432568, and separate bibliographic references to D65 [1] and historical D7 [2]. All three public scientific tag ZIP, PDF and certificate JSON originals must match filenames, exact sizes and public MD5 against source SHA256.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 65D: Exact 70-Point Euclidean Metric and Fifty-Ninefold Ideal Graph Mode. Zenodo DOI 10.5281/zenodo.24432568. https://doi.org/10.5281/zenodo.24432568

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo DOI 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Full original Polybrutus D65 frozen scientific source Git tag v0.1.0, https://github.com/Topbrutus/polybrutus-d65/tree/v0.1.0, peeled commit 32fb982037750653f416546ba721333011532adc, original source ZIP preserved unchanged.
