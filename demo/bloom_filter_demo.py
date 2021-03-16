from pybloom import BloomFilter, ScalableBloomFilter
bf = BloomFilter(capacity=10000, error_rate=0.001)
bf.add('test')
print('test' in bf)
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
sbf.add('dddd')
print('ddd' in sbf)