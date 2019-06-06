def default(session):
    hashtags = [
        'coding',
        'programmer'
        'developer',
        'webdeveloper',
        'softwaredeveloper',
        'coding',
        'worldcode',
        'thedevlife',
        'streetstyle',
        'streetwear',
        'lifestyleblog',
        'seattlegram',
    ]

    session.set_do_like(True, percentage=70)
    session.set_user_interact(amount=1, randomize=False, percentage=40, media='Photo')

    session.like_by_tags(hashtags, amount=60, media=None, interact=True)
