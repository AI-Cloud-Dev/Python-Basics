# Task 1: The "Unique Username" Filter
# Real-Time Scenario: You are cleaning a database of sign-ups.

raw_usernames = ["user1", "admin", "user1", "guest", "admin", "tester"]

unique_usernames = set(raw_usernames)
unique_usernames.add("dev_user")
unique_usernames.add("admin")
print(unique_usernames)

# Task 2: The "Security Audit" (Set Logic)
# Real-Time Scenario: You are comparing permissions between two different security groups.

group_a = {"alice", "Bob", "Charlie", "David"}
group_b = {"Charlie", "David", "edward", "Frank"}

both_access_mem= group_a.intersection(group_b)
only_building_access = group_a.difference(group_b)
any_access = group_a.union(group_b)
print(both_access_mem)
print(only_building_access)
print(any_access)
