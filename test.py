from graphqlclient import GraphQLClient
import json
from students import *

url = "https://api.github.com/graphql"
client = GraphQLClient(url)
client.inject_token("c867e6b3725007d868db2bb1a49814476d0a9b99")
result = client.execute('''
{
  repository(owner: "kossiitkgp", name: "kossiitkgp.github.io") {
    open: issues(last: 100, states: OPEN) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first: 10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
    closed: issues(last: 100, states: CLOSED) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first: 10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
    openPR: pullRequests(last: 100, states: OPEN) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first: 10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
    closedPR: pullRequests(last: 100, states: CLOSED) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first: 10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
    mergedPR: pullRequests(last: 100, states: MERGED) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first: 10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
  }
}
''')


result = json.loads(result)

openissues = result['data']['repository']['open']['edges']
closedissues = result['data']['repository']['closed']['edges']
openPR = result['data']['repository']['openPR']['edges']
closedPR = result['data']['repository']['closedPR']['edges']
mergedPR = result['data']['repository']['mergedPR']['edges']


dict = {}

for node in openissues:
    title  = node['node']['title']
    author = node['node']['author']['login']
    tagslist = []
    for tags in node['node']['labels']['edges']:
        tagslist.append(tags['node']['name'])

    if not (str(author) in dict):
        dict[str(author)] = students(str(author))
        dict[str(author)].numOfCreatedIssue = dict[str(author)].numOfCreatedIssue + 1
    else:
        dict[str(author)].numOfCreatedIssue = dict[str(author)].numOfCreatedIssue + 1


    alltags = ", ".join(str(p) for p in tagslist)
    print(str(title)+ " : "+ str(alltags) + "|" + "createdBy" + "(" + str(author) + ")" )
    print("\n")

print("-"*75)

for node in closedissues:
    title  = node['node']['title']
    author = node['node']['author']['login']
    tagslist = []
    for tags in node['node']['labels']['edges']:
        tagslist.append(tags['node']['name'])

    if not (str(author) in dict):
        dict[str(author)] = students(str(author))
        dict[str(author)].numOfCreatedIssue = dict[str(author)].numOfCreatedIssue + 1
    else:
        dict[str(author)].numOfCreatedIssue = dict[str(author)].numOfCreatedIssue + 1

    alltags = ", ".join(str(p) for p in tagslist)
    print(str(title)+ " : "+ str(alltags) + "|" + "(" + str(author) + ")")
    print("\n")

print("-"*75)


for node in openPR:
    title = node['node']['title']
    author = node['node']['author']['login']
    tagslist = []
    for tags in node['node']['labels']['edges']:
        tagslist.append(tags['node']['name'])

    if not(str(author) in dict):
        dict[str(author)] = students(str(author))
        dict[str(author)].numOfOpenPr = dict[str(author)].numOfOpenPr + 1
    else:
        dict[str(author)].numOfOpenPr = dict[str(author)].numOfOpenPr + 1

    alltags = ", ".join(str(p) for p in tagslist)
    print(str(title)+ " : "+ str(alltags) + " | " + "opened" + "(" + str(author) + ")")
    print("\n")

print("-"*75)

for node in closedPR:
    title = node['node']['title']
    author = node['node']['author']['login']
    tagslist = []
    for tags in node['node']['labels']['edges']:
        tagslist.append(tags['node']['name'])

    if not(str(author) in dict):
        dict[str(author)] = students(str(author))
        dict[str(author)].numOfClosedPr = dict[str(author)].numOfClosedPr + 1
    else:
        dict[str(author)].numOfClosedPr = dict[str(author)].numOfClosedPr + 1

    alltags = ", ".join(str(p) for p in tagslist)
    try:
        print(str(title)+ " : "+ str(alltags) + " | " + "closed" + "(" + str(author) + ")")
    except:
        print("ONE MISSED")

    print("\n")

print("-"*75)

for node in closedPR:
    title = node['node']['title']
    author = node['node']['author']['login']
    tagslist = []
    for tags in node['node']['labels']['edges']:
        tagslist.append(tags['node']['name'])

    if not(str(author) in dict):
        dict[str(author)] = students(str(author))
        dict[str(author)].numOfOPr = dict[str(author)].numOfOpenPr + 1
    else:
        dict[str(author)].numOfOpenPr = dict[str(author)].numOfOpenPr + 1

    alltags = ", ".join(str(p) for p in tagslist)
    try:
        print(str(title)+ " : "+ str(alltags) + " | " + "Merged" + "(" + str(author) + ")")
    except:
        print("ONE MISSED")

    print("\n")

print("-"*75)


for key in dict:
    print("numOfCreatedIssue by " + str(dict[key].name) + " is " + str(dict[key].numOfCreatedIssue))
    print("numOfOpenPr by       " + str(dict[key].name) + " is " + str(dict[key].numOfOpenPr))
    print("numOfClosedPr by     " + str(dict[key].name) + " is " + str(dict[key].numOfClosedPr))
    print("numOfMergedPr by     " + str(dict[key].name) + " is " + str(dict[key].numOfMergedPr))
    print("-"*50)

print("-"*50)


