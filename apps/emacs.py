# TODO:
# tree?

# Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu.

from talon.voice import Context, Key, Str
from ..utils import text, text_to_number

ctx = Context("emacs", bundle="org.gnu.Emacs")

def insert_number(words):
  Str(text_to_number(words))(None)

keymap = {
  "C T R L": "ctrl",
  # nato codes
  "alfa": "a",
  "bravo": "b",
  "charlie": "c",
  "delta": "d",
  "echo": "e",
  "foxtrot": "f",
  "golf": "g",
  "hotel": "h",
  "india": "i",
  "juliet": "j",
  "kilo": "k",
  "lima": "l",
  "mike": "m",
  "november": "n",
  "oscar": "o",
  "papa": "p",
  "quebec": "q",
  "romeo": "r",
  "sierra": "s",
  "tango": "t",
  "uniform": "u",
  "victor": "v",
  "whiskey": "w",
  "x-ray": "x",
  "yankee": "y",
  "zulu": "z",
  # working with files
  "open file": Key("ctrl-x ctrl-f"),
  "open buffer": Key("ctrl-x b"),
  "save buffer": Key("ctrl-x ctrl-s"),
  "search directory": Key("cmd-s g"),
  "search directory phrase <dgndictation> [over]": [Key("cmd-s g"), text],
  "write buffer": Key("ctrl-x ctrl-s"),
  "search buffer": Key("ctrl-s"),
  "search buffer for <dgndictation> [over]": [Key("ctrl-s"), text],
  "previous buffer": [Key("ctrl-x b enter")],
  "window down": [Key("shift-down")],
  "window up": [Key("shift-up")],
  "window right": Key("shift-right"),
  "window left": Key("shift-left"),
  "quit": Key("ctrl-g"),
  "undo": Key("ctrl-x u"),
  "start of buffer": Key("shift-cmd-<"),
  "start of line": Key("ctrl-a"),
  "end of line": Key("ctrl-e"),
  # ""
  "scroll to the bottom": Key("shift-cmd->"),
  "beginning of buffer": Key("shift-cmd-<"),
  "top of buffer": Key("shift-cmd-<"),
  "end of buffer": Key("shift-cmd->"),
  "switch to buffer": Key("ctrl-x b"),
  "switch back": Key("ctrl-x b enter"),
  "close search": Key("q"),
  "mark": Key("ctrl-space"),
  "new line": Key("enter"),
  "newline": Key("enter"),
  "nuline": Key("enter"),
  "new line below": Key("ctrl-e enter"),
  "chunk left": Key("cmd-left"),
  "show lines": [Key("cmd-x"), "linum-mode", Key("enter")],
  "start string": Key('" " left'),
  "new string": Key('" " left'),
  "go to line": Key("cmd-g g"),
  "left word": Key("cmd-left"),
  "auto complete": Key("cmd-/"),
  "comment region": Key("cmd-;"),
  "close buffer": Key("ctrl-x k enter"),
  "copy line": Key("ctrl-a ctrl-space ctrl-e cmd-w"),
  "comment line": Key("ctrl-a ctrl-space ctrl-e cmd-;"),
  "copy": Key("cmd-w"),
  "paste": Key("ctrl-y"),
  "delete line": Key("ctrl-a ctrl-k"),
  "parentheses": Key("( ) left"),
  # "": Key()
}

ctx.keymap(keymap)
