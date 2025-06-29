from clean_training_data import clean_lua, clean_luau, clean_py, clean_r, clean_racket, clean_ml, clean_julia, clean_generic

LANG_CONFIG = {
    # Lisp/Clojure
    'clj':    {'line_comment': ';',    'block_comment': ('#_', ''),       'stop_tokens': ['(deftest', '(ns']},
    # C family
    'cpp':    {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['TEST(', 'int main']},
    'cs':     {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['[Test]', 'static void Main']},
    # Dart
    'dart':   {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['test(', 'void main']},
    # D
    'd':      {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['unittest', 'void main']},
    # Elixir
    'elixir': {'line_comment': '#',    'block_comment': ('"""','"""'), 'stop_tokens': ['ExUnit']},
    # Go
    'go':     {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['func Test']},
    # Haskell
    'hs':     {'line_comment': '--',   'block_comment': ('{-','-}'),     'stop_tokens': ['main =']},
    # Java / Scala / Kotlin family
    'java':   {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['@Test', 'public static void main']},
    'jl':     {'line_comment': '#',    'block_comment': ('#=','#='),      'stop_tokens': ['@test']},
    'js':     {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['describe(', 'test(']},
    'ts':     {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['describe(', 'test(']},
    # Lua
    'lua':    {'line_comment': '--',   'block_comment': ('--[[', ']]'),   'stop_tokens': ['function']},
    'luau':   {'line_comment': '--',   'block_comment': ('--[[', ']]'),   'stop_tokens': ['function']},
    # MATLAB
    'matlab': {'line_comment': '%',    'block_comment': ('%{','%}'),     'stop_tokens': ['function']},
    # OCaml / ML
    'ml':     {'line_comment': '(*',   'block_comment': ('(*','*)'),     'stop_tokens': ['let assertions']},
    # PHP / Prolog
    'php':    {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['function test', '<?php']},
    'pl':     {'line_comment': '%',    'block_comment': ('/*','*/'),     'stop_tokens': [':-']},
    # Ruby
    'rb':     {'line_comment': '#',    'block_comment': ('=begin','=end'), 'stop_tokens': ['RSpec.describe', 'def test']},
    # Racket
    'rkt':    {'line_comment': ';',    'block_comment': ('#|','|#'),     'stop_tokens': ['(require rackunit)']},
    # R
    'r':      {'line_comment': '#',    'block_comment': (None, None),     'stop_tokens': ['test_humaneval']},
    # Rust
    'rs':     {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['fn main', 'assert!']},
    # Scala
    'scala':  {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['should', 'object']},
    # Shell
    'sh':     {'line_comment': '#',    'block_comment': (None, None),     'stop_tokens': ['exit']},
    # Swift
    'swift':  {'line_comment': '//',   'block_comment': ('/*','*/'),     'stop_tokens': ['XCTest', 'func test']},
    # F#
    'fs':     {'line_comment': '//',   'block_comment': ('(*','*)'),     'stop_tokens': ['[<Test>]']},
}

def clean_sol_prompt(lang, sol):
    if lang == "lua":
        return clean_lua(sol)
    elif lang == "luau":
        return clean_luau(sol)
    elif lang == "py":
        return clean_py(sol)
    elif lang == "racket":
        return clean_racket(sol)
    elif lang == "ml":
        return clean_ml(sol)
    elif lang == "r":
        return clean_r(sol)
    elif lang == "julia":
        return clean_julia(sol)
    # else:
    #     raise Exception("Unknown language: " + lang)
    elif lang in LANG_CONFIG:
        return clean_generic(sol, lang)