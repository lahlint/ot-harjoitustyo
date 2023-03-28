import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_vahenee_oikein_kun_rahat_riittavat(self):
        self.maksukortti.ota_rahaa(250)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_saldo_ei_vahene_kun_rahat_eivat_riita(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_True_kun_rahat_riittavat(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_metodi_palauttaa_False_kun_rahat_eivat_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2000))