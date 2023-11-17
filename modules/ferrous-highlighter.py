# @author Alexander Hinze
# @since 17/11/2023

from pygments.token import *
from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, this, combined, default, words
from sphinx.highlighting import lexers

LANG_NAME = 'Ferrous'

def setup(app):
    lexers[LANG_NAME] = FerrousLexer()
    return

class FerrousLexer(RegexLexer):
    name = LANG_NAME
    url = 'https://ferrouslang.org'
    aliases = ['ferrous']
    filenames = ['*.ferrous', '*.fe']
    mimetypes = ['text/x-ferrous']
    tokens = {
        'root': [
            (r'(//.*?)(\n)', bygroups(
                Comment.Single, 
                Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline),
            include('attrib_usage'),
            include('function'),
            include('callconv_mod'),
            include('type'),
            include('keyword'),
            include('ident'),
            (r'[^\S\n]+', Whitespace)
        ],
        'type': [
            include('ref_type'),
            include('ptr_type'),
            include('primitive_keyword'),
            include('ident')
        ],
        'ptr_type': [
            (r'(\*)([^\s]+)', bygroups(
                Punctuation, 
                using(this)))
        ],
        'ref_type': [
            (r'(&)([^\s]+)', bygroups(
                Punctuation, 
                using(this)))
        ],
        'function': [
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))(\s*)(:)(\s*)([^\s]+)(\s*)({)([^}]+)(})', bygroups(
                Keyword,
                Whitespace,
                using(this),
                Punctuation,
                using(this),
                Punctuation,
                Whitespace,
                Punctuation,
                Whitespace,
                using(this),
                Whitespace,
                Punctuation,
                using(this),
                Punctuation)),
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))(\s*)(:)(\s*)([^\s]+)', bygroups(
                Keyword,
                Whitespace,
                using(this),
                Punctuation,
                using(this),
                Punctuation,
                Whitespace,
                Punctuation,
                Whitespace,
                using(this))),
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))', bygroups(
                Keyword,
                Whitespace,
                using(this),
                Punctuation,
                using(this),
                Punctuation))
        ],
        'param_list': [

        ],
        'attrib_usage': [
            (r'@\s*\b[a-zA-Z_]+[a-zA-Z_0-9]*\b', Name.Decorator)
        ],
        'callconv_mod': [
            (r'(\bcallconv\b)\s*(\()([^\)]+)(\))', bygroups(
                Keyword, 
                Punctuation, 
                Name, 
                Punctuation))
        ],
        'keyword': [
            include('misc_keyword'),
            include('primitive_keyword'),
            include('literal_keyword')
        ],
        'misc_keyword': [
            (r'\b(unreachable|stackalloc|interface|bitfield|override|callconv|alignof|virtual|literal'
             r'|default|sizeof|vaargs|return|extern|struct|attrib|delete|atomic|panic'
             r'|token|while|macro|const|class|trait|ident|super|when|else|loop|type|expr'
             r'|enum|goto|null|this|asm|new|for|pub|use|mod|inl|tls|let|mut|fun'
             r'|get|set|as\??|!?is|!?in|op|if|do)\b', Keyword)
        ],
        'primitive_keyword': [
            (r'\b(isize|i64|i32|i16|i8|usize|u64|u32|u16|u8'
             r'|f64|f32|void|char|bool|string)\b', Keyword.Type)
        ],
        'literal_keyword': [
            (r'\b(null|true|false)\b', Keyword.Constant)
        ],
        'ident': [
            (r'\b[a-zA-Z_]+[a-zA-Z_0-9]*\b', Name)
        ]
    }