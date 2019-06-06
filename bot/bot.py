import logging

from instapy import InstaPy
from pythonjsonlogger import jsonlogger

def build(username, password, config):
    # Create a new session with `selenium_local_session` set to `False`, as we
    # do not yet want to create the browser session without applying all of
    # our configurator functions.
    session = InstaPy(
        username=username,
        password=password,
        selenium_local_session=False)

    set_browser(session, config.get('browser'))
    set_headless(session, config.get('headless'))
    set_relationship_bounds(session, config.get('relationship_bounds'))
    #set_logging(session, config)

    return session

def set_browser(session, browser):
    session.use_firefox = browser == 'firefox'

def set_headless(session, use_headless):
    session.headless_browser = use_headless

def set_relationship_bounds(session, bounds):
    session.set_relationship_bounds(enabled=bounds.get('enabled'),
                                    potency_ratio=bounds.get('potency_ratio'),
                                    delimit_by_numbers=bounds.get('delimit_by_numbers'),
                                    max_followers=bounds.get('max_followers'),
                                    max_following=bounds.get('max_following'),
                                    min_followers=bounds.get('min_followers'),
                                    min_following=bounds.get('min_following'))

# TODO(samrap) figure out the type of logging we want.
def set_logging(session, config):
    pass
