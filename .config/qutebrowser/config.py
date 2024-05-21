import glob
import os.path

c = locals()["c"]
config = locals()["config"]

c.aliases = {
    "q": "quit",
    "w": "session-save",
    "wq": "quit --save",
    "x": "quit --save",
    "h": "help",
}

c.confirm_quit = ["downloads"]

# proxy_current = 'http://DXf2sxr5:2EVysff7@103.163.53.91:64692/'
# c.content.proxy = proxy_current

c.new_instance_open_target = "tab-silent"
c.new_instance_open_target_window = "last-focused"

c.keyhint.delay = 0

# Dark mode
config.set("colors.webpage.darkmode.enabled", True)

c.auto_save.session = True

c.content.javascript.enabled = True
c.content.autoplay = False
c.content.pdfjs = True

# c.spellcheck.languages = ["en-US", "de-DE", "ru-RU" ]

c.tabs.position = "right"
c.tabs.title.format_pinned = "{index} {audio}"
c.tabs.show = "multiple"
c.tabs.width = 250
c.tabs.background = True
c.tabs.favicons.scale = 0.9
c.tabs.last_close = "close"
c.tabs.padding = {"bottom": 4, "left": 10, "right": 3, "top": 4}
c.tabs.mode_on_change = "restore"
c.tabs.indicator.width = 0

c.window.title_format = "{perc}{current_title}{title_sep}nephestate browser"

c.search.incremental = False

c.scrolling.bar = "never"

c.completion.shrink = True
c.completion.scrollbar.width = 0
c.completion.scrollbar.padding = 0
c.completion.open_categories = ["quickmarks", "bookmarks", "history", "filesystem"]

c.hints.auto_follow = "always"
c.hints.mode = "letter"
if c.hints.mode == "number":
    c.hints.auto_follow_timeout = 400

c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "sx": "https://search.realnephestate.xyz/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
}

# Setting default page for when opening new tabs or new windows with
# commands like :open -t and :open -w .
c.url.default_page = "https://distro.tube/"
c.url.start_pages = "https://distro.tube/"

config.load_autoconfig()

for f in glob.glob(str(config.configdir / "conf.d" / "*.py")):
    config.source(str(os.path.relpath(f, start=config.configdir)))
