from django.db import models

class StudentProfile(models.Model):
    """学生档案（敏感数据：本科院校/专业/成绩排名）"""
    profile_id = models.AutoField(primary_key=True)
    undergraduate_school = models.CharField(max_length=100, verbose_name="本科院校")
    undergraduate_major = models.CharField(max_length=100, verbose_name="本科专业")
    rank_percent = models.CharField(max_length=20, verbose_name="成绩排名")
    target_major = models.CharField(max_length=100, blank=True, verbose_name="目标专业")
    preferred_region = models.CharField(max_length=100, blank=True, verbose_name="意向地域")
    risk_preference = models.CharField(
        max_length=10, choices=[("冲","冲"),("稳","稳"),("保","保")],
        blank=True, verbose_name="风险偏好"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.undergraduate_school}-{self.undergraduate_major}"