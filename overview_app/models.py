from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill


class CmsBenefit(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    basic_img = ProcessedImageField(upload_to='profile-pictures',
                                    processors=[ResizeToFit(1272, 1280)],
                                    format='JPEG',
                                    options={'quality': 100})


class CmsReviews(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    basic_img = ProcessedImageField(upload_to='profile-pictures',
                                    processors=[ResizeToFit(200, 200)],
                                    format='JPEG',
                                    options={'quality': 100})


class CmsFaq(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class SimpleCms(models.Model):
    section_home_1 = models.CharField(max_length=200, default='The Best Aplication For Personal Trainers')
    #next
    section_info_1_title = models.CharField(max_length=200, default='Access on all devices')
    section_info_1_description = models.TextField(default='Fusce lectus neque viverra risus lobortis adipiscing integer pulvinar elementum. Lorem viverra tincidunt tortor pellentesque.')
    section_info_2_title = models.CharField(max_length=200, default='Large online library')
    section_info_2_description = models.TextField(default='Vulputate convallis odio donec massa facilisis sed nibh rhoncus, maecenas. Maecenas morbi est neque pellentesque.')
    section_info_3_title = models.CharField(max_length=200, default='Study convenient')
    section_info_3_description = models.TextField(default='Fermentum convallis mi posuere rutrum turpis duis facilisis integer. Rhoncus in in sit tellus velit quis laoreet morbi orci sed.')
    section_info_4_title = models.CharField(max_length=200, default='Tracking results')
    section_info_4_description = models.TextField(default='Arcu nisl aliquet vel pellentesque. Vitae nibh leo, facilisis laoreet metus, felis. Egestas id enim turpis tellus, nulla adipiscing.')
    #next
    section_counter_1 = models.TextField(default='Improve your skills and gain knowledge in one application. Become the best version of yourself')
    section_counter_1_title = models.CharField(max_length=200, default='1,000+')
    section_counter_1_description = models.TextField(default='Downloads per day')
    section_counter_2_title = models.CharField(max_length=200, default='1 Million')
    section_counter_2_description = models.TextField(default='Users per month')
    section_counter_3_title = models.CharField(max_length=200, default='300+')
    section_counter_3_description = models.TextField(default='Courses')
    section_counter_4_title = models.CharField(max_length=200, default='134')
    section_counter_4_description = models.TextField(default='Countries')
    #next
    section_options_5_many = models.ManyToManyField(CmsBenefit)
    #next
    section_team_6_title = models.CharField(max_length=200, default='Online learning has already been chosen by 5 million people')
    section_team_6_description = models.TextField(default='<li class="mb-2">Amet minim mollit deserunt ullamco</li>\n<li class="mb-2">Velit officia consequat duis enim</li>\n<li>Exercitation veniam minim</li>')
    #next
    section_review_7_title = models.CharField(max_length=200, default='Testimonials from students who recommend Around')
    section_review_7_all = models.ManyToManyField(CmsReviews)
    #next
    section_faq_8_title = models.CharField(max_length=200, default='Any questions? Check out the FAQ')
    section_faq_8_description = models.TextField(default='Et felis vitae ac venenatis lacus cras etiam risus scelerisque auctor adipiscing in a porta')
    section_faq_8_all = models.ManyToManyField(CmsFaq)
    #next
    section_up_footer_9_title = models.TextField(default='Ready to <br class="d-none d-xxl-inline">Get Started?')
