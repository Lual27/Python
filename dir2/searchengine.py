import webbrowser
website = input("search website: ")

if website == "google":
  name = input("search: ")
  webbrowser.open("https://www.google.com/search?q=" + name)

elif website == "youtube":
  name = input("search: ")
  webbrowser.open("https://www.youtube.com/watch?v=" + name)
  
elif website == "chatgbt":
  name = input("search: ")
  webbrowser.open("https://chat.openai.com/chat" + name)