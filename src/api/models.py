from django.db import models


class Record(models.Model):
    class Meta:
        db_table = 'records'

    dbn = models.CharField(blank=True, null=True, max_length=20)
    school_name = models.CharField(blank=True, null=True, max_length=100)
    category = models.CharField(blank=True, null=True, max_length=100)
    total_enrolments = models.IntegerField(blank=True, null=True)
    grade_k = models.IntegerField(blank=True, null=True)
    grade_1 = models.IntegerField(blank=True, null=True)
    grade_2 = models.IntegerField(blank=True, null=True)
    grade_3 = models.IntegerField(blank=True, null=True)
    grade_4 = models.IntegerField(blank=True, null=True)
    grade_5 = models.IntegerField(blank=True, null=True)
    grade_6 = models.IntegerField(blank=True, null=True)
    grade_7 = models.IntegerField(blank=True, null=True)
    grade_8 = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    asian = models.IntegerField(blank=True, null=True)
    black = models.IntegerField(blank=True, null=True)
    hispanic = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
    ell_spanish = models.IntegerField(blank=True, null=True)
    ell_chinese = models.IntegerField(blank=True, null=True)
    ell_bengali = models.IntegerField(blank=True, null=True)
    ell_arabic = models.IntegerField(blank=True, null=True)
    ell_haitian_creole = models.IntegerField(blank=True, null=True)
    ell_french = models.IntegerField(blank=True, null=True)
    ell_russian = models.IntegerField(blank=True, null=True)
    ell_korean = models.IntegerField(blank=True, null=True)
    ell_urdu = models.IntegerField(blank=True, null=True)
    ell_other = models.IntegerField(blank=True, null=True)
    ela_takers = models.IntegerField(blank=True, null=True)
    ela_level_1 = models.IntegerField(blank=True, null=True)
    ela_level_2 = models.IntegerField(blank=True, null=True)
    ela_level_3 = models.IntegerField(blank=True, null=True)
    ela_level_4 = models.IntegerField(blank=True, null=True)
    math_takers = models.IntegerField(blank=True, null=True)
    math_level_1 = models.IntegerField(blank=True, null=True)
    math_level_2 = models.IntegerField(blank=True, null=True)
    math_level_3 = models.IntegerField(blank=True, null=True)
    math_level_4 = models.IntegerField(blank=True, null=True)

    def get_percentage(self, total_field: str, value_field) -> float:
        total = self.__getattribute__(total_field)
        value = self.__getattribute__(value_field)

        return float(value/total)
