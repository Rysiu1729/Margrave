from django.db import models


class Chapter(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class Section(models.Model):
    title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Page(models.Model):
    text = models.TextField(max_length=40000)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:100]+"..."



class Effect(models.Model):
    next_page = models.ForeignKey(Page,on_delete=models.CASCADE)
    action = models.CharField(max_length=1000)

    def __str__(self):
        return self.action



class Option(models.Model):
    text = models.CharField(max_length=10000)
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    effect = models.ForeignKey(Effect,on_delete=models.CASCADE)

    def __str__(self):
        return self.text



class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    relations = models.IntegerField(default=0)
    position = models.CharField(max_length=200)
    story = models.CharField(max_length=40000)

    def __str__(self):
        return self.name
