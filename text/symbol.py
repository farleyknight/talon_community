from talon.voice import Context, Key

ctx = Context('symbol')

keymap = {
    'randall': Key('esc'),
    '(question [mark] | questo)': '?',
    '(minus | dash)': '-',
    'plus': '+',
    'tilde': '~',
    '(bang | exclamation point | clamor)': '!',
    '(dollar [sign] | dolly)': '$',
    '(downscore | crunder)': '_',
    '(semi | semicolon | sunk)': ';',
    'colon': ':',

    '(square | left square [bracket] | brackorp)': '[',
    '(rsquare | are square | right square [bracket] | brackose)': ']',
    '(paren | left paren | precose)': '(',
    '(rparen | are paren | right paren)': ')',
    '(brace | left brace | kirksorp)': '{',
    '(rbrace | are brace | right brace | kirkos)': '}',
    '(angle | left angle | less than)': '<',
    '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | number sign)': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    '(pipe | spike)': '|',
    '(D pipe)': ' | ',

    '(dubquote | double quote | quatches)': '"',
    '(quote | quatchet)': "'",
    'triple quote': "'''",
    'tick': "`",
    'triple tick': "```",
    '(dot | period)': '.',
    'comma': ',',
    'comshock': [',', Key('enter')],
    'swipe': ', ',
    'coalgap': ': ',
    'skoosh': ' ',
    '[forward] slash': '/',
    '[forward] slasher': '// ',
    '[forward] dubslash': '//',
    'backslash': '\\',
    'coalshock': [':', Key('enter')],
    'coal twice': '::',
    'ellipsis': '...',
    'mintwice': '--',
    'plustwice': '++',

    # equality
    'coleek': ' := ',
    'empty dict': '{}',
    'minquall': '-=',
    'pluqual': '+=',
    'starqual': '*=',
    'lessqual': ' <= ',
    'grayqual': ' >= ',
    'smaqual': '=',
    'equeft': ' = ',
    '([is] equal to | longqual)': ' == ',
    '([is] not equal to | banquall)': ' != ',
    '(trickle | triple equal)': ' === ',
    '(ranqual | nockle)': ' !== ',

    '(arrow | lambo)': ' -> ',
    'shrocket': ' => ',
    'sinker': [Key('cmd-right ;')],

    # surrounders
    '(empty array | brackers)': '[]',
    'brax-block': ['[', Key('enter')],
    'prex-block': ['(', Key('enter')],
    'angler': ['<>', Key('left')],
    'brax': ['[]', Key('left')],
    'coif': ['""', Key('left')],
    'glitch': ['``', Key('left')],
    'kirk': ['{}', Key('left')],
    'precoif': ['("")', Key('left'), Key('left')],
    'prex': ['()', Key('left')],
    'posh': ["''", Key('left')],
    #'padded': (False, surround(" "), 1),

    'and sign': '&',

    '(dot dot | dotdot | doodle)': '..',
    '(enter | shock)': Key('enter'),
    'junk': Key('backspace'),
    'spunk': Key('delete'),
}

ctx.keymap(keymap)