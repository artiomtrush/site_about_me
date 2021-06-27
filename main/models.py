from django.db import models


class Skills_description(models.Model):
    title = models.CharField("Название", max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Summary_description(models.Model):
    title = models.CharField("Название", max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Summary"
        verbose_name_plural = "Summary"


class Language_description(models.Model):
    title = models.CharField("Language", max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


class Work_experience_description(models.Model):
    time = models.CharField("time_work", max_length=50)
    title = models.CharField("Works_experience", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Work_experience"
        verbose_name_plural = "Works_experience"

class Education_description(models.Model):
    time = models.CharField("time_work", max_length=50)
    location = models.CharField("Works_experience", max_length=100)
    title = models.CharField("Works_experience", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
