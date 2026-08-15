
users = [
    {
        "username": "ameer",
        "followers": ["ali", "sara", "nida"],
        "following": ["sara", "hassan"]
    },
    {
        "username": "sara",
        "followers": ["ameer", "zara"],
        "following": ["ameer", "ali"]
    }
]

# Work with the first user (ameer) for these examples
target_user = users[0]

# 1. Mutual followers (Followers who I also follow)
# Converting lists to sets allows us to use the intersection (&) operator easily
followers_set = set(target_user["followers"])
following_set = set(target_user["following"])
mutuals = followers_set & following_set

print(f" Mutual followers of {target_user['username']}: {mutuals}")

# 2. Unfollow someone
user_to_unfollow = "hassan"
if user_to_unfollow in target_user["following"]:
    target_user["following"].remove(user_to_unfollow)
    print(f" {target_user['username']} unfollowed {user_to_unfollow}.")

# 3. Suggest new follows (People my followers follow, but I don't)
# Let's just suggest a list of random platform users not in my 'following'
all_platform_users = {"ali", "sara", "nida", "hassan", "zara", "bilal"}
# Remove people I am already following, and remove myself
suggestions = all_platform_users - set(target_user["following"]) - {target_user["username"]}
print(f" Follow Suggestions for {target_user['username']}: {suggestions}")

# 4. Most followed user on the platform
most_followed = max(users, key=lambda u: len(u["followers"]))
print(f"\n Most Followed User: {most_followed['username']} with {len(most_followed['followers'])} followers!")