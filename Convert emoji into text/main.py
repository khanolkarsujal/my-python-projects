import demoji

#remove emojis from text

text = "Good morning! ☀️ 🌸"

a1 = demoji.replace(text , "")

print(a1)


# replace the emoji with descriptive text

text1 = "Happy birthday! 🎂🎈"
a2 = demoji.replace_with_desc(text)
print(a2)

# dectection emoji in a string 

text = "Good morning ☀️😊"

emoji = demoji.findall(text)

print(emoji)




