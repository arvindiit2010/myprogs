# Create your models here.
from django.db import models


class User(models.Model):

    name = models.CharField(null=False, max_length=255)
    city = models.CharField(null=False, max_length=255)

    # def __unicode__(self):
    #     return '%s' % self.name

    class Meta:
        verbose_name = 'user registration table'
        db_table = 'user'
    app_label = 'cube'


class Cube(models.Model):

    user_id = models.ForeignKey(User, db_column='user_id', related_name='cube')
    name = models.CharField(null=False, max_length=255)

    #
    # def __unicode__(self):
    #     return '%s: %s ' % (self.name, self.user_id)

    class Meta:
        verbose_name = 'Cube details'
        db_table = 'cube'
    app_label = 'cube'


class Content(models.Model):

    user_id = models.ForeignKey(User, db_column='user_id', related_name='content')
    link = models.CharField(null=False, max_length=255)

    # def __unicode__(self):
    #     return '%s: %s' % (self.link, self.user_id)

    class Meta:
        verbose_name = 'content details'
        db_table = 'content'
    app_label = 'cube'


class CubeUser(models.Model):

    user_id = models.ForeignKey(User, db_column='user_id', related_name='cube_user')
    cube_id = models.ForeignKey(Cube, db_column='cube_id', related_name='cube_user')

    # def __unicode__(self):
    #     return '%s: %s' % (self.link, self.user_id)
    def __repr__(self):
        return '%s: %s' % (self.user_id, self.cube_id)
    class Meta:
        verbose_name = 'share cube with user'
        db_table = 'cube_user'
    app_label = 'cube'


class ContentUser(models.Model):

    user_id = models.ForeignKey(User, db_column='user_id', related_name='content_user')
    content_id = models.ForeignKey(Content, db_column='content_id', related_name='content_user')

    # def __unicode__(self):
    #     return '%s: %s' % (self.link, self.user_id)

    class Meta:
        verbose_name = 'share content with user'
        db_table = 'content_user'
    app_label = 'cube'


class ContentCube(models.Model):
    user_id = models.ForeignKey(User, db_column='user_id', related_name='content_cube')
    cube_id = models.ForeignKey(Cube, db_column='cube_id', related_name='content_cube')
    content_id = models.ForeignKey(Content, db_column='content_id', related_name='content_cube')

    def __repr__(self):
        return '%s: %s' % (self.user_id, self.cube_id)

    class Meta:
        verbose_name = 'add content with cube'
        db_table = 'content_cube'
    app_label = 'cube'