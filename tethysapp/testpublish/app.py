from tethys_sdk.base import TethysAppBase, url_map_maker


class Testpublish(TethysAppBase):
    """
    Tethys app class for asdfadsf.
    """

    name = 'asdfadsf'
    index = 'testpublish:home'
    icon = 'testpublish/images/icon.gif'
    package = 'testpublish'
    root_url = 'testpublish'
    color = '#2c3e50'
    description = 'asdfas ads fasfasdf asdfc asdf asdf '
    tags = 'asdf,asdf,sadf'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='testpublish',
                controller='testpublish.controllers.home'
            ),
        )

        return url_maps