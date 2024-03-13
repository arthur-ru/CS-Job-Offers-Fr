import requests
from bs4 import BeautifulSoup
import csv

def get_web_frameworks():
    url = "https://github.com/sindresorhus/awesome?tab=readme-ov-file"
    response = requests.get(url)

    frameworks = set()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Adjust the CSS selector based on the structure of the webpage
        framework_elements = soup.select(".markdown-body li a")

        for element in framework_elements:
            framework = element.text.strip()
            frameworks.add(framework)

        return frameworks
    else:
        print(f"Error: {response.status_code}")
        return set()

# Example usage
web_frameworks = get_web_frameworks()
print("Web Development Frameworks:", web_frameworks)


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["hardskills"])

        for framework in data:
            csv_writer.writerow([framework])
save_to_csv(web_frameworks, "/data/hardkills.csv")