from synapse.tests.common import *

import synapse.lib.thishost as s_thishost

class ThisTest(SynTest):

    def test_thishost_hostname(self):
        self.assertIsNotNone( s_thishost.get('hostname') )

    def test_thishost_ptrsize(self):
        self.assertIsNotNone( s_thishost.get('ptrsize') )

    def test_thishost_platform(self):
        self.assertIsNotNone( s_thishost.get('platform') )
