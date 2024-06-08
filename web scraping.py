from bs4 import BeautifulSoup
import requests
import time

print('PYTHON JOB SEARCHING')

# Filter out the wanted jobs
print("Enter a skill you have (apart from Python) ")
yes_skills = input(">>")

print('Enter a skill you do not have ')
no_skills = input(">>")

print(f'Filtering out the job that require {yes_skills} and do not require {no_skills}')

#Function to scrape the website to find suitable jobs
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text

        #Filter out the jobs that were posted a few days ago , or moths/years ago in order to get the jobs that are still accepting applications
        if "few" not in published_date or "month" not in published_date or "year" not in published_date:
            
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            

            #find the list of skills the job p[ost requires]
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            # print(skills)
            
            #Find only the jobs that you are elligible for 
            if yes_skills in skills and no_skills not in skills:
                more_info = job.header.h2.a['href']
                
                #Save each job info in a file 
                with open(f'search results/ {index}.txt','w') as f:
                    f.write(f'Comapny Name: {company_name.strip()} \n')
                    f.write(f'Skills Required : {skills.strip()} \n')
                    f.write(f'More info : {more_info} \n')
                print(f'File Saved : {index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 24
        #update the list every 24 hours so to get the latest jobs on the site
        print("List will be updated after 24 hours  ")
        time.sleep(time_wait*60*60)






