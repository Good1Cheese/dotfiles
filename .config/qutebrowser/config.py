import needed

config.load_autoconfig(False)

# Dark mode
config.set("colors.webpage.darkmode.enabled", True)

# config.source('themes/qute-city-lights/city-lights-theme.py')
config.source('themes/onedark/onedark.py')

# dracula.draw.blood(c)

config.bind('pt', 'tab-pin')
config.bind(';w','hint links spawn --detach mpv --force-window yes {hint-url}')
config.bind(';W','spawn --detach mpv --force-window yes {url}')
config.bind(';I','hint images spawn --output-messages wget -P "/home/cheese/Pictures/" {hint-url}')

c.content.autoplay = False
c.keyhint.delay = 0

# c.spellcheck.languages = ["en-US", "de-DE", "ru-RU" ]
c.tabs.title.format_pinned = '{index} {audio}'

c.window.title_format = '{perc}{current_title}{title_sep}nephestate browser'

c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}",
                       "sx": "https://search.realnephestate.xyz/search?q={}",
                       "yt": "https://www.youtube.com/results?search_query={}"}

c.auto_save.session = True

c.editor.command = ['wezterm', '-e', 'nvim', '{file}']#, '-c', 'normal {line}G{column0}l']

# c.new_instance_open_target = 'tab-silent'
# c.new_instance_open_target_window = 'last-focused'
#
# c.window.hide_decoration = False
#
# alacritty_bin = '/home/peter/bin/alacritty'
# c.editor.command = [alacritty_bin, '-e', 'nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
#
# c.fileselect.handler = 'external'
# c.fileselect.single_file.command = [alacritty_bin, '-e', 'ranger', '--choosefile={}']
# c.fileselect.multiple_files.command = [alacritty_bin, '-e', 'ranger', '--choosefiles={}']
# c.fileselect.folder.command = [alacritty_bin, '-e', 'ranger', '--choosedir={}']

c.fileselect.single_file.command = ['wezterm', '-e', 'yazi']#, '--choosefile={}']
c.fileselect.multiple_files.command = ['wezterm', '-e', 'yazi']#, '--choosefiles={}']
c.fileselect.folder.command = ['wezterm', '-e', 'yazi']#, '--choosedir={}']

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# For google login
config.set('content.headers.user_agent',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
           'accounts.google.com')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.local_content_can_access_remote_urls', True, 'file:///home/cheese/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', False, 'file:///home/cheese/.local/share/qutebrowser/userscripts/*')

c.downloads.location.directory = '~/Downloads'

c.tabs.show = 'multiple'

# Setting default page for when opening new tabs or new windows with
# commands like :open -t and :open -w .
# c.url.default_page = 'https://distro.tube/'
# c.url.start_pages = 'https://distro.tube/'

c.fonts.default_family = '"Source Code Pro"'

c.fonts.default_size = '11pt'
c.fonts.completion.entry = '11pt "Source Code Pro"'
c.fonts.debug_console = '11pt "Source Code Pro"'
c.fonts.statusbar = '11pt "Source Code Pro"'

c.fonts.prompts = 'default_size sans-serif'

# Bindings to use dmenu rather than qutebrowser's builtin search.
#config.bind('o', 'spawn --userscript dmenu-open')
#config.bind('O', 'spawn --userscript dmenu-open --tab')

# Bindings for normal mode
config.bind('`', 'bookmark-add')
config.bind('~', 'bookmark-del')

config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')
config.bind('t', 'cmd-set-text -s :open -t')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
