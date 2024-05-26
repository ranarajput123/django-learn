from django.db import models
from ..user.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ForgotPasswordToken(models.Model):
    token = models.CharField('Forgot Password Token')
    user = models.ForeignKey(User, verbose_name='User whom the token belongs to', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("ForgotPasswordToken")
        verbose_name_plural = _("ForgotPasswordTokens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ForgotPasswordToken_detail", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'forgot-password-token'