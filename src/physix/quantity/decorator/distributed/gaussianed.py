from mathx.probability.covariance_matrix import CovarianceMatrix
from mathx.probability.distribution.gaussian.distribution import Distribution
from physix.quantity.decorator.decorator import Decorator
from physix.quantity.quantifiable import Quantifiable


class Gaussianed(Decorator):
    def __init__(self, inner:Quantifiable, cov_matrix:CovarianceMatrix):
        super().__init__(inner)
        self._gaussian_distribution = Distribution(self._inner, cov_matrix)

    def get_distribution(self)->Distribution:
        return self._gaussian_distribution