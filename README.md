<h1>QBFFam</h1>

<h2>Description</h2>

qbffam is a generator for QBF benchmarks in QDIMACS format
that currently supports 12 formula families of crafted formula instances
from QBF proof complexity

<h2>Usage</h2>

python qbffam.py <family> <n>

where 

<n> is the size of the generated formula (parameter common to all families)
<family> is one of the following formula families 

<ul>
<li>EQ:          Equalities</li>
<li>EQ2:         Squared Equalities</li>
<li>CP:          Completion Principle</li>
<li>TRAP:        Trapdoor Familiy</li>
<li>LONSING:     Lonsing familiy</li>
<li>BEQ:         Blocked Equality Formula</li>
<li>PARITY:      Parity Formulas</li>
<li>LQ_PARITY:   Variation of Parity Formulas hard for LD</li>
<li>QU_PARITY:   Variation of Parity Formulas hard for QU</li>
<li>KBKF:        Kleine Buening et al Formulas</li>
<li>KBKF_QU:     Variation of Kleine Buening et al Formulas hard for QU</li>
<li>KBKF_LD:     Variation of Kleine Buening et al Formulas hard for LD</li>
</ul>


