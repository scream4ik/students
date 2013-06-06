from django.core.management.base import BaseCommand, CommandError
from students.models import Group


class Command(BaseCommand):
	
	def handle(self, *args, **options):
		
		for group in Group.objects.all():
			print group.name
			
			for student in group.get_students():
				print '    ' + student.fio