CONTACTS_ID = 'contacts'
TEXT_INTERVIEWS_ID = 'text-interviews'
VIDEO_INTERVIEWS_ID = 'video-interviews'
BIO_ID = 'bio'
PROGRAM_ID = 'program'
SOME_ID = 'some'

CONTACTS_NAME = 'Кантакты'
TEXT_INTERVIEWS_NAME = 'Тэкставыя інтэрв\'ю'
VIDEO_INTERVIEWS_NAME = 'Відэа-інтэрв\'ю'
BIO_NAME = 'Біяграфія'
PROGRAM_NAME = 'Праграма'
SOME_NAME = 'Што-небудзь'

id_name_map = {
    CONTACTS_ID: CONTACTS_NAME,
    TEXT_INTERVIEWS_ID: TEXT_INTERVIEWS_NAME,
    VIDEO_INTERVIEWS_ID: VIDEO_INTERVIEWS_NAME,
    BIO_ID: BIO_NAME,
    PROGRAM_ID: PROGRAM_NAME,
    SOME_ID: SOME_NAME,
}
name_id_map = {
    CONTACTS_NAME: CONTACTS_ID,
    TEXT_INTERVIEWS_NAME: TEXT_INTERVIEWS_ID,
    VIDEO_INTERVIEWS_NAME: VIDEO_INTERVIEWS_ID,
    BIO_NAME: BIO_ID,
    PROGRAM_NAME: PROGRAM_ID,
    SOME_NAME: SOME_ID,
}


def humanize(cat_id):
    try:
        return id_name_map[cat_id]
    except KeyError:
        return cat_id


def dehumanize(cat_name):
    try:
        return name_id_map[cat_name]
    except KeyError:
        return cat_name
