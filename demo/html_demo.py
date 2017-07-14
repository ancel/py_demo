

import html.parser

if __name__ == '__main__':
	# html禁止转义
    html_parser = html.parser.HTMLParser()
    print(html_parser.unescape('Selection Foam &amp; Mattresses'))
