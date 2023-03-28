import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        pass

    def test_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_oikea(self):
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.edulliset, 0)
        self.assertEqual(kassapaate.maukkaat, 0)

    def test_edullisesti_kateisella_kassan_rahat_ja_vaihtorahat_oikein_kun_rahat_riittavat(self):
        kassapaate = Kassapaate()
        maksu = kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(maksu, 1000-240)

    def test_maukkaasti_kateisella_kassan_rahat_ja_vaihtorahat_oikein_kun_rahat_riittavat(self):
        kassapaate = Kassapaate()
        maksu = kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000+400)
        self.assertEqual(maksu, 1000-400) 

    def test_kateisosto_kasvattaa_lounaiden_maaraa_kun_rahat_riittavat(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(1000)
        kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(kassapaate.edulliset, 1)
        self.assertEqual(kassapaate.maukkaat, 1)

    def test_kateisostossa_kassan_rahat_vaihtorahat_ja_lounaiden_maarat_oikein_kun_rahat_eivat_riita(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(kassapaate.maukkaat, 0)
        self.assertEqual(kassapaate.edulliset, 0)

    def test_korttiostossa_veloitetaan_summa_kortilta_ja_palautetaan_True_kun_rahat_riittavat(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(1000)
        palautusarvo = kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(palautusarvo, True)
        self.assertEqual(kortti.saldo, 1000-240)
        kortti = Maksukortti(1000)
        palautusarvo = kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(palautusarvo, True)
        self.assertEqual(kortti.saldo, 1000-400)

    def test_korttiostoissa_myytyjen_lounaiden_maara_kasvaa_kun_rahat_riittavat(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(1000)
        kassapaate.syo_edullisesti_kortilla(kortti)
        kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.edulliset, 1)
        self.assertEqual(kassapaate.maukkaat, 1)

    def test_korttiostoissa_kortin_saldo_ja_lounaiden_maara_ei_muutu_ja_palautetaan_False_kun_rahat_eivat_riita(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(200)
        palautusarvo = kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(palautusarvo, False)
        palautusarvo = kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(palautusarvo, False)
        self.assertEqual(kassapaate.edulliset, 0)
        self.assertEqual(kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_korttiostoissa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(1000)
        kassapaate.syo_edullisesti_kortilla(kortti)
        kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasvaa_ladattavalla_summalla(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(0)
        kassapaate.lataa_rahaa_kortille(kortti,1000)
        kassapaate.lataa_rahaa_kortille(kortti, 0)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000+1000)
        self.assertEqual(kortti.saldo, 1000)

    def test_kortin_saldo_ja_kassan_rahamaara_eivat_muutu_kun_yritetaan_ladata_negatiivinen_summa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(0)
        kassapaate.lataa_rahaa_kortille(kortti, -1000)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 0)