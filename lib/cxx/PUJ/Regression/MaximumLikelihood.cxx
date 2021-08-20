// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <cassert>
#include <PUJ/Regression.h>
#include <PUJ/Model.h>

// -------------------------------------------------------------------------
template< class _TScalar >
PUJ::Regression::MaximumLikelihood< _TScalar >::
MaximumLikelihood( const TMatrix& X, const TMatrix& y )
  : Superclass( X, y )
{
  this->m_Eps = TScalar( 1e-8 );
  this->m_Xby = ( this->m_X.array( ) * this->m_y.array( ) ).colwise( ).mean( );
  this->m_uy = this->m_y.mean( );
}

// -------------------------------------------------------------------------
template< class _TScalar >
typename PUJ::Regression::MaximumLikelihood< _TScalar >::
TScalar PUJ::Regression::MaximumLikelihood< _TScalar >::
CostAndGradient( TRowVector& gt, const TRowVector& theta )
{
  using _TModel = PUJ::Model::Logistic< TScalar >;

  _TModel model( theta.block( 0, 1, 0, theta.cols( ) ), theta( 0, 0 ) );
  TMatrix z = model( this->m_X );
  TScalar p;
  TScalar n;

  gt( 0, 0 ) = z.mean( ) - this->m_uy;
  gt.block( 0, 1, 0, gt.cols( ) ) =
    ( this->m_X.array( ) * z.array( ) ).colwise( ).mean( ) - this->m_Xby;
  

  return( -( p + n ) / TScalar( this->NumberOfExamples( ) ) );

  /* TODO
     p = numpy.log(
     z[ numpy.where( self.m_y[ : , 0 ] == 1 )[ 0 ] , : ] + self.m_Eps
     ).sum( )
     n = numpy.log(
     1 - z[ numpy.where( self.m_y[ : , 0 ] == 0 )[ 0 ] , : ] + self.m_Eps
     ).sum( )

     J = -( p + n ) / self.m_M


     dw = numpy.matrix(
     ( numpy.array( self.m_X ) * numpy.array( z ) ).mean( axis = 0 ) -
     self.m_Xby
     )
  */
}

// -------------------------------------------------------------------------
#include <PUJ_ML_export.h>
template class PUJ_ML_EXPORT PUJ::Regression::MaximumLikelihood< float >;
template class PUJ_ML_EXPORT PUJ::Regression::MaximumLikelihood< double >;
template class PUJ_ML_EXPORT PUJ::Regression::MaximumLikelihood< long double >;

// eof - $RCSfile$
