import googletrans

print(googletrans.LANGUAGES) # 나라코드: 나라이름 dict

tr = googletrans.Translator()
result = tr.translate("hello", src="en", dest="ko")
print(result.text)
