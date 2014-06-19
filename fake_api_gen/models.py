from django.db import models

# Create your models here.
class FakeApi(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='snippets', blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    METHOD_CHOICES = (
        ('GET', 'GET'),
        ('HEAD', 'HEAD'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('OPTIONS', 'OPTIONS'),
        ('CONNECT', 'CONNECT'),
        ('PATCH', 'PATCH'),
    )
    request_method = models.CharField(max_length=10,
                                      choices=METHOD_CHOICES,
                                      default='GET')
    RESPONSE_BODY_TYPE_CHOICES = (
        ('JSON', 'JSON'),
        ('HTML', 'HTML'),
    )
    response_body_type = models.CharField(max_length=10,
                                          choices=RESPONSE_BODY_TYPE_CHOICES,
                                          default='JSON')
    RESPONSE_CODE_CHOICES = (
        (100, "1xx Informational"),
        (200, "2xx Success"),
        (200, "3xx Redirection"),
        (200, "4xx Client Error"),
        (200, "5xx Server Error"),
    )
    response_status_code = models.IntegerField(max_length=10,
                                               choices=RESPONSE_CODE_CHOICES,
                                               default=200)
    response_body = models.TextField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name