"""
There are just some things you can't do on television. In this case, you've just come back from having a "delicious" Barth burger and you're set to give an interview. The Barth burger has made you queezy, and you've forgotten some of the import rules of the "You Can't Do That on Television" set.

If you say any of the following words a large bucket of "water" will be dumped on you: "water", "wet", "wash" This is true for any form of those words, like "washing", "watered", etc.

If you say any of the following phrases you will be doused in "slime": "I don't know", "slime"

If you say both in one sentence, a combination of water and slime, "sludge", will be dumped on you.

Write a function, bucketOf(str), that takes a string and determines what will be dumped on your head. If you haven't said anything you shouldn't have, the bucket should be filled with "air". The words should be tested regardless of case.
"""
"""
Test cases:
Test.assert_equals(bucket_of("wet water"), "water")
Test.assert_equals(bucket_of("slime water"), "sludge")
Test.assert_equals(bucket_of("I don't know if this will work"), "slime")
Test.assert_equals(bucket_of("I don't know if this will work without watering it first."), "sludge")
Test.assert_equals(bucket_of(""), "air")
"""

def bucket_of(said):
    list_o_words = said.split(" ")
    key_words = []
    for word in list_o_words:
        if word in ["water", "wash", "wet", "slime", "I", "don't", "know"]:
            key_words.append(word)
    

x = bucket_of("water")   
assert(x) == "water"
print x
