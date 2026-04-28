# reverse all word...eg - I like your watch :>>> watch your like I
str1 = "I like your watch"
new_list = list(str1)
rev = new_list[: : -1]

print(f"#After reversing all word>> {rev}")