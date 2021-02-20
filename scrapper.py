import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


def extract_job(html):
    html1 = html.find("div", {"class": "fl1"})
    title = html1.find("h2").find("a")["title"]
    company, location = html1.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True).strip(" \r")
    location = location.get_text(strip=True).strip(" \r")
    job_id = html['data-jobid']

    return {'title': title, 'company': company, 'location': location, "aplly_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scraaping SO: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
