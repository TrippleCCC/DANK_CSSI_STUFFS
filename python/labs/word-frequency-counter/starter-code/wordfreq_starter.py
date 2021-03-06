#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time


def read_process_data():
    with open('third_party/jane-eyre.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content


# You do not need to call this function unless you are doing level 3
def get_stop_words():
    with open('stop-words.txt') as f:
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content.split(' ')

def get_highest_words(counts_dictionary, count):
    print("The top {x} word(s) is/are...".format(x = count))
    highest = sorted(counts_dictionary.items(), key=lambda x:x[1])[::-1][:count]
    for word in highest:
        print("%s: %s" % (word[0], word[1]))

def remove_empty_strings(word_lst):
    word_lst.sort()
    while(word_lst[0] == ""):
        word_lst.pop(0)

content = read_process_data()


# Write your solution below!
word_count = {}
stop_words = get_stop_words()

temp = time.time()
words = content.split(" ")
print("The content split took {t}".format(t = time.time() - temp))


temp = time.time()
remove_empty_strings(words)
print("The remove_empty_strings funtion took {t}".format(t = time.time() - temp))


temp = time.time()
for word in words:
    if(word not in word_count and word not in stop_words):
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1

print("The tally took {t}".format(t = time.time() - temp))

get_highest_words(word_count, 15)
