# Tasohyppelypeli

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuri](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [Changelog](https://github.com/lahlint/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Ohjelman käynnistäminen ja komennot

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
