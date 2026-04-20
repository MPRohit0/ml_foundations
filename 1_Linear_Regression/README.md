# Linear Regression

This is one of the most simple and intuitive machine learning algorithms. 

In this algorithm we plot all the points on a graph and try to plot a line whose values have the least error from the original. This is called the "Bestfit line"

error:
`error = predicted value - actual value`

Line:
$$Y = mx+c$$
m - slope / coefficient \
c - intercept / bias

## Mathematical Setup
Let us assume h(x) to be our line function. 

$$h_{\theta}(x) = \theta_0+\theta_1x_1+\dots+\theta_{n}x_{n}$$

i.e. hypothetical function = bias + 1st parameter / 1st coefficient (1st feature) + 2nd parameter / 2nd coefficient (1st feature) + ...... and so on as required by number of parameters.

so the error will be: 

$$ error = \sum_{i=1}^{n}h_{\theta}(x^{(i)})-y^{(i)}$$

where, y^(i) is the actual value

cost function is a function which tells us how "costly" a function is i.e. gives us a quantified value on how our algorithm is performing compared to the actual data.

Generally, we take MSE (mean square error) as a cost function. This is because we don't care if the error is negative or positive. We are just trying to minimise the magnitude of errors. so, let's just stick to it.

In our algorithm we are trying to "minimise" our error.  

let consider the following as our MSE: 

$$J(\theta) = \frac{1}{n}\sum_{i=1}^{n}(h_{\theta}(x^{(i)})-y^{(i)})^2$$

## Mathematical Derivation
Gradient decent:
In multi-variable calculus, the gradient of a function points to the direction of maximum ascent of that function. We are trying to "minimise". so, we can just take the negative gradient of a function i.e. direction of maximum descent.

but we only have a direction. so, we assume a step size also called the learning rate. and we move with that amount of steps. We use these steps to update our value. 

$$\theta_{k} = \theta_{k} - \alpha  j(\frac{\partial{j(\theta_{k})}}{\partial{\theta_{k}}})$$

theoretically, we continue till our gradient is 0. but, practically we reach very close to 0 and end it there.









