import codecs
with codecs.open('backend_test_output.txt', 'r', 'utf-16le') as f:
    data = f.read()
for kw in ('Traceback', 'Exception', 'Error', 'TypeError', 'ValueError', 'AttributeError', 'HTTPError', '500'):
    if kw in data:
        print('===', kw, '===')
        start = data.index(kw)
        end = min(len(data), start + 2000)
        print(data[start:end])
        print()
print('--- END ---')
