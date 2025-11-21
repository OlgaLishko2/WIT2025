# # Example highlighted_poems string
# highlighted_poems = "The Shadow:William Carlos Williams:1915, Spring Storm:William Carlos Williams:1921, Love, Maybe:Audre Lorde:1985"

# # Step 1: print the original string
# print(highlighted_poems)

# # Step 2: split the string by commas
# highlighted_poems_list = highlighted_poems.split(",")

# # Step 3: print the split list
# print(highlighted_poems_list)

# # Step 4: strip whitespace from each poem
# highlighted_poems_stripped = []
# for poem in highlighted_poems_list:
#     highlighted_poems_stripped.append(poem.strip())

# # Step 5: print the cleaned list
# print(highlighted_poems_stripped)

# # Step 6: prepare list of lists
# highlighted_poems_details = []

# # Step 7: split each poem's info by ':'
# for poem in highlighted_poems_stripped:
#     highlighted_poems_details.append(poem.split(":"))

# # Step 8: create separate lists for titles, poets, and dates
# titles = []
# poets = []
# dates = []

# # Step 9: populate the lists
# for poem_info in highlighted_poems_details:
#     titles.append(poem_info[0])
#     poets.append(poem_info[1])
#     dates.append(poem_info[2])

# # Step 10: print formatted output
# for i in range(len(titles)):
#     print("The poem {title} was published by {poet} in {date}.".format(
#         title=titles[i], poet=poets[i], date=dates[i]
#     ))





print("!!!!!!!!!!!!!!!!!")