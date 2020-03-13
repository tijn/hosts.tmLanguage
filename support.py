import sublime
import sublime_plugin


class HostsFileViewListener(sublime_plugin.ViewEventListener):

    SYNTAX = 'hosts.sublime-syntax'

    @classmethod
    def is_applicable(cls, settings):
        try:
            return (settings and
                    settings.get('syntax', '').lower().endswith(cls.SYNTAX))
        except Exception as e:
            return False

    def on_hover(self, point, hover_zone):
        if ((hover_zone != sublime.HOVER_TEXT or not
             self.view.match_selector(point, 'meta.hostname meta.punycode'))):
            return

        expression_region = next(
            r for r in self.view.find_by_selector('meta.hostname')
            if r.contains(point))

        hostname = self.view.substr(expression_region)

        try:
            hover_text = str.encode(hostname).decode('idna')
        except Exception as e:
            hover_text = 'Could not parse Punycode expression'

        html = '''
            <body id="render-punycode">
                <div>{}</div>
            </body>
        '''.format(hover_text)

        self.view.show_popup(html, sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                             location=point, max_width=512, max_height=60)
