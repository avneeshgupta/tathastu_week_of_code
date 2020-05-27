votes_num=int(input("Enter no. of votes to be casted: "))
votes_list=[]
final_list=[]
for x in range(votes_num):
    votes_list.append(input("Enter vote no. "+str(x+1)+": "))
for vote_name in votes_list:
    final_list.append((vote_name,votes_list.count(vote_name)))
final_list.sort(key=lambda x: x[0], )
final_list.sort(key=lambda x: x[1], reverse=True)
print("Candidate recieving max. votes:",final_list[0][0])