## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import os, sys
sys.path.append( os.path.join( os.getcwd( ), '../../lib/python3' ) )

import numpy
import PUJ.Model.Logistic, PUJ.Regression.MaximumLikelihood
import PUJ.Normalize, PUJ.Optimizer.GradientDescent
import PUJ.Debug.Labeling

print('!'*8)

## -------------------------------------------------------------------------
learning_rate = 1e-4
maximum_iterations = 100000
epsilon = 1e-8
debug_step = 1000
init_theta = numpy.random.rand( 1, 3 ) * 1e-1

## -------------------------------------------------------------------------

## Read data
# D = numpy.loadtxt( open( sys.argv[ 1 ], 'rb' ), delimiter = ',' )
csv_data = numpy.loadtxt(
  open('/Users/Gio0/Develop/Python/Buscaminas/PUJ_ML/examples/python3/algo.csv', 'rb'),
  delimiter=','
)

# numpy.random.shuffle(csv_data)

## -- Separate X and y
x0 = csv_data[:, :-1]
y0 = numpy.matrix(csv_data[:, -1]).T

# Prepare regression
x0, x0_off, x0_div = PUJ.Normalize.Standardize(x0)
cost = PUJ.Regression.MaximumLikelihood( x0, y0 )

# Prepare debug
debug = PUJ.Debug.Labeling(x0[:, 0: 2], y0)
print('#'*8)
# Iterative solution
tI, nI = PUJ.Optimizer.GradientDescent(
  cost,
  learning_rate=learning_rate,
  init_theta=init_theta,
  maximum_iterations=maximum_iterations,
  epsilon=epsilon,
  debug_step=debug_step,
  debug_function=None
  )

print( '=================================================================' )
print( '* Iterative solution   :', tI )
print( '* Number of iterations :', nI )
print( '=================================================================' )

debug.KeepFigures( )

## eof - $RCSfile$

if __name__ == "__main__":
  print('Stating')
