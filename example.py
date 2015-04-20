import picnic

picnic.api_key = 'YOUR_API_KEY_HERE'

websites = picnic.list_websites()
print("Websites: {}".format(websites))

website = picnic.get_website('example.com')
print("example.com: {}".format(website))

website.update_content('''
<!doctype html>
<title>hello, world</title>
''')

price = picnic.get_price('picnicisthebest.org')
print("Price: {}".format(price))

new_website = picnic.create_website('thesecondpicnic.com', '''
<!doctype html>
<title>The Second Picnic</title>
''')

