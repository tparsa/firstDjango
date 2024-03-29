import django.db
from django.db.models.functions import Length
from myapp.models import MyModel


invalid_ages = (MyModel.objects.filter(age__gt=99) | MyModel.objects.filter(age__lt=18)).distinct()
invalid_experience = (MyModel.objects.filter(experience__gt=24) |MyModel.objects.filter(experience__lt=0)).distinct()
invalid_first_name_len = (MyModel.objects.annotate(first_name_length=Length('first_name')).filter(first_name_length__lt=2) | MyModel.objects.annotate(first_name_length=Length('first_name')).filter(first_name_length__gt=32)).distinct()
invalid_last_name_len = (MyModel.objects.annotate(last_name_length=Length('last_name')).filter(last_name_length__lt=4) | MyModel.objects.annotate(last_name_length=Length('last_name')).filter(last_name_length__gt=64)).distinct()
invalid_data = (invalid_ages | invalid_experience | invalid_first_name_len | invalid_last_name_len).distinct()


valid_data = MyModel.objects.annotate(len_fname=Length('first_name'), len_lname=Length('last_name')).filter(age__gte=18,
                                                                                                            age__lte=99,
                                                                                                            experience__gte=0,
                                                                                                            experience__lte=240,
                                                                                                            len_fname__gte=2,
                                                                                                            len_fname__lte=32,
                                                                                                            len_lname__gte=4,
                                                                                                            len_lname__lte=64)

mahdi_21 = (valid_data.filter(first_name="mahdi") | valid_data.filter(age__lte=21)).distinct()
ali_31_24 = valid_data.filter(first_name__contains="ali", age__lt=30, experience__gt=24)
only_ali = valid_data.filter(first_name="ali").order_by('last_name')
eleven = valid_data.filter(age__lt=25) | valid_data.filter(last_name__contains="hassan").order_by('experience')
