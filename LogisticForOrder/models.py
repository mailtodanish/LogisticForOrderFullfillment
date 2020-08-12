from django.db import models
from django.template.defaultfilters import slugify


class CourierAgency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']
        db_table = "courier_agenecy"
        verbose_name_plural = "courier Agenecies"

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('courier_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Destination(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']
        db_table = "destnation"

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('destination_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Rate(models.Model):
    courier = models.ForeignKey(CourierAgency, on_delete=models.CASCADE)
    from_destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="From")
    to = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="To")
    min_two_kg_rate = models.DecimalField(max_digits=5,
                                          decimal_places=2)
    per_kilo_thereafter = models.DecimalField(max_digits=5,
                                              decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.courier},{self.from_destination},{self.to}"

    class Meta:
        ordering = ['created_on']
        db_table = "rate_card"
