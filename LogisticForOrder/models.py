from django.db import models
from django.template.defaultfilters import slugify


class CourierAgency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        db_table = "courier_agenecy"

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('courier_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Destination(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        db_table = "destnation"

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('destination_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Rate(models.Model):
    courier = models.ForeignKey(CourierAgency, on_delete=models.CASCADE)
    from = models.ForeignKey(Destination, on_delete=models.CASCADE)
    to = models.ForeignKey(Destination, on_delete=models.CASCADE)
    min_two_kg_rate = models.DecimalField(max_digits=5,
                                          decimal_places=2)
    per_kilo_thereafter = models.DecimalField(max_digits=5,
                                              decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        db_table = "rate_card"

    def save(self, *args, **kwargs):
        self.update_on = slugify(self.title)
        super().save(*args, **kwargs)
