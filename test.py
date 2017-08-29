from graphqlclient import GraphQLClient
import json
from students import *

url = "https://api.github.com/graphql"
client = GraphQLClient(url)
client.inject_token("ABCD")
result = client.execute('''
query allissues{
  repository(owner:"kossiitkgp", name:"kossiitkgp.github.io") {
    open :issues(last:100, states:OPEN) {
      edges {
        node {
          title
          author {
            login
          }
          labels(first:10) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
    closed :issues(last:100, states:CLOSED){
      edges{
        node{
          title
          author{
            login
          }
          labels(first:10){
            edges{
              node{
                name
              }
            }
          }
        }
      }
    }
  }
}''')


result = json.loads(result)

openissues = result['data']['repository']['open']['edges']
closedissues = result['data']['repository']['closed']['edges']

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
    print(str(title)+ " : "+ str(alltags))
    print(str(author))


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
    print(str(title)+ " : "+ str(alltags))
    print(str(author))

print("-"*50)

for key in dict:
    print("numOfCreatedIssue by " + str(dict[key].name) + " is " + str(dict[key].numOfCreatedIssue))


#print(result)
