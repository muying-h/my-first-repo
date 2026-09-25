from django.db import models

class University(models.Model):
    university_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="院校名称")
    level = models.CharField(max_length=20, verbose_name="层次")
    region = models.CharField(max_length=50, verbose_name="地域")
    self_line = models.BooleanField(default=False, verbose_name="自主划线")
    website = models.URLField(blank=True, verbose_name="官网链接")

    def __str__(self):
        return self.name

class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='majors')
    name = models.CharField(max_length=100, verbose_name="专业名称")
    degree_type = models.CharField(max_length=20, verbose_name="学位类型")
    exam_subjects = models.CharField(max_length=200, blank=True, verbose_name="考试科目")

    def __str__(self):
        return f"{self.university.name}-{self.name}"

class Admission(models.Model):
    admission_id = models.AutoField(primary_key=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='admissions')
    year = models.IntegerField(verbose_name="年份")
    score_line = models.IntegerField(verbose_name="复试分数线")
    ratio = models.CharField(max_length=20, blank=True, verbose_name="报录比")
    enrollment = models.IntegerField(null=True, blank=True, verbose_name="招生人数")
    pending = models.BooleanField(default=False, verbose_name="待核实")
    source = models.CharField(max_length=200, blank=True, verbose_name="数据来源")

    class Meta:
        unique_together = ("major", "year")

    def __str__(self):
        return f"{self.major}-{self.year}"