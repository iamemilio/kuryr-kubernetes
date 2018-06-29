from oslo_versionedobjects import fixture, base
from kuryr_kubernetes.tests import base as test_base

object_data = {
     'FixedIP': '1.0-d1a0ec7e7b6ce021a784c54d44cce009',
     'FixedIPList': '1.0-15ecf022a68ddbb8c2a6739cfc9f8f5e',
     'HostInfo': '1.0-4dba5ce236ea2dc559de8764995dd247',
     'HostPluginInfo': '1.0-5204e579864981c9891ecb5d1c9329f2',
     'HostPortProfileInfo': '1.0-e0bc9228c1456b220830d67b05bc4bf2',
     'HostVIFInfo': '1.1-00fdbeba3f9bb3bd2a723c17023ba182',
     'InstanceInfo': '1.0-84104d3435046b1a282ac8265ec2a976',
     'LBaaSL7Policy': '1.0-3ac4fcd50a555f433a78c67cb6a4cd52',
     'LBaaSL7Rule': '1.0-276d9d678e1a8fc4b53fdbf3b2ac39ec',
     'LBaaSListener': '1.0-a9e2d5c73687f5edc66fdb2f48650e15',
     'LBaaSLoadBalancer': '1.2-d498ade2e705c3977eb66ff46133ed2b',
     'LBaaSMember': '1.0-a770c6884c27d6d8c21186b27d0e2ccb',
     'LBaaSPool': '1.1-6e77370d7632a902445444249eb77b01',
     'LBaaSPortSpec': '1.0-51dfa3436bec32db3614720056fcc83f',
     'LBaaSPubIp': '1.0-83992edec2c60fb4ab8998ea42a4ff74',
     'LBaaSRouteNotifEntry': '1.0-dd2f2be956f68814b1f47cb13483a885',
     'LBaaSRouteNotifier': '1.0-f0bfd8e772434abe7557930d7e0180c1',
     'LBaaSRouteState': '1.0-bdf561462a2d337c0e0ae8cb10e9ff20',
     'LBaaSServiceSpec': '1.0-d430ecd443f2b1999196bfe531e56f7e',
     'LBaaSState': '1.0-a0ff7dce2d3f6ce1ffab4ff95a344361',
     'Network': '1.1-27a8a3e236d1d239121668a590130154',
     'Route': '1.0-5ca049cb82c4d4ec5edb1b839c1429c7',
     'RouteList': '1.0-15ecf022a68ddbb8c2a6739cfc9f8f5e',
     'Subnet': '1.0-6a8c192ef7492120d1a5e0fd08e44272',
     'SubnetList': '1.0-15ecf022a68ddbb8c2a6739cfc9f8f5e',
     'VIFBase': '1.0-4a5a8881dc999752cb050dd443458b6a',
     'VIFBridge': '1.0-e78d355f3505361fafbf0797ffad484a',
     'VIFDirect': '1.0-05c939280f4025fd1f7efb921a835c57',
     'VIFGeneric': '1.0-c72e637ed620f0135ea50a9409a3f389',
     'VIFHostDevice': '1.0-bb090f1869c3b4df36efda216ab97a61',
     'VIFMacvlanNested': '1.0-c72e637ed620f0135ea50a9409a3f389',
     'VIFOpenVSwitch': '1.0-e78d355f3505361fafbf0797ffad484a',
     'VIFPortProfile8021Qbg': '1.0-167f305f6e982b9368cc38763815d429',
     'VIFPortProfile8021Qbh': '1.0-4b945f07d2666ab00a48d1dc225669b1',
     'VIFPortProfileBase': '1.0-77509ea1ea0dd750d5864b9bd87d3f9d',
     'VIFPortProfileFPBridge': '1.0-d50872b3cddd245ffebef6053dfbe27a',
     'VIFPortProfileFPOpenVSwitch': '1.1-74e77f46aa5806930df6f37a0b76ff8b',
     'VIFPortProfileFPTap': '1.0-11670d8dbabd772ff0da26961adadc5a',
     'VIFPortProfileOVSRepresentor': '1.1-30e555981003a109b133da5b43ded5df',
     'VIFPortProfileOpenVSwitch': '1.1-70d36e09c8d800345ce71177265212df',
     'VIFVHostUser': '1.1-1f95b43be1f884f090ca1f4d79adfd35',
     'VIFVlanNested': '1.0-7c127b859770cdc04407590c39b59782'}
class TestObjectVersions(test_base.TestCase):
	def test_versions(self):
		checker = fixture.ObjectVersionChecker(
			base.VersionedObjectRegistry.obj_classes())
		expected, actual = checker.test_hashes(object_data)
		self.assertEqual(expected, actual, 
				"Some objects have changed; please make sure the "
				"versions have been bumped and backporting "
				"compatibility code has been added to "
				"obj_make_compatible if necessary, and then update "
				"their hashes in the object_data map in this test "
				"module.  If we don't need to add backporting code "
				"then it means we also don't need the version bump "
				"and we just have to change the hash in this module.")
