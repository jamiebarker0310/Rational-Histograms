import unittest
import rationalHistogram.rationalHistogram as rh 
import numpy as np

class TestRH(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRH, self).__init__(*args, **kwargs)
        mu = np.random.uniform(low=-100, high = 100)
        std = np.random.uniform(low=0, high = 100)
        n = np.random.randint(5,high=10**6)
        data = np.random.normal(loc = mu, scale = std, size=(n))
        self.bins = rh.getBins(data)
        
    def test_bend(self):
        x = list(range(10))
        y = [1 for i in range(10)]
        self.assertAlmostEqual(rh.calculateBend(x,y), 0)
    
    def test_bend1(self):
        x = list(range(10))
        y = list(range(10))
        self.assertAlmostEqual(rh.calculateBend(x,y), 0)
    
    def test_freedmanDiaconus(self):
        x = [1,2,3,4,5,6,7,8]
        np_bins = np.histogram_bin_edges(x, bins='fd')
        np_bin_width = np_bins[1] - np_bins[0]
        self.assertEqual(rh.freedmanDiaconus(x), np_bin_width)

    def test_getBinsRational(self):
        remainders= []
        bin_width = self.bins[1] - self.bins[0]
        for base_val in rh.baseVals():
            remainders.append(np.log10(bin_width/base_val) % 1)
        self.assertEqual(min(remainders), 0)
    
    def test_getBinsLengty(self):
        minbin = rh.minBin()
        self.assertGreaterEqual(len(self.bins), minbin)

        



if __name__ == "__main__":
    unittest.main()