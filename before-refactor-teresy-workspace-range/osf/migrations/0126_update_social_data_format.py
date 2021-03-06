# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-25 20:39
from __future__ import unicode_literals

import logging
import progressbar

from django.db import migrations, connection


logger = logging.getLogger(__name__)


FIELDS_TO_MIGRATE = [
    'github',
    'linkedIn',
    'twitter'
]


class Migration(migrations.Migration):

    def update_social_fields(state, schema):
        for field in FIELDS_TO_MIGRATE:
            sql = """
                UPDATE osf_osfuser
                    SET social = social || json_build_object(
                        '{0}', CASE WHEN (osf_osfuser.social ->> '{0}') = '' THEN '[]'
                                    WHEN (osf_osfuser.social ->> '{0}') IS NOT NULL
                                        AND json_typeof(osf_osfuser.social::json -> '{0}') != 'array'
                                        THEN json_build_array(osf_osfuser.social ->> '{0}')
                                    ELSE (osf_osfuser.social -> '{0}')::json
                                END
                    )::jsonb
                WHERE osf_osfuser.social ? '{0}';
            """.format(field)
            with connection.cursor() as cursor:
                logger.info('Setting social fields for {}...'.format(field))
                cursor.execute(sql)

    def reset_social_fields(state, schema):
        OSFUser = state.get_model('osf', 'osfuser')
        users_with_social = OSFUser.objects.filter(social__has_any_keys=FIELDS_TO_MIGRATE)
        users_to_update = users_with_social.count()
        logger.info('Updating social fields for {} users'.format(users_to_update))
        progress_bar = progressbar.ProgressBar(maxval=users_to_update or 100).start()

        users_updated = 0
        for user in users_with_social:
            old_social = {}
            for key, value in user.social.iteritems():
                if key in FIELDS_TO_MIGRATE:
                    if len(value) > 1:
                        raise ValueError('Current social list field has more than one value, cannot reset to just one value.')
                    old_social[key] = value[0]
                else:
                    old_social[key] = value
            user.social = old_social
            user.save()
            users_updated += 1
            progress_bar.update(users_updated)

        progress_bar.finish()
        logger.info('Updated social field for {} users'.format(users_updated))

    dependencies = [
        ('osf', '0125_merge_20180824_1856'),
    ]

    operations = [
        migrations.RunPython(update_social_fields, reset_social_fields)
    ]
