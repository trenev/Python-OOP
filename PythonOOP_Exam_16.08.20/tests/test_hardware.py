from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("SSD", "Power", 500, 200)

    def test_is_instance_set(self):
        self.assertEqual("SSD", self.hardware.name)
        self.assertEqual("Power", self.hardware.type)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install_when_not_success_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hardware.install(Software("Linux", "Express", 400, 300))
        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual([], self.hardware.software_components)

    def test_install_when_success(self):
        software = Software("Linux", "Express", 400, 100)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)

    def test_uninstall_when_not_success(self):
        software = Software("Linux", "Express", 400, 100)
        other_soft = Software("Windows", "Express", 400, 100)
        self.hardware.install(software)
        self.hardware.uninstall(other_soft)
        self.assertIn(software, self.hardware.software_components)

    def test_uninstall_when_success(self):
        software = Software("Linux", "Express", 400, 100)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertNotIn(software, self.hardware.software_components)


if __name__ == "__main__":
    main()
