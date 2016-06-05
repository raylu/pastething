#new paste defaults
defaults = {
	'ttl': 1.0,
	'lexer': 'auto',
	'burn': 0,
	'paste': '',
}

#paste options
ttl_max = 730 #maximum allowed paste ttl in hours
ttl_min = 0 #minimum allowed paste ttl in hours
token_len = 6 #delete token length in bytes/characters

#flask configuration
secret_key = 'some_secret'
max_content_length = 10 * 1024 * 1024 #max form upload size in bits

#paste url
url_len = 1 #minimum paste url length in characters
url_alph = tuple("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghkmnpqrstuvwxyz") #alphabet used to generate paste url
base = len(url_alph)

#error messages
empty_paste = "pls, actually paste something k?\n"
invalid_ttl = "ttl must be between " + str(ttl_min) + " and " + str(ttl_max) +" hours\n"


#form options
ttl_options = {
	'5 minutes': 0.0833,
	'15 minutes': 0.25,
	'30 minutes': 0.5,
	'1 hour': 1,
	'3 hours': 3,
	'6 hours': 6,
	'12 hours': 12,
	'1 day': 24,
	'3 days': 72,
	'1 week': 168,
	'2 weeks': 336,
	'1 month': 730,
}

common_lexers = {
	'Bash': 'bash',
	'C': 'c',
	'C++': 'cpp',
	'C#': 'csharp',
	'Python': 'python',
	'Ruby': 'ruby',
	'Go': 'go',
	'Perl': 'perl',
	'PHP': 'php',
	'CSS': 'css',
	'HTML': 'html',
	'JavaScript': 'javascript',
	'JSON': 'json',
	'XML': 'xml',
	'SQL': 'sql',
}
