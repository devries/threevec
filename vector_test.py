#!/usr/bin/env python
import threevec.vector as vector
import unittest
import math

class TestForKnownOperations(unittest.TestCase):
    def setUp(self):
        self.testing_vectors = (vector.Threevec(1,2,3),
                vector.Threevec(1.0,2.0,3.0),
                vector.recvec(-1.0,1.0,0.0),
                vector.sphvec(5.0,math.pi,math.pi),
                vector.cylvec(10.0,0.0,3.0),
                vector.i,
                vector.j,
                vector.k)

    def test_basis_cross_products(self):
        """Cross products of the basis vectors i, j, and k should give known responses."""
        self.assertEqual(vector.i%vector.j,vector.k)
        self.assertEqual(vector.j%vector.k,vector.i)
        self.assertEqual(vector.k%vector.i,vector.j)
        self.assertEqual(vector.j%vector.i,-vector.k)
        self.assertEqual(vector.k%vector.j,-vector.i)
        self.assertEqual(vector.i%vector.k,-vector.j)

    def test_self_dot_product(self):
        """Dot products of vectors with self should give magnitude squared."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(v*v,abs(v)**2)

    def test_self_cross_product(self):
        """Cross products of vectors with self should have magnitude of 0.0."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(abs(v%v),0.0)

    def test_ninety_degree_rotation(self):
        """Basis vector i rotated 90 degrees around k should yield j."""
        self.assertAlmostEqual(vector.i.rotate(vector.k,math.pi/2.0),vector.j)

    def test_spherical_rotation(self):
        """Rotating about the k axis is equivalent to changing phi."""
        v_original = vector.sphvec(2.0,math.pi/3.0,0.0)
        rotation = math.pi/4.0
        v_new = v_original.rotate(vector.k,rotation)
        self.assertAlmostEqual(v_new.phi,rotation)

    def test_two_pi_rotation(self):
        """A rotation by 2 pi around any axis yields the original vector."""
        v_axis = vector.recvec(-1.0,1.0,4.0)
        for v in self.testing_vectors:
            self.assertAlmostEqual(v.rotate(v_axis,2.0*math.pi),v)

    def test_self_subtracted_vectors(self):
        """A vector minus itself has a magnitude of 0."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(abs(v-v),0.0)

    def test_double_vector(self):
        """A vector plus itself has twice the magnitude."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(abs(v+v),2.0*abs(v))

    def test_unit_phis(self):
        """Unit vectors in the direction of each vector have the same spherical phi."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(v.unit().phi,v.phi)

    def test_unit_thetas(self):
        """Unit vectors in the direction of each vector have the same spherical theta."""
        for v in self.testing_vectors:
            self.assertAlmostEqual(v.unit().theta,v.theta)

    def test_magnitude_greater(self):
        """A vector multiplied by 3.0 should have a greater magnitude."""
        for v in self.testing_vectors:
            self.assertGreaterEqual(abs(3.0*v),abs(v))

    def test_magnitude_lesser(self):
        """A vector divided by 3.0 should have a lesser magnitude."""
        for v in self.testing_vectors:
            self.assertLessEqual(abs(v/3.0),abs(v))

    def test_no_zero_length_unit_vector(self):
        """Test that calling unit() on a zero length vector throuws a ZeroDivisionError."""
        v = vector.Threevec()
        self.assertRaises(ZeroDivisionError,v.unit)

    def test_theta_not_defined_for_zero_vector(self):
        v = vector.Threevec()
        with self.assertRaises(ZeroDivisionError):
            v.theta

if __name__ == '__main__':
    unittest.main()
    
