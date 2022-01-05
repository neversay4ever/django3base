from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class Data(models.Model):
    gene_id = models.CharField(_("基因编码"), max_length=50)
    gene_length = models.PositiveSmallIntegerField(_("基因长度"))
    gene_seq = models.TextField(_("基因序列"))
