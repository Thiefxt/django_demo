"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-28 03:04
@Filename			: initdata.py
@Description		: 
@Software           : PyCharm
"""
from django.core.management import BaseCommand
from demo.apps.booktest.models import SoOrder


class Command(BaseCommand):
    """自定义脚本"""

    def add_arguments(self, parser):
        parser.add_argument(
            '-order',
            '--name',
            action='store',
            dest='name',
            default='',
            help='order order_sn.',
        )

    def handle(self, *args, **options):
        try:
            if options["name"]:
                print("hello_world %s" % options["name"])
            self.stdout.write(self.style.SUCCESS("命令 %s 执行成功， 参数为%s" % (__file__, options["name"])))
        except Exception as e:
            self.stdout.write(self.style.ERROR('命令执行出错'))

        obj = SoOrder.objects.filter(buyer_id="91").first()
        self.stdout.write(obj.order_sn)
        for i in options:
            self.stdout.write(i)
        # raise CommandError("执行失败")
