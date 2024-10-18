# app/models.py

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    skin_care_hair_care = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    teens = models.BooleanField(null=True, blank=True)
    twenties = models.BooleanField(null=True, blank=True)
    thirties = models.BooleanField(null=True, blank=True)
    forties = models.BooleanField(null=True, blank=True)
    fifties = models.BooleanField(null=True, blank=True)
    sixties = models.BooleanField(null=True, blank=True)
    skin_type_normal = models.BooleanField(null=True, blank=True)
    oily = models.BooleanField(null=True, blank=True)
    dry = models.BooleanField(null=True, blank=True)
    sensitive = models.BooleanField(null=True, blank=True)
    combination = models.BooleanField(null=True, blank=True)
    skin_concerns_acne = models.BooleanField(null=True, blank=True)
    aging = models.BooleanField(null=True, blank=True)
    dull_skin = models.BooleanField(null=True, blank=True)
    elasticity = models.BooleanField(null=True, blank=True)
    hydration = models.BooleanField(null=True, blank=True)
    pigmentation = models.BooleanField(null=True, blank=True)
    pores = models.BooleanField(null=True, blank=True)
    redness = models.BooleanField(null=True, blank=True)
    scarring = models.BooleanField(null=True, blank=True)
    sensitive_skin = models.BooleanField(null=True, blank=True)
    sun_protection = models.BooleanField(null=True, blank=True)
    texture = models.BooleanField(null=True, blank=True)
    uneven_skin_tone = models.BooleanField(null=True, blank=True)
    body_care = models.BooleanField(null=True, blank=True)
    eye_cream = models.BooleanField(null=True, blank=True)
    cleanser = models.BooleanField(null=True, blank=True)
    exfoliant = models.BooleanField(null=True, blank=True)
    microneedling = models.BooleanField(null=True, blank=True)
    moisturizer = models.BooleanField(null=True, blank=True)
    peels = models.BooleanField(null=True, blank=True)
    serums = models.BooleanField(null=True, blank=True)
    sun_screen = models.BooleanField(null=True, blank=True)
    spot_treatment = models.BooleanField(null=True, blank=True)
    toner = models.BooleanField(null=True, blank=True)
    use_sunscreen_daily = models.BooleanField(null=True, blank=True)
    react_to_sun_exposure = models.BooleanField(null=True, blank=True)
    hair_loss = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.product_name