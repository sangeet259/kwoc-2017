#import requests
#import traceback 
#import json 
#import os
from students import *

def get_commits(username, repo_name):
    '''
    username : 'kshitij10496'
    repo_name : 'kshitij10496/IIKH'
                'sympy/sympy'
    '''
    # total_commits = 0
    # total_additions, total_deletions, total_changes = 0, 0, 0
    
    # user = g.get_user(username)
    # repo = g.get_repo(repo_name)
    # starting_date = datetime.datetime(2016, 5, 1)
    # ending_date = datetime.datetime(2016, 12, 31)
    # all_commits = repo.get_commits(author=username)#, since=starting_date, until=ending_date)
    # for commit in all_commits:
    #     total_additions += int(commit.stats.additions)
    #     total_deletions += int(commit.stats.deletions)
    #     total_changes += int(commit.stats.total)
    #     total_commits += 1
    # # return total_commits
    # print("Total commits: " + str(total_commits))
    # print("Total additions: " + str(total_additions))
    # print("Total deletions: " + str(total_deletions))
    # print("Total changes: " + str(total_changes))
    query = "https://api.github.com/repos/{}/stats/contributors?access_token={}".format(repo_name,os.environ["DEFCON_GITHUB_AUTH_TOKEN"])
    response = requests.get(query).json()
    commits = 0
    try :
        for data in response :
            if data["author"]["login"].lower() == username.lower() :
                commits+=int(data["total"])
        return commits 
    except TypeError :
        msg = "Unable to get commits in {} repo.\nFollowing error occured : {}".format(repo_name,traceback.format_exc())
        slack_notification(msg)
        return 0


def slack_notification(message):
        headers = {
                "Content-Type": "application/json"
        }
        data = json.dumps({
                "text": "In leaderboard.py  following error occured :\n{}".format(message)
        })
        r = requests.post(
                os.environ["SLACK_WEBHOOK_URL"], headers=headers, data=data)

        if r.status_code != 200:
                print("in slack_notification : {}".format(r.status_code))
                print(r.text)


def students_list():
    #get data from data base and make object of students class and append in a list
    alldata = [["dibya","koss",10,20,1000,13,15],["shubham","cricFev",7,23,100000,13,19],["americast","kwoc",10,15,150001,18,19],["rahul","krssg",23,56,33,10000,58],["mehul","robocup",18,52,56984,54,78],["saurabh","bhoot",15,1005,56,21,56]]
    stul = []
    for x in alldata:
        stu = students()
        stu.name = x[0]
        stu.repo_name = x[1]
        stu.numOfOpenPr = x[2]
        stu.numOfClosedPr = x[3]
        stu.numOfLinesAdded = x[4]
        stu.totalCommits = x[5]
        stu.numOfCreatedIssue = x[6]
        stul.append(stu)
    return stul

# alldata a list of object containg all data of a participant 
#object --> name -- repo_name -- total_commits -- openPRs -- closed PR -- total_additions -- total_deletions etc.

def sortByAlpha(alldata):
    return sorted(alldata, key=lambda l:l.name)

def sortByOpenPr(alldata):
    return sorted(alldata, key=lambda l:l.numOfOpenPr)

def sortByClosedPr(alldata):
    return sorted(alldata,key=lambda l:l.numOfClosedPr)

def sortByTotalNumOfLines(alldata):
    return sorted(alldata, key=lambda l:l.numOfLinesAdded)

def printing(alldata):
    for x in alldata:
        print str(x.name) + " --  " +str(x.repo_name) +" -- "+str(x.totalCommits)+" --  "+str(x.numOfOpenPr)+" --  "+str(x.numOfClosedPr)+" -- "+str(x.numOfLinesAdded)+" -- "+str(x.numOfCreatedIssue)+"\n"

if __name__ == '__main__':
    alldata = students_list()
    print "name____repoName____commits____openPR____closedPr____lineAdded____Issue"
    print "____sort by name____"
    printing(sortByAlpha(alldata)) 
    print "____sort by openPr____"
    printing(sortByOpenPr(alldata))
    print "____sort by lines added____"
    printing(sortByTotalNumOfLines(alldata))
    print "____sort by closedPr____"
    printing(sortByClosedPr(alldata))


