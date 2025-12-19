### 18.14 OTHER LOGIC GATES

## NOR Gate

In NOR gate the output of OR gate is inverted. Its symbol is shown in Fig. 18.38 and its truth table is given in Table 18.5. The mathematical notation for NOR operation is

$$
X=\overline{A+B}
$$

## NAND Gate

In NAND gate the output of an AND gate is inverted. Its symbol is shown in Fig. 18.39. The bubble in this figure shows that the output of AND gate is inverted. The truth table implemented by it is shown in Table 18.6. The mathematical notation for NAND operation is

$$
X=\bar{A} \cdot \bar{B}
$$

## Exclusive OR Gate(XOR)

Consider a Boolean function $X$ of two variables $A$ and $B$ such that

$$
X=A \bar{B}+\bar{A} B
$$

The first term of the function $X$ is obtained by ANDing the variable $A$ with NOT of $B$. The second term is NOT of $A$ ANDed with B. The function $X$ is obtained by ORing these two terms. It can be constructed by combining AND, OR and NOT gates according to the scheme shown in Fig. 18.40(a). The
Fig. 18.40 (a)
Making an XOR gate
| Table 18.4 |  |  |
| :--: | :--: | :--: |
| A | Output |  |
| 0 | 1 |  |
| 1 | 0 |  |

| Table 18.5 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

| Input A |  | Output |
| :--: | :--: | :--: |
| Input B |  |  |
| NAND gate |  |  |
| Fig. 18.39 |  |  |
| Table 18.6 |  |  |
| A | B | Output |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Fig. 18.40 (b)
Fig. 18.41

| Table 18.8 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

value of this function can be obtained by drawing the truth table (Table 18.7) which gives the value of $X$ for all the values of the variables $A$ and $B$. The value of $X$ is 0 when the two inputs have the same values and it is 1 when the inputs have different values. It can be verified that the circuit of Fig. 18.40 (a) implements this truth table. The symbol of XOR gate is shown in Fig. 18.40(b).

## Exclusive-NOR gate (XNOR)

The exclusive NOR gate is obtained by inverting the output of a XOR gate. Its symbol is shown in Fig. 18.41. The bubble shown at the output in this figure shows that the output of XOR gate has been inverted. So its Boolean expression is given by

$$
X=\overrightarrow{A B}+\overrightarrow{A B}
$$

The truth table of XNOR gate is given in the Table 18.8. Its output is 1 when its two inputs are identical and 0 when the two inputs are different. Like XOR gate, it is also constructed by a combination of NOT, AND and NOR gates by the scheme shown in Fig. 18.42.
Fig. 18.42