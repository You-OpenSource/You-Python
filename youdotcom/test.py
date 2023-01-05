from search import Search

search_results = Search.search_for("how to make an python loop?")  # search! No need to use the Init class.

print(search_results["results"])  # print all the search results

print(search_results["time"])  # print the total time taken (les then 3 seconds on average)
