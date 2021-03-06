Optimization by Gradient Descent
================================

This optimizer varies a list of input variables x1, x2, ... xn in order to find a minimum for an target function func(x1, x2, ...xn).

The optimizer supports min/max limits of the input variables and inputs that can only be integers.

The optimization process either starts at a given point of initial input values or does a grid search in the input space to increase the probability to find a global optimum instead of a local one. It supports an automatic learning rate adjustment via backtracking line search, autmatic zoom-in for fine tuning as well as an adjustable momentum.

Using the optimizer involves four steps:

#### 1. Create any number of Parameter() objects by using the constructor:


    Parameter (name, initial_value=None, min=None, max=None, grid=None, integral=False, dx=None)

The meaning of these parameters:

- name: identifies the parameter
- initial_value: where the search will start. Either initial_value or a grid must be specified
- min/max: limits for this input
- grid: an integer specifying the number of intervals between min and max. The midpoint in each of these intervals will be a start point for optimization. If multiple parameters have grids, their cartesian product will be used. 
- integral: if True, the input is an integer
- dx: the (initial) increment to estimate the gradient at a certain point by (f(x + dx) - f(x)) / dx
  
  Must be specified if initial_value is zero. Otherwise, dx defaults to initial_value * 0.001

#### 2. Create an optimizer instance by using the constructor:

    Optimizer (function, args='enum', zoom_limit=1e6, cfactor=0.5, momentum=0, iterations=100, min_improvement=0, trace=False, debug=False)

The meaning of these parameters:

- function: the target function
- args: the way the parameters will be passed to the function. If there are two parameters x and y, there are the following options:
  - args='enum': function(x, y)
  - args='kwargs': function(x=x, y=y)
  - args='dict': function(params) with x=params['x'] and y=params['y']
  - args='list': function(params) with x=params[0] and y=params[1]
- cfactor: control parameter in the Armijo condition for the backtracking line search algorithm
- zoom_limit: if applying the steps doesn't improve the result any more, learning as well as the dx for calculating the gradient will be divided by an ever increasing zoom factor. This parameter limits the zooming process.
- momentum: if momentum > 0, the (momentum * last_step) is added to the current step
- iterations: maximum number of iterations
- min_improvement: iteration is stopped early if per-iteration improvement is less than this value
- trace/debug: print some output during iterations

#### 3. add the parameters to the optimizer:

    opt.add_par (param1)
    opt.add_par (param2)
    ...

#### 4. invoke the calculation:

    res = opt.optimize()
    # res[0] will contain a dictionary of the optimal parameter values
    # res[1] will conmtain the function value at this point 

    
