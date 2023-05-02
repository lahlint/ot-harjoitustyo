# Tasohyppelypeli

Tässä tasohyppelypelissä perusideana on yrittää päästä mahdollisimman korkealle putoamatta, hyppelemällä tasolta toiselle sekä kerätä kolikoita matkalla.

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuri](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [Changelog](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Ohjelman käynnistäminen ja komennot

Voit ladata viimeisimmän releasen lähdekoodin [täältä](https://github.com/lahlint/ot-harjoitustyo/releases/tag/viikko5) valitsemalla Assets-osion alta Source code.

### Käynnistäminen

1. Asenna riippuvuudet komennolla:

```poetry install```

2. Käynnistä sovellus komennolla:

```poetry run invoke start```

### Testaus

Testien suoritus tapahtuu komennolla:

```poetry run invoke test```

### Testikattavuus

Testikattavuusraportin voi luoda htmlcov-hakemistoon komennolla:

```poetry run invoke coverage-report```

### Pylint

Pylint-tarkistukset voi suorittaa komennolla:

```poetry run invoke lint```
