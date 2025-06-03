
# Return a youtube link for the given query
def get_youtube_link(query):
    formatted_query = query.strip().replace("\"", "").replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={formatted_query}"