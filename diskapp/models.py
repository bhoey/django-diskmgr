from django.db import models


class Host(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'hosts'
        ordering = [ 'name', ]


class Disk(models.Model):

    INTERFACES = (
        ('IDE',   'IDE'  ),
        ('eSATA', 'eSATA'),
        ('PCIe',  'PCIe' ),
        ('SATA',  'SATA' ),
        ('SAS',   'SAS'  ),
        ('USB',   'USB'  ),
    )

    id = models.AutoField(primary_key=True)
    serial_no = models.CharField(verbose_name='Serial Number', max_length=128)
    size_gb = models.IntegerField(verbose_name='Size (GB)')
    interface = models.CharField(max_length=100, choices=INTERFACES, blank=True)
    purpose = models.CharField(max_length=100, blank=True)
    host = models.ForeignKey('Host', blank=True, null=True, related_name='host_disks', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.size_gb} GB S/N:{self.serial_no}"

    class Meta:
        db_table = 'disks'
        ordering = [ 'size_gb', 'serial_no', ]
        verbose_name_plural = "Disks"


