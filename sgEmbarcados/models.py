from django.db import models

# Create your models here.

MODE_CHOICE = (
        ('MASTER', 'MASTER'),
        ('SLAVE', 'SLAVE')
)


class Embedded(models.Model):

    hardware = models.CharField(max_length=200)
    firmware = models.FileField(upload_to='uploads/',max_length=100,blank=True)
    location = models.CharField(max_length=100)
    state = models.BooleanField()
    mode = models.CharField(max_length=6, choices=MODE_CHOICE, blank=True)
    essid = models.CharField(max_length=20,blank=True)
    ip = models.GenericIPAddressField(protocol='both')
    mac = models.GenericIPAddressField(protocol='both')
    mask = models.GenericIPAddressField(protocol='both')
    gateway = models.GenericIPAddressField(protocol='both')

    def __str__(self):

        return "%s %s %s %s %s %s %s %s %s" % (self.id, self.hardware, self.location, self.state, self.mode, self.ip, self.mac, self.essid, self.gateway)

    class Meta:
        verbose_name_plural = 'Embeddeds'


class Sensor(models.Model):

    description = models.CharField(max_length=50)
    rate = models.IntegerField()
    data = models.FloatField()

    fkEmbedded = models.ForeignKey(Embedded, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s %s" % (self.id, self.description, self.description, self.rate, self.data)

    class Meta:
        verbose_name_plural = 'Sensors'


class Actuator(models.Model):

    description = models.CharField(max_length=50)
    command = models.IntegerField()

    fkEmbedded = models.ForeignKey(Embedded, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s %s" % (self.id, self.description, self.description, self.command)

    class Meta:
        verbose_name_plural = 'Actuators'

