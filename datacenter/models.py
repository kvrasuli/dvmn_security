from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if not self.leaved_at:
            duration_seconds = localtime() - self.entered_at
        else:
            duration_seconds = self.leaved_at - self.entered_at
        return duration_seconds.total_seconds()

    @staticmethod
    def format_duration(duration):
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        return f'{int(hours)}h {int(minutes)}m'

    def is_long(self, minutes=60):
        return self.get_duration() > minutes * 60

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
