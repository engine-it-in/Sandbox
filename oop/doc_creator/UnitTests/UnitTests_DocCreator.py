import unittest
from OOP.DocCreator.Draft import CollectionRoot


class CollectionRootTest(unittest.TestCase):
    def Test_CollectRoot(self):
        self.assertEquals(CollectionRoot.CollectRoot())


if __name__ == '__main__':
    unittest.main()
