def remove_fourth_character(word: str) -> str:
    before_4th = word[:3]
    after_4th = word[4:]
    new = before_4th + after_4th
    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
