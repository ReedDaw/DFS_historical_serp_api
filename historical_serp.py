import pandas as pd
from client import RestClient

# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("user_name", "pw")

post_data = dict()
# Simple way to set a task
post_data[len(post_data)] = dict(
    keyword="albert einstein",
    location_name="United States",
    language_name="English"
)

# POST /v3/dataforseo_labs/google/historical_serps/live
response = client.post("/v3/dataforseo_labs/google/historical_serps/live", post_data)

# Function to save the response to a CSV file using pandas
def save_response_to_csv(response, filename='response.csv'):
    if response["status_code"] == 20000:
        # Extract the relevant part of the response
        tasks = response.get("tasks", [])
        
        if tasks:
            result_data = tasks[0].get("result", [])
            
            # Normalize the result data
            normalized_data = pd.json_normalize(result_data, 
                                                sep='_', 
                                                record_path=['items', 'items'], 
                                                meta=[
                                                    ['items', 'se_type'],
                                                    ['items', 'type'],
                                                    ['items', 'rank_group'],
                                                    ['items', 'rank_absolute'],
                                                    ['items', 'position'],
                                                    ['items', 'xpath'],
                                                    ['items', 'domain'],
                                                    ['items', 'title'],
                                                    ['items', 'url'],
                                                    ['items', 'breadcrumb'],
                                                    ['items', 'website_name'],
                                                    ['items', 'is_image'],
                                                    ['items', 'is_video'],
                                                    ['items', 'is_featured_snippet'],
                                                    ['items', 'is_malicious'],
                                                    ['items', 'description'],
                                                    ['items', 'pre_snippet'],
                                                    ['items', 'extended_snippet'],
                                                    ['items', 'amp_version'],
                                                    ['items', 'rating'],
                                                    ['items', 'highlighted'],
                                                    ['items', 'links'],
                                                    ['items', 'about_this_result'],
                                                    ['items', 'main_domain'],
                                                    ['items', 'relative_url'],
                                                    ['items', 'etv'],
                                                    ['items', 'impressions_etv'],
                                                    ['items', 'estimated_paid_traffic_cost'],
                                                    ['items', 'clickstream_etv'],
                                                    ['items', 'rank_changes'],
                                                    ['items', 'backlinks_info'],
                                                    ['items', 'rank_info'],
                                                ],
                                                errors='ignore')
            
            # Write the DataFrame to a CSV file
            normalized_data.to_csv(filename, index=False)
            print(f"Response saved to {filename}")
        else:
            print("No result data found in the response.")
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

# Save the response to a CSV file
save_response_to_csv(response)
