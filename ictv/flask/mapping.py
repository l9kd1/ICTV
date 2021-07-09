from ictv.pages import users_page, screens_page, screen_renderer, screen_client, screen_subscriptions_page, screen_router
from ictv.pages import buildings_page, channels_page, channel_page, manage_bundle_page, plugins_page, channel_renderer
from ictv.pages import storage_page, logs_page, emails_page

import ictv
# from ictv.pages import buildings_page
# from ictv.pages import users_page


# from ictv.pages.users_page import UsersPage


def init_flask_url_mapping(app):
    app.add_url_rule('/', view_func=ictv.app.IndexPage.as_view('IndexPage'))
    app.add_url_rule('/channels', view_func=ictv.pages.channels_page.ChannelsPage.as_view('ChannelsPage'))

    app.add_url_rule('/users', view_func=users_page.UsersPage.as_view('UsersPage'))
    app.add_url_rule('/logs', view_func=logs_page.LogsPage.as_view('LogsPage'))

    app.add_url_rule('/buildings', view_func=buildings_page.BuildingsPage.as_view('BuildingsPage'))

    app.add_url_rule('/tour/(started|ended)', view_func=ictv.pages.utils.TourPage.as_view('TourPage'))