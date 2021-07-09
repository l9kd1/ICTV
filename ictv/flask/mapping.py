import ictv

from ictv.pages import users_page, screens_page, screen_renderer, screen_client, screen_subscriptions_page, screen_router
from ictv.pages import buildings_page, channels_page, channel_page, manage_bundle_page, plugins_page, channel_renderer
from ictv.pages import storage_page, logs_page, emails_page
from ictv.storage import cache_page, transcoding_page
from ictv.client.pages import client_pages

def init_flask_url_mapping(app):
    app.add_url_rule('/', view_func=ictv.app.IndexPage.as_view('IndexPage'))
    app.add_url_rule('/users', view_func=ictv.pages.users_page.UsersPage.as_view('UsersPage'))
    app.add_url_rule('/users/<int:id>', view_func=ictv.pages.users_page.UserDetailPage.as_view('UserDetailPage'))
    app.add_url_rule('/screens', view_func=ictv.pages.screens_page.ScreensPage.as_view('ScreensPage'))
    app.add_url_rule('/screens/<int:id>', view_func=ictv.pages.screens_page.DetailPage.as_view('ScreensDetailPage'))
    app.add_url_rule('/screens/<int:id>/config', view_func=ictv.pages.screens_page.ScreenConfigPage.as_view('ScreenConfigPage'))
    app.add_url_rule('/screens/<int:screen_id>/view/<string:secret>', view_func=ictv.pages.screen_renderer.ScreenRenderer.as_view('ScreenRenderer'))
    app.add_url_rule('/screens/<int:screen_id>/client/<string:secret>', view_func=ictv.pages.screen_client.ScreenClient.as_view('ScreenClient'))
    app.add_url_rule('/screens/<int:screen_id>/subscriptions', view_func=ictv.pages.screen_subscriptions_page.ScreenSubscriptionsPage.as_view('ScreenSubscriptionsPage'))
    app.add_url_rule('/screens/redirect/<string:mac>', view_func=ictv.pages.screen_router.ScreenRouter.as_view('ScreenRouter'))
    app.add_url_rule('/buildings', view_func=ictv.pages.buildings_page.BuildingsPage.as_view('BuildingsPage'))
    app.add_url_rule('/channels', view_func=ictv.pages.channels_page.ChannelsPage.as_view('ChannelsPage'))
    app.add_url_rule('/channels/<int:channel_id>', view_func=ictv.pages.channel_page.ChannelPage.as_view('ChannelPage'))
    app.add_url_rule('/channels/<int:id>/request/<int:user_id>', view_func=ictv.pages.channel_page.RequestPage.as_view('RequestPage'))
    app.add_url_rule('/channels/<int:bundle_id>/manage_bundle', view_func=ictv.pages.manage_bundle_page.ManageBundlePage.as_view('ManageBundlePage'))
    app.add_url_rule('/channels/<int:channel_id>/subscriptions', view_func=ictv.pages.channel_page.SubscribeScreensPage.as_view('SubscribeScreensPage'))
    app.add_url_rule('/channel/<int:channel_id>', view_func=ictv.pages.channel_page.DetailPage.as_view('ChannelDetailPage'))
    app.add_url_rule('/channel/<int:channel_id>/force_update', view_func=ictv.pages.channel_page.ForceUpdateChannelPage.as_view('ForceUpdateChannelPage'))
    app.add_url_rule('/plugins', view_func=ictv.pages.plugins_page.PluginsPage.as_view('PluginsPage'))
    app.add_url_rule('/plugins/<int:plugin_id>/config', view_func=ictv.pages.plugins_page.PluginConfigPage.as_view('PluginConfigPage'))
    app.add_url_rule('/preview/channels/<int:channel_id>/<string:secret>', view_func=ictv.pages.channel_renderer.ChannelRenderer.as_view('ChannelRenderer'))
    app.add_url_rule('/renderer/<int:channelid>', view_func=ictv.pages.utils.DummyRenderer.as_view('DummyRenderer'))
    app.add_url_rule('/renderer/<int:channelid>/capsule/<int:capsuleid>', view_func=ictv.pages.utils.DummyCapsuleRenderer.as_view('DummyCapsuleRenderer'))
    app.add_url_rule('/cache/<int:asset_id>', view_func=ictv.storage.cache_page.CachePage.as_view('CachePage'))
    app.add_url_rule('/storage', view_func=ictv.pages.storage_page.StoragePage.as_view('StoragePage'))
    app.add_url_rule('/storage/<int:channel_id>', view_func=ictv.pages.storage_page.StorageChannel.as_view('StorageChannel'))
    app.add_url_rule('/logs', view_func=ictv.pages.logs_page.LogsPage.as_view('LogsPage'))
    app.add_url_rule('/logs/<string:log_name>', view_func=ictv.pages.logs_page.ServeLog.as_view('ServeLog'))
    app.add_url_rule('/logas/<string:target_user>', view_func=ictv.pages.utils.LogAs.as_view('LogAs'))
    app.add_url_rule('/tour/<string:status>', view_func=ictv.pages.utils.TourPage.as_view('TourPage'))
    app.add_url_rule('/client/ks/<path:file>', view_func=ictv.client.pages.client_pages.Kickstart.as_view('Kickstart'))
    app.add_url_rule('/emails', view_func=ictv.pages.emails_page.EmailPage.as_view('EmailPage'))
    app.add_url_rule('/transcoding/<path:b64_path>/progress', view_func=ictv.storage.transcoding_page.ProgressPage.as_view('ProgressPage'))