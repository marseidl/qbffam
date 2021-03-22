#QBFFam

##Description

qbffam is a generator for QBF benchmarks in QDIMACS format
that currently supports 12 formula families of crafted formula instances
from QBF proof complexity

#Usage

python qbffam.py <family> <n>

where 

<n> is the size of the generated formula (parameter common to all families)
<family> is one of the following formula families 

EQ          Equalities
EQ2         Squared Equalities
CP          Completion Principle
TRAP        Trapdoor Familiy
LONSING     Lonsing familiy
BEQ         Blocked Equality Formula
PARITY      Parity Formulas
LQ_PARITY   Variation of Parity Formulas hard for LD
QU_PARITY   Variation of Parity Formulas hard for QU
KBKF        Kleine Buening et al Formulas
KBKF_QU     Variation of Kleine Buening et al Formulas hard for QU
KBKF_LD     Variation of Kleine Buening et al Formulas hard for LD



