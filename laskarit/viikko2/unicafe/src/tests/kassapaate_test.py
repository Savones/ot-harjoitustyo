import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # oikea set up

    def test_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_edullisten_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyjen_maukkaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # käteinosto toimii edullisilla lounailla

    def test_edullinen_kateismaksu_riittaa_kassan_rahanousu_oikea(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_kateismaksu_riittaa_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_edullinen_kateismaksu_riittaa_myytyjen_lounaiden_maara_oikea(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateismaksu_ei_riita_kassan_rahamaara_muuttumaton(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kateismaksu_ei_riita_vaihtoraha_koko_summa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_edullinen_kateismaksu_ei_riita_lounaiden_maara_muuttumaton(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    # käteisnosto toimii maukkailla lounailla

    def test_maukas_kateismaksu_riittaa_kassan_rahanousu_oikea(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_kateismaksu_riittaa_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukas_kateismaksu_riittaa_myytyjen_lounaiden_maara_oikea(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateismaksu_ei_riita_kassan_rahamaara_muuttumaton(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateismaksu_ei_riita_vaihtoraha_koko_summa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_maukas_kateismaksu_ei_riita_lounaiden_maara_muuttumaton(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # korttiosto toimii edullisella lounaalla

    def test_edullinen_korttiosto_riittaa_summa_veloitetaan_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000 - 240)

    def test_edullinen_korttiosto_riittaa_palautetaan_True(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullinen_korttiosto_riittaa_myytyjen_maara_oikea(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_korttiosto_ei_riita_summaa_ei_veloiteta(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_edullinen_korttiosto_ei_riita_palautetaan_False(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_edullinen_korttiosto_ei_riita_myytyjen_maara_muuttumaton(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # korttiosto toimii maukkailla lounailla

    def test_maukas_korttiosto_riittaa_summa_veloitetaan_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000 - 400)

    def test_maukas_korttiosto_riittaa_palautetaan_True(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukas_korttiosto_riittaa_myytyjen_maara_oikea(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_korttiosto_ei_riita_summaa_ei_veloiteta(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_maukas_korttiosto_ei_riita_palautetaan_False(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_maukas_korttiosto_ei_riita_myytyjen_maara_muuttumaton(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # rahan lataus toimii

    def test_rahan_lataus_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)

    def test_rahan_lataus_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_rahan_negatiivinen_lataus_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_negatiivinen_lataus_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)