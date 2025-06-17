def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s = input("Enter the first string (s): ").strip()
t = input("Enter the second string (t): ").strip()

if isAnagram(s, t):
    print("Output: True (They are anagrams)")
else:
    print("Output: False (They are not anagrams)")