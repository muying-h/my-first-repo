from django.core.management.base import BaseCommand
from universities.models import University, Major, Admission

class Command(BaseCommand):
    help = '导入样例院校数据'

    def handle(self, *args, **kwargs):
        z, _ = University.objects.get_or_create(
            name="Z大学",
            defaults={"level": "985", "region": "江苏", "self_line": True, "website": "https://www.z.edu.cn"}
        )
        y, _ = University.objects.get_or_create(
            name="Y大学",
            defaults={"level": "211", "region": "湖北", "self_line": False, "website": "https://www.y.edu.cn"}
        )
        w, _ = University.objects.get_or_create(
            name="W大学",
            defaults={"level": "双非", "region": "浙江", "self_line": False, "website": "https://www.w.edu.cn"}
        )

        m1, _ = Major.objects.get_or_create(
            university=z, name="计算机科学与技术",
            defaults={"degree_type": "学硕", "exam_subjects": "政治/英语/数一/408"}
        )
        m2, _ = Major.objects.get_or_create(
            university=y, name="软件工程",
            defaults={"degree_type": "学硕", "exam_subjects": "政治/英语/数一/408"}
        )
        m3, _ = Major.objects.get_or_create(
            university=w, name="计算机技术",
            defaults={"degree_type": "专硕", "exam_subjects": "政治/英语/数二/自命题"}
        )

        Admission.objects.get_or_create(
            major=m1, year=2025,
            defaults={"score_line": 345, "ratio": "12.5:1", "enrollment": 50, "pending": False, "source": "研招网"}
        )
        Admission.objects.get_or_create(
            major=m2, year=2025,
            defaults={"score_line": 320, "ratio": "", "enrollment": 40, "pending": True, "source": "待核实"}
        )
        Admission.objects.get_or_create(
            major=m3, year=2025,
            defaults={"score_line": 308, "ratio": "6.2:1", "enrollment": 60, "pending": False, "source": "研招网"}
        )

        self.stdout.write(self.style.SUCCESS("样例数据导入成功"))