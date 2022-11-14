import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassassa_oikea_maara_rahaa_alussa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisia_myyty_oikea_maara_alussa(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaita_myyty_oikea_maara_alussa(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_rahan_maara_kasvaa_oikein_edullisessa_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_rahan_maara_kasvaa_oikein_maukkaassa_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_edullinen_palauttaa_oikean_maaran_rahaa(self):
        palautus = self.kassa.syo_edullisesti_kateisella(400)
        self.assertEqual(palautus, 160)

    def test_maukas_palauttaa_oikean_maaran_rahaa(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(palautus, 600)

    def test_edullisten_maara_kasvaa_oikein_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukkaiden_maara_kasvaa_oikein_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassan_rahamaara_ei_muutu_jos_raha_ei_riita_edulliseen_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_jos_raha_ei_riita_maukkaaseen_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassa_palauttaa_kaikki_rahat_jos_raha_ei_riita_edulliseen(self):
        palautus = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(palautus, 100)

    def test_kassa_palauttaa_kaikki_rahat_jos_raha_ei_riita_maukkaaseen(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(palautus, 100)

    def test_edullisten_maara_ei_muutu_jos_raha_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaiden_maara_ei_muutu_jos_raha_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortin_saldo_vahenee_oikein_edullisella(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_kortin_saldo_vahenee_oikein_maukkaalla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_edullinen_palauttaa_true_jos_raha_riittaa_kortilla(self):
        onnistuiko = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(onnistuiko, True)

    def test_maukas_palauttaa_true_jos_raha_riittaa_kortilla(self):
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(onnistuiko, True)

    def test_edullinen_palauttaa_true_jos_raha_ei_riita_kortilla(self):
        kortti = Maksukortti(200)
        onnistuiko = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)

    def test_maukas_palauttaa_true_jos_raha_ei_riita_kortilla(self):
        kortti = Maksukortti(200)
        onnistuiko = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)

    def test_edullisten_maara_kasvaa_oikein_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukkaiden_maara_kasvaa_oikein_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_edullinen_ei_muuta_kortin_saldoa_jos_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_maukas_ei_muuta_kortin_saldoa_jos_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_edullisten_maara_ei_muutu_jos_raha_ei_riita_kortilla(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaiden_maara_ei_muutu_jos_raha_ei_riita_kortilla(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_kortilla_edullisessa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_kortilla_maukkaassa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_kortilla_edullisessa_jos_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_kortilla_maukkaassa_jos_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_saldo_kasvaa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 2000)

    def test_kortille_ladattaessa_kassan_rahamaara_kasvaa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ladattaessa_saldo_ei_muutu_jos_summa_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_kortille_ladattaessa_kassan_rahamaara_ei_muutu_jos_summa_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)