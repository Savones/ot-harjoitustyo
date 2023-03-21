import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_saldo_vähenee_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
    
    def test_saldo_ei_muutu_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahanotto_palauttaa_true_kun_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
    
    def test_rahanotto_palauttaa_false_kun_ei_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)






