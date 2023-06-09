from django.db import models
from django.conf import settings
# Create your models here.

class Element(models.Model):
    symbol = models.CharField(max_length=100)
    elementId = models.IntegerField()
    name = models.CharField(max_length=100)
    atomic_number = models.IntegerField()
    mass = models.CharField(max_length=100)
    period = models.IntegerField()
    row = models.IntegerField()
    column = models.IntegerField()
    _group = models.CharField(max_length=100)
    protons = models.IntegerField()
    neutrons = models.IntegerField()
    electrons = models.IntegerField()
    _1s = models.IntegerField()
    _2s = models.IntegerField()
    _2p = models.IntegerField()
    _3s = models.IntegerField()
    _3p = models.IntegerField()
    _4s = models.IntegerField()
    _3d = models.IntegerField()
    _4p = models.IntegerField()
    _4d = models.IntegerField()
    _5s = models.IntegerField()
    _5p = models.IntegerField()
    _6s = models.IntegerField()
    _5d = models.IntegerField()
    _6p = models.IntegerField()
    _7s = models.IntegerField()
    affinity = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    electronegativity = models.CharField(max_length=100)
    melt = models.CharField(max_length=100)
    boil = models.CharField(max_length=100)
    e_fusion = models.CharField(max_length=100)
    e_vapor = models.CharField(max_length=100)
    t_crit = models.CharField(max_length=100)
    p_crit = models.CharField(max_length=100)
    valence = models.CharField(max_length=100)
    a_radius = models.CharField(max_length=100)
    actiivity = models.IntegerField()

    def __str__(self):
        return self.name


class Compound(models.Model):
    compoundId = models.IntegerField()
    formula = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    alpha = models.CharField(max_length=100)
    mol_mass = models.FloatField()
    bond = models.CharField(max_length=100)
    acid_base = models.CharField(max_length=100)
    electronegativity = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    boiling = models.FloatField()
    melting = models.CharField(max_length=100)
    Vanderwaals_radius = models.CharField(max_length=100)
    Ionic_radius = models.CharField(max_length=100)
    Isotopes = models.CharField(max_length=100)
    electronic_shell = models.CharField(max_length=100)
    Energy_of_first_ionization = models.CharField(max_length=100)
    energy_of_second_ionization = models.CharField(max_length=100)
    standard_potential = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    uses = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ion(models.Model):
    ionId = models.IntegerField()
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    alpha = models.CharField(max_length=100)
    mass = models.FloatField()
    charge = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Substance(models.Model):
    substanceId = models.IntegerField()
    formula = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    alpha = models.CharField(max_length=100)
    mass = models.FloatField()
    units = models.CharField(max_length=100)
    moles = models.FloatField()
    mole_units = models.CharField(max_length=100)
    mol_mol_qty = models.FloatField()
    mol_mol_units = models.CharField(max_length=100)
    A_Z_qty = models.FloatField()
    A_Z__units = models.CharField(max_length=100)
    temp_qty = models.FloatField()
    temp__units = models.CharField(max_length=100)
    press_qty = models.FloatField()
    press__units = models.CharField(max_length=100)
    heat_qty = models.FloatField()
    heat__units = models.CharField(max_length=100)
    reserved_qty = models.FloatField()
    reserved__units = models.CharField(max_length=100)
    bond = models.CharField(max_length=100)
    acid_base = models.CharField(max_length=100)
    electronegativity = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    boiling = models.FloatField()
    melting = models.CharField(max_length=100)
    Vanderwaals_radius = models.CharField(max_length=100)
    Ionic_radius = models.CharField(max_length=100)
    Isotopes = models.CharField(max_length=100)
    electronic_shell = models.CharField(max_length=100)
    Energy_of_first_ionization = models.CharField(max_length=100)
    energy_of_second_ionization = models.CharField(max_length=100)
    standard_potential = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    uses = models.CharField(max_length=100)

    def __str__(self):
        return self.name
