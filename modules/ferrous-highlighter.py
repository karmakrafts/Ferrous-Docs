# @author Alexander Hinze
# @since 17/11/2023

import re
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
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            (r'(//.*?)(\n)', bygroups(Comment.Single, Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline),
            include('attrib_usage'),
            include('udt'),
            include('function'),
            include('params'),
            include('generic_params'),
            include('callconv_mod'),
            include('type'),
            include('keyword'),
            include('int_literal'),
            include('ident'),
            (r'[,.{}()]', Punctuation),
            (r'[^\S\n]+', Whitespace)
        ],
        'udt': [
            (r'(\bstruct|interface|trait|attrib|enum\s+class|enum\b)(\s*)([^{]+)(\s*)({)', bygroups(Keyword, Whitespace, using(this), Whitespace, Punctuation), 'udt_body')
        ],
        'udt_body': [
            (r'}', Punctuation, '#pop'),
            include('root')
        ],
        'type': [
            include('ref_type'),
            include('ptr_type'),
            include('primitive_keyword'),
            include('ident')
        ],
        'ptr_type': [
            (r'(\*)([^\s]+)', bygroups(Punctuation, using(this)))
        ],
        'ref_type': [
            (r'(&)([^\s]+)', bygroups(Punctuation, using(this)))
        ],
        'function': [
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))(\s*)(:)(\s*)([^\s{]+)(\s*)({)(\s*)', bygroups(Keyword, Whitespace, Name.Function, Punctuation, using(this), Punctuation, Whitespace, Punctuation, Whitespace, using(this), Whitespace, Punctuation, Whitespace), 'function_body'),
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))(\s*)(:)(\s*)([^\s]+)', bygroups(Keyword, Whitespace, Name.Function, Punctuation, using(this), Punctuation, Whitespace, Punctuation, Whitespace, using(this))),
            (r'(\bfun\b)(\s*)([^\(\s]+)(\()([^\)]+)(\))', bygroups(Keyword, Whitespace, Name.Function, Punctuation, using(this), Punctuation))
        ],
        'function_body': [
            (r'}', Punctuation, '#pop'),
            include('variable'),
            include('return_statement'),
            include('root')
        ],
        'variable': [
            (r'(\blet\b)(\s*)(\bmut\b)(\s*)([^\s:]+)(\s*)(:)(\s*)([^\s;]+)(\s*)(=)(\s*)([^;\s]+)(\s*)', bygroups(Keyword, Whitespace, Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace, Punctuation, Whitespace, using(this), Whitespace)),
            (r'(\blet\b)(\s*)(\bmut\b)(\s*)([^\s:]+)(\s*)(=)(\s*)([^;\s]+)(\s*)', bygroups(Keyword, Whitespace, Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace)),
            (r'(\blet\b)(\s*)(\bmut\b)(\s*)([^\s:]+)(\s*)(:)(\s*)([^;\s]+)(\s*)', bygroups(Keyword, Whitespace, Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace)),
            (r'(\blet\b)(\s*)([^\s:]+)(\s*)(=)(\s*)([^;\s]+)(\s*)', bygroups(Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace)),
            (r'(\blet\b)(\s*)([^\s:]+)(\s*)(:)(\s*)([^\s]+)(\s*)(=)(\s*)([^;\s]+)(\s*)', bygroups(Keyword, Whitespace, Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace, Punctuation, Whitespace, using(this), Whitespace))
        ],
        'params': [
            (r'([^\s:]+)(\s*)(:)(\s*)([^\s]+)(\s*)(,)([^,]+)', bygroups(Name, Whitespace, Punctuation, Whitespace, using(this), Whitespace, Punctuation, using(this))),
            (r'([^\s:]+)(\s*)(:)(\s*)([^\s]+)', bygroups(Name, Whitespace, Punctuation, Whitespace, using(this)))
        ],
        'generic_params': [
            (r'(<)([^>]+)(>)', bygroups(Punctuation, using(this), Punctuation))
        ],
        'attrib_usage': [
            (r'@\s*\b[a-zA-Z_]+[a-zA-Z_0-9]*\b', Name.Decorator)
        ],
        'callconv_mod': [
            (r'(\bcallconv\b)\s*(\()([^\)]+)(\))', bygroups(Keyword, Punctuation, Name, Punctuation))
        ],
        'return_statement': [
            (r'(\breturn\b)(\s*)([^\s]+)(\s*)', bygroups(Keyword, Whitespace, using(this), Whitespace)),
            (r'(\breturn\b)(\s*)', bygroups(Keyword, Whitespace))
        ],
        'keyword': [
            include('misc_keyword'),
            include('primitive_keyword'),
            include('literal_keyword')
        ],
        'int_literal': [
            include('dec_int_literal')
        ],
        'dec_int_literal': [
            (r'(?:(?<![0-9a-zA-Z_]))([0-9_]+)', Number.Integer)
        ],
        'misc_keyword': [
            (r'(\bunreachable\b|\bstackalloc\b|\binterface\b|\bbitfield\b|\boverride\b|\bcallconv\b|\balignof\b|\bvirtual\b|\bliteral\b'
             r'|\bdefault\b|\bsizeof\b|\bvaargs\b|\breturn\b|\bextern\b|\bstruct\b|\battrib\b|\bdelete\b|\batomic\b|\bpanic\b'
             r'|\btoken\b|\bwhile\b|\bmacro\b|\bconst\b|\btrait\b|\bident\b|\bsuper\b|\bwhen\b|\belse\b|\bloop\b|\btype\b|\bexpr\b'
             r'|\benum\b|\bgoto\b|\bnull\b|\bthis\b|\basm\b|\bnew\b|\bfor\b|\bpub\b|\buse\b|\bmod\b|\binl\b|\btls\b|\blet\b|\bmut\b|\bfun\b'
             r'|\bget\b|\bset\b|as\??|!?is|!?in|\bop\b|\bif\b|\bdo\b)', Keyword)
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