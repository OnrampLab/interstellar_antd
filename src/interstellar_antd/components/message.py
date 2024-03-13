from urllib.parse import urlparse

from interstellar.framework import Element


class Message(Element):
    XPATH_CURRENT = '//div[@class="ant-message"]/div/div'

    def get_content(self):
        return self.get_current_dom_element().text
