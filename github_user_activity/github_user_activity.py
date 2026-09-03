import requests
import argparse

def main():
    parser = argparse.ArgumentParser("getting username")
    parser.add_argument('username',help = "enter a valid github username")
    args = parser.parse_args()
    username = args.username
    url = f"https://api.github.com/users/{username}/events"
    data = requests.get(url)
    response = data.json()
    if response["status"] == "404":
        print("NO SUCH USE EXISTS! TRY AGAIN WITH VALID USERNAME.")
        return
    n = len(response)
    if n==0:
        print("No user data")
    i = 0
    while i< n-1:
        x = 1
        while(i<n-1 and response[i]["type"] == response[i+1]["type"] and response[i]["repo"]["id"]==response[i+1]["repo"]["id"]):
            i+=1
            x+=1
        repo = response[i]["repo"]["url"]
        repo = repo.removeprefix("https://api.github.com/repos/")
        match response[i]["type"]:
            case "PushEvent":
                print(f"Pushed {x} commits to {repo}")
            case "CreateEvent":
                print(f"Create {x} new repo {repo}")
            case "PullRequestEvent":
                print(f"Made {x} Pull requests in {repo}")
            case "IssueCommentEvent":
                print(f"{response[i]["payload"]["action"]} {x} comment in {repo}")
            case "PullRequestReviewEvent":
                print(f"Reviewd {x} pull request {response[i]['payload']['pull_request']['number']}")
            case "IssueEvent":
                print(f"Created {x} issue(s) in {repo}")
            case _:
                print(f"{response[i]["type"]}")
        i+=1

if __name__ == "__main__":
    main()