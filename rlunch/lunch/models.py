from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
from vocabs.models import SkosConcept


class Talk(models.Model):
    title = models.CharField(blank=True, max_length=250)
    speaker = models.CharField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    how_was_it = models.ForeignKey(SkosConcept, blank=True, null=True)

    def __str__(self):
        return "'{}', by {}".format(self.title, self.speaker)

    def get_absolute_url(self):
        return reverse('lunch:talk_detail', kwargs={'pk': self.id})
