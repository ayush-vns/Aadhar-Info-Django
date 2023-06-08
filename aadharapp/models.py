from django.db import models

# Create your models here.
class aadharModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    adhaarno = models.IntegerField()
    address = models.IntegerField()

    def __str__(self):
        return"firstname={0},lastname={1},dateofbirth={2},adhaarno={3},address={4}".fromate(self.firstname,self.lastname,self.dateofbirth,self.adhaarno,self.address)

    # class Meta:
        # db_table = "aadharModel"