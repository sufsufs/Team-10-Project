import openai


openai.api_key = "YOUR_API_KEY"


def request_news_by_filters(category=None, geography="world", date="last month", length=750):
    filters = [
        f"Category: {category}" if category else "No category filter",
        f"Geographical location: {geography}" if geography else "No geography filter",
        f"Date: {date}" if date else "No date filter",
        f"Length: {length} tokens" if length else "No length filter"
    ]
    
    prompt = f"Request news articles based on the following filters:\n{', '.join(filters)}.\nPlease provide the news summary."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides news summaries."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=length if length else 750 
    )

    return response['choices'][0]['message']['content']




print("Test Case 34: All Filters Selected")
print(request_news_by_filters(category="Technology", geography="USA", date="October 2024", length=500))

print("\nTest Case 35: All but Category Filter Selected")
print(request_news_by_filters(geography="Europe", date="October 2024", length=500))

print("\nTest Case 36: All but Geography Filter Selected")
print(request_news_by_filters(category="Health", date="October 2024", length=500))

print("\nTest Case 37: All but Date Filter Selected")
print(request_news_by_filters(category="Finance", geography="Asia", length=500))

print("\nTest Case 38: All but Length Filter Selected")
print(request_news_by_filters(category="Science", geography="Global", date="September 2024"))
