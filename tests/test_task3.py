import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/fold_depth.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):

        def rows(depth):
            return [dict(time_days=(i+.5)/100,magnitude=10+(depth if i%100<10 else 0),sector='1',quality='0') for i in range(400)]
        self.assertFalse(m['screen'](rows(1),1,0,1)['flag'])
        self.assertTrue(m['screen'](rows(.1),1,0,1)['flag'])
        self.assertIsNone(m['screen'](rows(.1)[:20],1,0,1)['flag'])
        with self.assertRaises(ValueError):m['screen']([],0,0,1)

if __name__=="__main__":unittest.main()
