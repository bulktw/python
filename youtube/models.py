from django.db import models

class Allowlist(models.Model):
    employeeid = models.CharField(max_length=10)
    employeedept = models.CharField(max_length=10)
    employeename = models.TextField()
    purpose = models.TextField()
    created_at = models.DateTimeField('data created')

    def __unicode__(self):
    	return (self.employeeid,self.employeename,self.employeedept,self.purpose,self.created_at)

    def __str__(self):
    	return self.employeeid

