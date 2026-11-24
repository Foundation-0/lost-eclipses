import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/cache_manifest.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):

        with tempfile.TemporaryDirectory() as d:
            pathlib.Path(d,'curve').write_bytes(b'curve')
            rows=[dict(cache_path='curve',source_url='https://example.org/product',sector='1')]
            self.assertEqual(m['manifest'](rows,d)[0]['bytes'],5)
            with self.assertRaises(ValueError):m['manifest']([dict(rows[0],cache_path='../escape')],d)

if __name__=="__main__":unittest.main()
