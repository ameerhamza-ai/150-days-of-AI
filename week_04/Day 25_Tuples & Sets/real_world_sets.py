user1_followers = {"Ali", "Sara", "Ameer", "Zara"}
user2_followers = {"Sara", "Hassan", "Ameer", "Nida"}

print(f"User 1: {user1_followers}")
print(f"User 2: {user2_followers}\n")

# 1. Common followers (Intersection &)
common = user1_followers & user2_followers
print(f" Mutual Followers: {common}")

# 2. Unique to user1 (Difference -)
only_user1 = user1_followers - user2_followers
print(f" Followers unique to User 1: {only_user1}")

# 3. Total unique followers combined (Union |)
total_unique = user1_followers | user2_followers
print(f" Total unique followers in the network: {len(total_unique)}")

# 4. Suggest friends to User 1 (Followers of User 2 that User 1 doesn't know)
suggested_friends = user2_followers - user1_followers
print(f" Suggested Friends for User 1: {suggested_friends}")