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
        'comment': [
            (r'(//.*?)(\n)', 
                bygroups(Comment.Single, Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'default': [
            (r'[,.{}()\[\]:]', Punctuation),
            (r'[^\S\n]+', Whitespace)
        ],
        'root': [
            include('comment'),
            include('attrib_usage'),
            include('mod_block'),
            include('udt'),
            include('function'),
            include('statement'),
            include('misc_keyword'),
            include('default')
        ],
        'mod_block': [
            (r'(\bmod\b)(\s*?)([^\s{]+)(\s*?)({)', 
                bygroups(Keyword, Whitespace, using(this), Whitespace, Punctuation), 'mod_block_body')
        ],
        'mod_block_body': [
            (r'}', Punctuation, '#pop'),
            include('root')
        ],
        'operator': [
            (r'[=+\-*/%<>!&|\^]', Operator) # Covers all combinations of operators wihout any validation
        ],
        'udt': [
            (r'(\bstruct|interface|trait|attrib|enum\b)(\s*)([^{]+)', 
                bygroups(Keyword, Whitespace, using(this)), 'udt_type'),
            include('generic_param')
        ],
        'udt_type': [
            (r'{', Punctuation, '#pop', 'udt_body'),
            include('generic_param')
        ],
        'udt_body': [
            (r'}', Punctuation, '#pop'),
            include('root')
        ],
        'function_type': [
            (r'\(', Punctuation, 'function_type_params')
        ],
        'function_type_params': [
            (r'(\))(\s*?)(->)', 
                bygroups(Punctuation, Whitespace, Punctuation), '#pop', 'function_type_return_type'),
            (r'\)', Punctuation, '#pop'),
            include('type'),
            include('default')
        ],
        'function_type_return_type': [
            (r'[,;:)\s]', Punctuation, '#pop'),
            include('type')
        ],
        'type_alias': [
            (r'(\btype\b)(\s*)([^\s=]+)(\s*)', bygroups(Keyword, Whitespace, Name, Whitespace), 'type_alias_type')
        ],
        'type_alias_type': [
            (r';|$', Punctuation, '#pop'),
            include('type')
        ],
        'ptr_type': [
            (r'\*', Punctuation, 'type_mode'),
            include('type')
        ],
        'ref_type': [
            (r'&', Punctuation, 'type_mode'),
            include('type')
        ],
        'type_mode': [
            (r'[,;)}\]\s\t\n]', Punctuation, '#pop'),
            include('type')
        ],
        'type': [
            (r'\bmut\b', Keyword),
            include('function_type'),
            include('ptr_type'),
            include('ref_type'),
            include('primitive_keyword'),
            include('qualified_ident'),
            include('ident')
        ],
        'function': [
            (r'(\bfun\b)(\s*?)([^\(\s]+)(\()', 
                bygroups(Keyword, Whitespace, Name.Function, Punctuation), 'function_sig'),
            include('statement')
        ],
        'function_sig': [
            (r'(\))(\s*?)(:)(\s*?)([^{\s]+)(\s*?)({)(\s*?)', 
                bygroups(Punctuation, Whitespace, Punctuation, Whitespace, using(this), Whitespace, Punctuation, Whitespace), '#pop', 'function_body'),
            (r'(\))(\s*?)({)(\s*?)', 
                bygroups(Punctuation, Whitespace, Punctuation, Whitespace), '#pop', 'function_body'),
            (r'(\))(\s*?)(:)(\s*?)([^\s;]+)(\s*?)', 
                bygroups(Punctuation, Whitespace, Punctuation, Whitespace, using(this), Whitespace), '#pop'),
            (r'\)', Punctuation, '#pop'),
            include('param'),
            include('type'),
            include('default')
        ],
        'function_body': [
            (r'}', Punctuation, '#pop'),
            include('function'), # Allow any depth of nested functions
            include('statement'),
            include('default')
        ],
        'statement': [
            include('type_alias'),
            include('variable'),
            include('return_statement'),
            include('expr')
        ],
        'call_expr': [
            (r'([^:]+)(::)(\b[a-zA-Z_]+[a-zA-Z_0-9]*\b)(\s*)(\()', 
                bygroups(using(this), Punctuation, Name.Function, Whitespace, Punctuation), 'call_expr_params'),
            (r'(\b[a-zA-Z_]+[a-zA-Z_0-9]*\b)(\s*)(\()', 
                bygroups(Name.Function, Whitespace, Punctuation), 'call_expr_params')
        ],
        'call_expr_params': [
            (r'\)', Punctuation, '#pop'),
            include('expr'),
            include('default')
        ],
        'expr': [
            include('call_expr'),
            include('literal'),
            include('misc_keyword'),
            include('primitive_keyword'),
            include('qualified_ident'),
            include('ident'),
            include('operator'),
            include('default')
        ],
        'literal': [
            include('string_literal'),
            include('literal_keyword'),
            include('real_literal'),
            include('int_literal')
        ],
        'variable': [
            (r'(\blet\b)(\s*)(\bmut\b)(\s*)([^:;,\s]+)(\s*)(:)(\s*)', 
                bygroups(Keyword, Whitespace, Keyword, Whitespace, Name.Variable, Whitespace, Punctuation, Whitespace), 'variable_type'),
            (r'(\blet\b)(\s*)([^:;,\s]+)(\s*)(:)(\s*)', 
                bygroups(Keyword, Whitespace, Name.Variable, Whitespace, Punctuation, Whitespace), 'variable_type')
        ],
        'variable_type': [
            include('comment'),
            (r'(\s*)(=)(\s*)', 
                bygroups(Whitespace, Operator, Whitespace), 'variable_initializer'),
            (r';|$', Punctuation, '#pop'),
            include('type')
        ],
        'variable_initializer': [
            include('comment'),
            (r';|$', Punctuation, '#pop'),
            include('expr')
        ],
        'param': [
            (r'([^\s:]+)(\s*)(:)', 
                bygroups(Name.Variable, Whitespace, Punctuation), 'param_type')
        ],
        'param_type': [
            include('comment'),
            (r'[),;]|$', Punctuation, '#pop'),
            include('type'),
            include('default')
        ],
        'generic_param': [
            (r'(<)([^>]+)(>)', 
                bygroups(Punctuation, using(this), Punctuation))
        ],
        'attrib_usage': [
            (r'@\s*\b[a-zA-Z_]+[a-zA-Z_0-9]*\b', Name.Decorator)
        ],
        'callconv_mod': [
            (r'(\bcallconv\b)(\s*)(\()([^\)]+)(\))', 
                bygroups(Keyword, Whitespace, Punctuation, Name, Punctuation))
        ],
        'return_statement': [
            (r'(\breturn\b)(\s*)([^\s]+)', 
                bygroups(Keyword, Whitespace, using(this))),
            (r'(\breturn\b)', Keyword)
        ],
        'real_literal': [
            (r'(?:(?<![0-9a-zA-Z_]))[0-9_]+\.(?:[0-9_]*)f(32|64)', Number.Float),
            (r'(?:(?<![0-9a-zA-Z_]))[0-9_]+\.(?:[0-9_]*)', Number.Float)
        ],
        'int_literal': [
            include('hex_int_literal'),
            include('oct_int_literal'),
            include('bin_int_literal'),
            include('dec_int_literal')
        ],
        'dec_int_literal': [
            (r'(?:(?<![0-9a-zA-Z_]))[0-9_]+[iu](size|8|16|32|64)', Number.Integer),
            (r'(?:(?<![0-9a-zA-Z_]))[0-9_]+', Number.Integer)
        ],
        'hex_int_literal': [
            (r'0[xX][0-9a-fA-F_]+[iu](size|8|16|32|64)', Number.Hex),
            (r'0[xX][0-9a-fA-F_]+', Number.Hex)
        ],
        'oct_int_literal': [
            (r'0[oO][0-7_]+[iu](size|8|16|32|64)', Number.Oct),
            (r'0[oO][0-7_]+', Number.Oct)
        ],
        'bin_int_literal': [
            (r'0[bB][01_]+[iu](size|8|16|32|64)', Number.Bin),
            (r'0[bB][01_]+', Number.Bin)
        ],
        'misc_keyword': [
            (r'(\bunreachable\b|\bstackalloc\b|\binterface\b|\bbitfield\b|\boverride\b|\bcallconv\b|\balignof\b|\bvirtual\b|\bliteral\b'
             r'|\bdefault\b|\bsizeof\b|\bvaargs\b|\breturn\b|\bextern\b|\bstruct\b|\battrib\b|\bdelete\b|\batomic\b|\bpanic\b'
             r'|\btoken\b|\bwhile\b|\bmacro\b|\bconst\b|\btrait\b|\bident\b|\bsuper\b|\bwhen\b|\belse\b|\bloop\b|\btype\b|\bexpr\b'
             r'|\benum\b|\bgoto\b|\bnull\b|\bthis\b|\basm\b|\bnew\b|\bfor\b|\bpub\b|\buse\b|\bmod\b|\binl\b|\btls\b|\blet\b|\bmut\b|\bfun\b'
             r'|\bget\b|\bset\b|(\bas\b\??)|(!?\bis\b)|(!?\bin\b)|\bop\b|\bif\b|\bdo\b)', Keyword)
        ],
        'primitive_keyword': [
            (r'\b(isize|i64|i32|i16|i8|usize|u64|u32|u16|u8'
             r'|f64|f32|void|char|bool|string)\b', Keyword.Type)
        ],
        'literal_keyword': [
            (r'\b(null|true|false)\b', Keyword.Constant)
        ],
        'qualified_ident': [
            (r'([^:]+)(::)(\b[a-zA-Z_]+[a-zA-Z_0-9]*\b)', 
                bygroups(using(this), Punctuation, Name)),
        ],
        'ident': [
            (r'\b[a-zA-Z_]+[a-zA-Z_0-9]*\b', Name)
        ],
        'string_literal': [
            include('cml_string'),
            include('ml_string'),
            include('string')
        ],
        'string': [
            (r'"', String, 'string_text')
        ],
        'string_text': [
            (r'"', String, '#pop'),
            (r'[^"]+', String)
        ],
        'ml_string': [
            (r'#"', String, 'ml_string_text')
        ],
        'ml_string_text': [
            (r'"#', String, '#pop'),
            include('string'),
            (r'[^("#)]+', String)
        ],
        'cml_string': [
            (r'/"', String, 'cml_string_text')
        ],
        'cml_string_text': [
            (r'"/', String, '#pop'),
            include('string'),
            (r'[^("/)]+', String)
        ]
    }