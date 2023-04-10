<h1>QBFFam</h1>

<h2>Description</h2>

qbffam is a generator for QBF benchmarks in QDIMACS format
that currently supports 12 formula families of crafted formula instances
from QBF proof complexity

<h2>Usage</h2>

python qbffam.py &lt;family&gt; &lt;n&gt;

where 
<ul>
<li>&lt;family&gt; is one of the following formula families</li>
<li>&lt;n&gt; is the size of the generated formula (parameter common to all families)</li>
</ul>

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
<li>KBKFTrue:    Kleine Buening et al Formulas - Satisfiable</li>
<li>PARITYTrue:  Parity Formulas - Satisfiable</li>
<li>KBKFQRE:     Kleine Buening et al Formulas - Satisfiable and quantifier rearranged</li>
</ul>


