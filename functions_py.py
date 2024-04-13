def centre_text(text):
    left_margin = (80-len(text)) // 2
    print(" " * left_margin, text)

centre_text("eggs")
centre_text("eggs and butter")
centre_text("eggs, butter and milk")
    