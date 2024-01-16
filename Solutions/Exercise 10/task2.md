# Task 2. Backpropagation (6 points)

Given the following neural network:
![Feed-Forward Neural Network](ffnn.png)

## a) Calculate the output for the following inputs i1 = 5 and i2 = 2. The output function is the identity function. (0.5
P.)

$$net_{h_1} = i_1 * 5 + i_2 * 4 = 25 + 8 = 33$$
$$net_{h_2} = i_1 * -3 + i_2 * 1 = -15 + 2 = -13$$
$$out_{o_1} = h_1 * 2 + h_2 * -2 = 66 + 26 = 92$$

## b) Calculate the error (MSE) for the input from part a). The actual output for the input is 100 (0.5 P.)

$$MSE = (92-100)^2 = 64$$

## c) Apply the Backpropagation algorithm once and update all weights of the network. Use a learning rate of 0.0005. Calculate the output and error again for the input from part a). (4 P.)

$w_i$ is the $i$-th weight reading left to right, top to bottom

Initial:
$$w_1 = 5,
w_2 = -3,
w_3 = 4,
w_4 = 1,
w_5 = 2,
w_6 = -2$$

Calculation:
$$w_i'=wi-n\frac{\delta E}{\delta w_i}=w_i-n\frac{\delta E}{\delta p}*\frac{\delta p}{\delta wi}$$
$$n = 0.0005,
p = 92,
a = 100,
E = \frac{1}{2}(p-a)^2$$

### Calculate $w_i'$ layer by layer backwards

#### Hidden nodes
$$\frac{\delta E}{\delta p}*\frac{\delta p}{\delta w_6}
=\frac{\frac{1}{2}(p-a)^2}{\delta p}*\frac{h_1*w_5+h_2*w_6}{\delta w_6}
=2*\frac{1}{2}(p-a)\frac{\delta (p-a)}{\delta p}*h_2
\overset{\Delta=p-a}{=} \Delta h_2$$
$$\implies w_6'=w_6+n*\Delta*h_2 =-2-.0005*-8*-13=-2.052$$
Analogue $w_5$
$$\implies w_5'=w_5+n*\Delta*h_1 =-2-.0005*-8*33=-2.132$$
## d) How would your result change if you increased or decreased the learning rate by a factor of 10? (0.5 P.)

## e) What would happen if you initialized all weights with 0? (0.5 P.)