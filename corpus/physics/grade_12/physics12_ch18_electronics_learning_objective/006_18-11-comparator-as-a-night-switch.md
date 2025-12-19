### 18.11 COMPARATOR AS A NIGHT SWITCH

Suppose it is required that when intensity of light falls below a certain level, the street light is automatically switched on. This can be accomplished by using op-amp as a comparator. In Fig. 18.33 resistances $R_{1}$ and $R_{2}$ form a potential divider. The potential drop across $R_{2}$ provides the reference voltage $V_{R}$ to the $(+)$ input of the op-amp. Thus

$$
V_{R}=\frac{R_{2}}{R_{1}+R_{2}} \times V_{C C}
$$

LDR is a light dependent resistance. The value of its resistance $R_{L}$ depends upon the intensity of light falling upon it. $R_{1}$ and $R_{2}$ form another potential divider. The potential drop across $R_{3}$ is $V^{\prime}$ which is given by

$$
V^{\prime}=\frac{R_{3}}{R_{L}+R_{3}} \times V_{C C}
$$

$V^{\prime}$ provides the voltage to (-) input of the op-amp. $V^{\prime}$ will not be

a constant voltage but it will vary with the intensity of light. During day time, when light is falling upon LDR, $R_{L}$ is small. According to Eq.18.9, $V^{\prime}$ will be large such that $V^{\prime}>V_{0}$ so that $V_{0}=-V_{c c}$. The output of the op is connected with a relay system which energizes only when $V_{0}=+V_{c c}$ and then it turns on the street lights. Thus when $V_{0}=-V_{c c}$, the light will not be switched ON.

As it gets darker, $R_{L}$ becomes larger and $V^{\prime}$ decreases. When $V^{\prime}$ becomes just less than $V_{0}$, the output of op-amp switches to $+V_{c c}$ which energizes the relay system and the street lights are turned ON.

# 18.12 DIGITAL SYSTEMS

A digital system deals with quantities or variables which have only two discrete values or states. Following are the examples of such quantities.
(i) A switch can be either open or closed.
(ii) The answer of a question can be either yes or no.
(iii) A certain statement can be either true or false.
(iv) A bulb can be either off or on.

Various designations are used to represent the two quantized states of such quantities. The most common of these are listed in Table 18.1.

| Table 18.1 |  |  |  |  |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| One of the states | True | High | 1 | Yes | On | Closed |
| The other state | False | Low | 0 | No | Off | Open |

Mathematical manipulation of these quantities can be best carried if they are represented by binary digits 1 and 0 . When we are dealing with voltages, designation No. 2 is also a convenient representation.
In describing functions of digital systems a closed switch will be shown as 1 and open switch will be shown as 0 . Similarly, a lighted bulb will be described as 1 and an off bulb will be described as 0 .
Just as we require two basic mathematical operations, i.e., addition and subtraction for the mathematical manipulation

Fig. 18.34
Fig. 18.35

| Table 18.2 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

Fig. 18.36
| Table 18.3 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

of ordinary quantities which can possess all continuous values, we require a special algebra, known as Boolean algebra for the manipulation of the quantities which have values 1 and 0 , now designated as Boolean variables. Boolean algebra is based upon three basic operations namely (i) AND operation, (ii) OR operation and (iii) NOT operation. You have already read about these operations. Here we would study about logic gates which implement these operations.

# 18.13 FUNDAMENTAL LOGIC GATES

The electronic circuits which implement the various logic operations are known as logic gates. In these gates the high and low states, i.e., 1 and 0 states are simulated by certain voltage levels. Ideally one particular voltage level represents a high (1) and another voltage level represents a low (0). In practical digital circuits, however a 1 or high can be any voltage between a specified minimum value and a specified maximum value. Likewise 0 or low can be any voltage between a specified minimum and a specified maximum. Fig. 18.34 shows the range 1 and 0 levels for a certain type of digital gates. Thus if voltage of 3.5 V is applied to a gate, it will accept it as high or 1 . If a voltage of 0.5 V is applied, the gate will recognize it as 0 or low.

## OR Gate

OR gate as symbolically represented in Fig.18.35, implements the logic of OR operation. It has two or more inputs and a single output $X$. The output has a value 1 when at least one of its inputs $A$ and $B$ is at 1 . Thus $X$ will be zero only when both the inputs are 0 . Thus it implements the truth table of OR operation (Table 18.2). The mathematical notation for OR operation is

$$
X=A+B
$$

## AND Gate

The AND gate shown in Fig. 18.36 has two or more inputs and a single output. It is designed such that it implements the truth table of AND operation, i.e., its output $X$ is 1 only when both of its inputs $A$ and $B$ are at 1 and for all other combinations of the values of $A$ and $B, X$ is zero (Table 18.3). The mathematical notation for AND operation is

$$
X=A \cdot B
$$

## NOT Gate

It performs the operation of inversion or complementation. That is why it is also known as inverter. It changes a logic level to its opposite level, i.e., it changes 1 to 0 and 0 to 1 . The symbolic representation of NOT gate is shown in Fig. 18.37. Whenever a bar is placed on any variable, it shows that the value of the variable has been inverted. For example $\overline{1}=0$ and $\overline{0}=1$. The "bubble" (o) in Fig. 18.37 indicates operation of inversion. Its truth table is given in Table 18.4. The mathematical notation for NOT operation is $\quad X=\bar{A}$