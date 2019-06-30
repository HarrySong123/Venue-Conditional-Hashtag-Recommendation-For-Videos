# Hashtag Recommendation

## each file's usage
jsonread.py: Read json file;

transDes.py:Transfer the 'location_videos_description' file's content (videoid&its description) to a json file which contains the videoid and its hashtag, at last we store them in hashtagTest.json

hashtagTest.json:The storage file of results of 'transDes.py';

hashtagDicWithUTF8.json:The storage file which written in coding of 'utf-8' by 'transDes.py';

hashtagEnglish.json:The storage file which written by 'transDes.py' only containing English;

location_videos_description:The file which contains videoid and its textual description;
    
h5read.py:The python script to read HDF5 file;

raw_dataset.h5:A HDF5 file which contains videoid, features, labels(in venue id);

allhashtag.txt:The hashtag list which doesn't have repeated words;

allhashtagWithUTF8.txt:The hashtag list which doesn't have repeated words and written in coding of UTF8;

leaf_venue_name:The file contains venueid and its venue;

json2onehot.py:The script which get unrepeating hashtags from 'hashtagEnglish.json' and store its result in 'allEnglishHashtag.txt';

allEnglishHashtag.txt:The file stores a list of EnglishHashtag without repeating words and we can get;

readList.py:Read a txt which contains a list;

Dic2labelDic.py:Transform a dictionary with words into a dictionary only contains labels of words and stores the result in 'hashtagLabel.json';